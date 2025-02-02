#!/bin/bash

# Функция для запроса пути к папке, пока она не будет найдена
get_folder() {
    while true; do
        echo "Введите путь к директории вашего Telegram-бота (например, /root/Telegram-chat-saver):"
        read telegram_folder

        # Проверка существования папки
        if [ -d "$telegram_folder" ]; then
            break
        else
            echo "Папка $telegram_folder не найдена. Попробуйте снова."
        fi
    done
}

# Вызов функции для получения правильного пути
get_folder

# Создание файла systemd для автозапуска
echo "[Unit]
Description=Start Telegram on Boot

[Service]
ExecStartPre=/bin/sleep 4
ExecStart=$telegram_folder/startup.sh
Restart=always
User=root

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/telegram-start.service

# Перезагрузка systemd для регистрации нового сервиса
systemctl daemon-reload

# Включение автозапуска сервиса
systemctl enable telegram-start.service

# Запуск сервиса немедленно (по желанию)
systemctl start telegram-start.service

screen -r telegram_session
