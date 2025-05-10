import string
import zipfile
import os
import json
import random

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
    var config = {
        mode: "fixed_servers",
        rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: %s
            },
            bypassList: [
                "localhost",
                "*.cloudflare.com",
                "challenges.cloudflare.com",
                "*.turnstile.com",
                "turnstile.com"
            ]
        }
    };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        // 跳过 Turnstile 相关域名的代理认证
        if (details.url.includes('turnstile.com') || 
            details.url.includes('cloudflare.com')) {
            return {};
        }
        
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
        callbackFn,
        {urls: ["<all_urls>"]},
        ['blocking']
    );

    // 监听请求，对特定域名不使用代理
    chrome.webRequest.onBeforeRequest.addListener(
        function(details) {
            if (details.url.includes('turnstile.com') || 
                details.url.includes('cloudflare.com')) {
                return {cancel: false};
            }
        },
        {
            urls: ["<all_urls>"]
        },
        ["blocking"]
    );
    """ % (proxy_host, proxy_port, username, password)

    # 创建插件目录
    plugin_dir = 'proxy_auth_plugin'
    if not os.path.exists(plugin_dir):
        os.makedirs(plugin_dir)

    # 写入manifest.json
    with open(os.path.join(plugin_dir, "manifest.json"), 'w') as f:
        f.write(manifest_json.strip())

    # 写入background.js
    with open(os.path.join(plugin_dir, "background.js"), 'w') as f:
        f.write(background_js.strip())

    return plugin_dir 