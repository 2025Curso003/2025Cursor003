#!/bin/bash

# 更新系统并安装必要的包
sudo apt-get update
sudo apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    wget \
    unzip \
    xvfb \
    libgconf-2-4 \
    libnss3 \
    libxss1 \
    libasound2 \
    libxtst6 \
    libgtk-3-0 \
    libgbm1

# 安装 Chrome
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google.list
sudo apt-get update
sudo apt-get install -y google-chrome-stable

# 创建项目目录和日志目录
mkdir -p /opt/cursor-auto-token
mkdir -p /var/log/cursor-auto-token
chmod 755 /var/log/cursor-auto-token

cd /opt/cursor-auto-token

# 创建并激活虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装项目依赖
pip install -r requirements.txt

# 确保turnstilePatch目录存在
if [ ! -d "turnstilePatch" ]; then
    echo "错误: turnstilePatch 目录不存在"
    exit 1
fi

# 创建系统服务配置
cat > /etc/systemd/system/cursor-auto-token.service << EOL
[Unit]
Description=Cursor Auto Token Service
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/cursor-auto-token
Environment=DISPLAY=:99
Environment=PYTHONUNBUFFERED=1
Environment=WEBSHARE_API_KEY=${WEBSHARE_API_KEY}
Environment=LOG_FILE=/var/log/cursor-auto-token/app.log

# 启动虚拟显示
ExecStartPre=/usr/bin/Xvfb :99 -screen 0 1024x768x16
# 主程序
ExecStart=/opt/cursor-auto-token/venv/bin/python cursor_pro_keep_alive.py

# 重启策略
Restart=always
RestartSec=3

# 限制
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
EOL

# 创建日志文件并设置权限
touch /var/log/cursor-auto-token/app.log
chmod 644 /var/log/cursor-auto-token/app.log

# 配置日志轮转
cat > /etc/logrotate.d/cursor-auto-token << EOL
/var/log/cursor-auto-token/app.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 644 root root
}
EOL

# 重新加载系统服务
sudo systemctl daemon-reload

# 启动服务
sudo systemctl enable cursor-auto-token
sudo systemctl start cursor-auto-token

# 检查服务状态
sudo systemctl status cursor-auto-token

# 等待几秒后检查日志
sleep 5
echo "检查应用日志..."
tail -n 50 /var/log/cursor-auto-token/app.log 