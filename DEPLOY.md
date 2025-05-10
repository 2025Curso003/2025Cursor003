# 阿里云 ECS 部署指南

## 1. 服务器要求

- 操作系统：Ubuntu 20.04 LTS
- 内存：至少 2GB RAM
- CPU：至少 1核
- 磁盘空间：至少 20GB

## 2. 前置准备

1. 登录阿里云控制台，确保以下端口已开放：
   - 22 端口 (SSH)
   - 80 端口 (HTTP，如果需要)
   - 443 端口 (HTTPS，如果需要)

2. 配置安全组规则：
   ```bash
   # 在阿里云控制台
   安全组 -> 配置规则 -> 添加安全组规则
   ```

## 3. 部署步骤

1. 连接到 ECS 实例：
   ```bash
   ssh root@your_ecs_ip
   ```

2. 克隆代码：
   ```bash
   cd /opt
   git clone https://github.com/your-username/cursor-auto-free-token.git
   cd cursor-auto-token
   ```

3. 配置环境变量：
   ```bash
   # 创建环境变量文件
   cp .env.example .env
   
   # 编辑环境变量
   nano .env
   
   # 设置必要的环境变量：
   # - WEBSHARE_API_KEY
   # - 其他必要的配置
   ```

4. 运行部署脚本：
   ```bash
   chmod +x deploy_ecs.sh
   ./deploy_ecs.sh
   ```

5. 检查服务状态：
   ```bash
   systemctl status cursor-auto-token
   ```

## 4. 日志查看

1. 查看服务日志：
   ```bash
   journalctl -u cursor-auto-token -f
   ```

2. 查看应用日志：
   ```bash
   tail -f /var/log/cursor-auto-token/app.log
   ```

## 5. 常见问题处理

1. 如果服务无法启动：
   ```bash
   # 检查日志
   journalctl -u cursor-auto-token -n 50
   
   # 检查 Chrome 是否正确安装
   google-chrome --version
   
   # 检查虚拟显示是否正常
   ps aux | grep Xvfb
   ```

2. 如果代理连接失败：
   ```bash
   # 检查代理配置
   cat .env | grep PROXY
   
   # 测试代理连接
   curl --proxy your_proxy_ip:port http://example.com
   ```

3. 内存问题：
   ```bash
   # 检查内存使用情况
   free -m
   
   # 如果内存不足，考虑添加swap
   sudo fallocate -l 2G /swapfile
   sudo chmod 600 /swapfile
   sudo mkswap /swapfile
   sudo swapon /swapfile
   ```

## 6. 维护指南

1. 更新代码：
   ```bash
   cd /opt/cursor-auto-token
   git pull
   systemctl restart cursor-auto-token
   ```

2. 更新依赖：
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt --upgrade
   systemctl restart cursor-auto-token
   ```

3. 备份配置：
   ```bash
   cp .env .env.backup
   cp -r /var/log/cursor-auto-token/ /backup/
   ```

## 7. 监控建议

1. 设置阿里云监控：
   - CPU 使用率告警
   - 内存使用率告警
   - 磁盘使用率告警

2. 设置应用监控：
   - 服务状态监控
   - 代理可用性监控
   - 成功率监控

## 8. 安全建议

1. 更新系统：
   ```bash
   apt update && apt upgrade -y
   ```

2. 配置防火墙：
   ```bash
   ufw allow ssh
   ufw enable
   ```

3. 设置定期备份：
   ```bash
   # 创建备份脚本
   nano /opt/backup.sh
   
   # 添加到 crontab
   crontab -e
   # 添加：
   # 0 2 * * * /opt/backup.sh
   ``` 