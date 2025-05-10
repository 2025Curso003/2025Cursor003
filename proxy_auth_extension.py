import string
import zipfile
import os
import json
import random
import logging

# 配置logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def generate_proxy_extension(proxy_host, proxy_port, username, password):
    """生成代理认证插件"""
    
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "webRequest",
            "webRequestBlocking",
            "<all_urls>"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = """
    // 创建一个简单的日志函数
    function logToConsole(message) {
        var timestamp = new Date().toISOString();
        var logMessage = timestamp + " - INFO - " + message;
        console.log(logMessage);
        
        // 如果需要，也可以将日志发送到后台服务器
        // fetch('/log', {
        //     method: 'POST',
        //     body: JSON.stringify({message: logMessage})
        // });
    }

    var bypassDomains = [
        "localhost",
        "*.cloudflare.com",
        "challenges.cloudflare.com",
        "*.turnstile.com",
        "turnstile.com",
        "client-api.arkoselabs.com",
        "*.client-api.arkoselabs.com",
        "cdn.cloudflare.com",
        "static.cloudflareinsights.com",
        "*.cloudflareinsights.com",
        "hcaptcha.com",
        "*.hcaptcha.com",
        "assets.hcaptcha.com",
        "newassets.hcaptcha.com"
    ];

    var config = {
        mode: "fixed_servers",
        rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: parseInt("%s"),
            },
            bypassList: bypassDomains
        }
    };

    // 设置代理并添加回调以确认设置成功
    chrome.proxy.settings.set(
        {value: config, scope: "regular"}, 
        function() {
            // 验证代理设置是否成功应用
            chrome.proxy.settings.get(
                {'incognito': false},
                function(config) {
                    logToConsole('Current proxy settings: ' + JSON.stringify(config));
                }
            );
        }
    );

    // 监听代理错误
    chrome.proxy.onProxyError.addListener(function(details) {
        logToConsole('Proxy error: ' + JSON.stringify(details));
    });

    function shouldBypassDomain(url) {
        let shouldBypass = bypassDomains.some(function(domain) {
            domain = domain.replace('*.', '');
            return url.includes(domain);
        });
        logToConsole('URL: ' + url + ' Bypass: ' + shouldBypass);
        return shouldBypass;
    }

    function callbackFn(details) {
        logToConsole('Auth required for: ' + details.url);
        if (shouldBypassDomain(details.url)) {
            logToConsole('Bypassing auth for: ' + details.url);
            return {};
        }
        
        logToConsole('Using proxy auth for: ' + details.url);
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    // 监听所有请求以记录代理使用情况
    chrome.webRequest.onBeforeRequest.addListener(
        function(details) {
            logToConsole('Request: ' + details.url);
            if (shouldBypassDomain(details.url)) {
                logToConsole('Bypassing proxy for: ' + details.url);
                return {cancel: false};
            }
            logToConsole('Using proxy for: ' + details.url);
        },
        {urls: ["<all_urls>"]},
        ["blocking"]
    );

    chrome.webRequest.onAuthRequired.addListener(
        callbackFn,
        {urls: ["<all_urls>"]},
        ["blocking"]
    );
    """ % (proxy_host, proxy_port, username, password)

    # 创建插件目录
    plugin_dir = 'proxy_auth_plugin'
    if not os.path.exists(plugin_dir):
        os.makedirs(plugin_dir)
        logging.info(f"Created plugin directory: {plugin_dir}")

    # 写入manifest.json
    manifest_path = os.path.join(plugin_dir, "manifest.json")
    with open(manifest_path, 'w') as f:
        f.write(manifest_json.strip())
    logging.info(f"Written manifest.json to {manifest_path}")

    # 写入background.js
    background_path = os.path.join(plugin_dir, "background.js")
    with open(background_path, 'w') as f:
        f.write(background_js.strip())
    logging.info(f"Written background.js to {background_path}")

    logging.info(f"Proxy extension generated successfully with host: {proxy_host}, port: {proxy_port}")
    return plugin_dir 