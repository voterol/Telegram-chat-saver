# Telegram-chat-saver
Telegram chat saver bot / телеграмм бот сохраняющий сообщения

# 📬 Telegram Bot на Python

Этот проект представляет собой Telegram-бота, написанного на Python с использованием библиотеки **Telethon**. Бот автоматически отслеживает сообщения, отвечает на команды и взаимодействует с пользователями в режиме реального времени.

## 🚀 Функционал

- **Автоматическая обработка сообщений:** Бот слушает входящие сообщения и реагирует в зависимости от их содержимого.
- **Поддержка команд:** Встроенные команды для управления ботом и взаимодействия с пользователями.
- **Гибкость и расширяемость:** Легко добавляйте новые команды и улучшайте функционал.

## 🛠️ Установка и настройка
1. **Установка одной командой** Не забудте сменить API
  ```bash
git clone https://github.com/voterol/Telegram-chat-saver && \
cd Telegram-chat-saver && \
chmod +x setup.sh root_start_bot.sh start.sh && \
./start.sh

  ```
1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/voterol/Telegram-chat-saver
   cd Telegram-chat-saver
   ```


2. **Установите зависимости:**

   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```


3. **Настройте данные API:**

   Зарегистрируйте приложение в [my.telegram.org](https://my.telegram.org), чтобы получить:

   - `API_ID`
   - `API_HASH`

   Запустите main.py (если запускаете setup.sh то он сам запустится) и если отсутствует `api.conf` то он создатся с кодом:

   ```env
   API_ID=your_api_id
   API_HASH=your_api_hash
   ```
   Замените эти данные на свои

4. **Запуск бота:**

   ```bash
   python3 main.py
   ```
  или
  ```bash
  chmod +x start.sh  
  ./start.sh
  ```

## 💡 Доступные команды

- `/ignore` — добавляет чат в список игнорируемых поддерживает как ссылки так и id
- `/ignore_bots` — Игнорирует удаления и изменения сообщений в ботах (Ваши так же читаются)


## 📂 Структура проекта

```
your-repo/
├── main.py            # Основной скрипт бота
├── requirements.txt     # Зависимости проекта
├── README.md            # Описание проекта
└── api.conf             # Конфигурационный файл с API-ключами (не добавлять в публичные репозитории)
```

## ⚙️ Зависимости (Для ручной установки)

- [Telethon](https://github.com/LonamiWebs/Telethon) — асинхронная библиотека для работы с Telegram API.
- [python-dotenv](https://github.com/theskumar/python-dotenv) — для удобной работы с переменными окружения.
- [requets](https://github.com) - для запросов
Установите зависимости через:

```bash
pip3 install telethon python-dotenv requests
```
Или

```bash
pip install telethon python-dotenv requests
```

## ❗ Важные замечания

- **Безопасность:** Никогда не публикуйте свои API-ключи в публичных репозиториях. Используйте файл `.env` и добавьте его в `.gitignore`.
- **Ограничения API:** Убедитесь, что соблюдаете лимиты Telegram API, чтобы избежать блокировки.

## 📄 Лицензия

Этот проект распространяется под лицензией [MIT](LICENSE).
