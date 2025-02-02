#!/bin/bash
# Create the systemd service file for automatic startup
echo "[Unit]
Description=Start Telegram on Boot

[Service]
ExecStart=/root/Telegram/start.sh
Restart=always
User=root

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/telegram-start.service

# Reload systemd to register the new service
systemctl daemon-reload

# Enable the service to start on boot
systemctl enable telegram-start.service

# Start the service immediately (optional)
systemctl start telegram-start.service
