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
                port: %s
            },
            bypassList: bypassDomains
        }
    };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function shouldBypassDomain(url) {
        return bypassDomains.some(function(domain) {
            domain = domain.replace('*.', '');
            return url.includes(domain);
        });
    }

    function callbackFn(details) {
        if (shouldBypassDomain(details.url)) {
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

    chrome.webRequest.onBeforeRequest.addListener(
        function(details) {
            if (shouldBypassDomain(details.url)) {
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