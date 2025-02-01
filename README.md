# Telegram-chat-saver
Telegram chat saver bot / телеграмм бот сохраняющий сообщения

# 📬 Telegram Bot на Python

Этот проект представляет собой Telegram-бота, написанного на Python с использованием библиотеки **Telethon**. Бот автоматически отслеживает сообщения, отвечает на команды и взаимодействует с пользователями в режиме реального времени.

## 🚀 Функционал

- **Автоматическая обработка сообщений:** Бот слушает входящие сообщения и реагирует в зависимости от их содержимого.
- **Поддержка команд:** Встроенные команды для управления ботом и взаимодействия с пользователями.
- **Гибкость и расширяемость:** Легко добавляйте новые команды и улучшайте функционал.

## 🛠️ Установка и настройка

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Создайте и активируйте виртуальное окружение (рекомендуется):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Настройте данные API:**

   Зарегистрируйте приложение в [my.telegram.org](https://my.telegram.org), чтобы получить:

   - `API_ID`
   - `API_HASH`

   Создайте файл `.env` в корне проекта и добавьте:

   ```env
   API_ID=your_api_id
   API_HASH=your_api_hash
   SESSION_NAME=your_session_name
   ```

5. **Запуск бота:**

   ```bash
   python3 remain.py
   ```

## 💡 Доступные команды

- `/start` — Приветственное сообщение от бота.
- `/help` — Показать список всех доступных команд.
- `/status` — Проверить текущий статус бота.
- `/echo <сообщение>` — Бот повторит ваше сообщение.
- `/stop` — Остановить бота (только для администратора).

## 📂 Структура проекта

```
your-repo/
├── remain.py            # Основной скрипт бота
├── requirements.txt     # Зависимости проекта
├── README.md            # Описание проекта
└── .env                 # Конфигурационный файл с API-ключами (не добавлять в публичные репозитории)
```

## ⚙️ Зависимости

- [Telethon](https://github.com/LonamiWebs/Telethon) — асинхронная библиотека для работы с Telegram API.
- [python-dotenv](https://github.com/theskumar/python-dotenv) — для удобной работы с переменными окружения.

Установите зависимости через:

```bash
pip install telethon python-dotenv
```

## ❗ Важные замечания

- **Безопасность:** Никогда не публикуйте свои API-ключи в публичных репозиториях. Используйте файл `.env` и добавьте его в `.gitignore`.
- **Ограничения API:** Убедитесь, что соблюдаете лимиты Telegram API, чтобы избежать блокировки.

## 📄 Лицензия

Этот проект распространяется под лицензией [MIT](LICENSE).
