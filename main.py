import os
import json
from telethon import TelegramClient, events
import asyncio
import sys

CONFIG_FILE = 'conf.configs'
API_CONFIG_FILE = 'api.conf'

# Функция для загрузки конфигурации API
def load_api_config():
    if os.path.exists(API_CONFIG_FILE):
        try:
            with open(API_CONFIG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Ошибка при чтении конфигурационного файла API: {e}.")
            sys.exit()  # Выход из программы в случае ошибки при чтении
    else:
        print(f"Файл {API_CONFIG_FILE} не найден. Создаю файл с дефолтными значениями.")
        return create_default_api_config()

# Функция для создания дефолтного конфигурационного файла API
def create_default_api_config():
    default_api_config = {
        "api_id": 12312312,  # Замените на ваш API ID
        "api_hash": "123456789012345678901234567890123"  # Замените на ваш API HASH
    }
    with open(API_CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(default_api_config, f, ensure_ascii=False, indent=4)
    return default_api_config

# Функция для изменения API_ID и API_HASH, если они дефолтные
def change_api_credentials_if_default():
    api_config = load_api_config()
    api_id = api_config.get('api_id')
    api_hash = api_config.get('api_hash')
    
    if api_id == 12312312 and api_hash == "123456789012345678901234567890123":
        print("Используются дефолтные значения для API ID и API Hash.")
        api_id = input(f"Введите новый API ID (текущий: {api_id}): ") or api_id
        api_hash = input(f"Введите новый API Hash (текущий: {api_hash}): ") or api_hash
        
        # Обновляем файл с новыми значениями
        new_config = {
            "api_id": api_id,
            "api_hash": api_hash
        }
        with open(API_CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(new_config, f, ensure_ascii=False, indent=4)
        
        print("API ID и API Hash обновлены.")
    return api_id, api_hash

# Проверка и смена API_ID и API_HASH, если они дефолтные
API_ID, API_HASH = change_api_credentials_if_default()

ARCHIVE_BOT_ID = 777000  # ID бота-архиватора

client = TelegramClient('my_session', API_ID, API_HASH)

message_storage = {}

# Функция для загрузки конфигурации
def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Ошибка при чтении конфигурационного файла: {e}. Создаем новый файл с настройками по умолчанию.")
            return create_default_config()
    else:
        return create_default_config()

# Создание конфигурации с настройками по умолчанию
def create_default_config():
    default_config = {
        'ignore_groups': [],
        'ignore_bots': False,
        'ignore_users': []
    }
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(default_config, f, ensure_ascii=False, indent=4)
    return default_config

# Сохраняем настройки в файл
def save_config(config):
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=4)

config = load_config()

async def start_client():
    await client.start()
    if not await client.is_user_authorized():
        phone_number = os.getenv('TELEGRAM_PHONE')
        if not phone_number:
            try:
                phone_number = input("Введите ваш номер телефона: ")
            except KeyboardInterrupt:
                print("\nПроцесс был прерван пользователем.")
                sys.exit()
        
        await client.send_code_request(phone_number)
        try:
            code = input("Введите код подтверждения: ")
        except KeyboardInterrupt:
            print("\nПроцесс был прерван пользователем.")
            sys.exit()

        try:
            await client.sign_in(phone_number, code)
        except Exception as e:
            print(f"Ошибка при авторизации: {e}")
            try:
                password = input("Введите пароль для двухфакторной аутентификации: ")
            except KeyboardInterrupt:
                print("\nПроцесс был прерван пользователем.")
                sys.exit()
            await client.sign_in(password=password)

@client.on(events.NewMessage)
async def handle_new_message(event):
    sender = await event.get_sender()
    sender_name = sender.username if sender.username else "Unknown"
    text = event.message.text or "Нет текста"
    media = None  # По умолчанию нет медиа

    # Проверяем наличие вложений (фото, видео и т.д.)
    if event.message.media:
        media = event.message.media

    # Запоминаем сообщение
    message_storage[event.message.id] = (sender_name, text, media)

    # Если игнорируем этого отправителя, игнорируем сообщение
    if sender_name in config['ignore_users']:
        return

    # Если это бот и игнорирование ботов включено
    if config['ignore_bots'] and sender.bot:
        return

    # Если это группа, и игнорируем группу
    if event.chat_id in config['ignore_groups']:
        return

@client.on(events.MessageDeleted)
async def handle_deleted_message(event):
    for msg_id in event.deleted_ids:
        if msg_id in message_storage:
            sender_name, text, media = message_storage.pop(msg_id)

            # Проверяем, если чат игнорируемый, не обрабатываем удаление
            if event.chat_id in config['ignore_groups']:
                return

            # Формируем ссылку на отправителя
            sender_link = f"[{sender_name}](http://t.me/{sender_name})" if sender_name != "Unknown" else "Неизвестный пользователь"

            message_content = f"‼️ Сообщение удалено!\n\nОт: {sender_link}\n{text}"

            if media:
                try:
                    await client.send_file(ARCHIVE_BOT_ID, media, caption=message_content)
                except Exception as e:
                    print(f"Ошибка при отправке медиа: {e}")
            else:
                await client.send_message(ARCHIVE_BOT_ID, message_content)

@client.on(events.MessageEdited)
async def handle_edited_message(event):
    sender = await event.get_sender()
    sender_name = sender.username if sender.username else "Unknown"
    new_text = event.message.text or "Нет текста"
    media = event.message.media if event.message.media else None

    # Проверяем, если чат игнорируемый, не обрабатываем изменение
    if event.chat_id in config['ignore_groups']:
        return

    # Формируем ссылку на отправителя (аналогично удаленному сообщению)
    sender_link = f"[{sender_name}](http://t.me/{sender_name})" if sender_name != "Unknown" else "Неизвестный пользователь"

    if event.message.id in message_storage:
        old_sender_name, old_text, old_media = message_storage[event.message.id]

        if old_text != new_text:
            edit_message = (
                f"✏️ *Сообщение отредактировано!*\n"
                f"**От:** {sender_link}\n"  # Используем формат с ссылкой
                f"**Старое сообщение:** {old_text}\n"
                f"**Новое сообщение:** {new_text}"
            )
            await client.send_message(ARCHIVE_BOT_ID, edit_message)

        message_storage[event.message.id] = (sender_name, new_text, media)
    else:
        edit_message = (
            f"✏️ *Сообщение отредактировано!*\n"
            f"**От:** {sender_link}\n"  # Используем формат с ссылкой
            f"**Старое сообщение:** Неизвестно (сообщение не сохранено ранее)\n"
            f"**Новое сообщение:** {new_text}"
        )
        await client.send_message(ARCHIVE_BOT_ID, edit_message)
        message_storage[event.message.id] = (sender_name, new_text, media)

@client.on(events.NewMessage(pattern='/ignore'))
async def ignore_command(event):
    chat_link = event.text.split(' ')[1] if len(event.text.split()) > 1 else ''
    if chat_link.startswith('https://t.me/'):
        chat_link = chat_link.split('/')[-1]  # Получаем username
        if chat_link not in config['ignore_groups']:
            config['ignore_groups'].append(chat_link)
            save_config(config)
            await event.reply(f"Группа {chat_link} теперь игнорируется.")
        else:
            await event.reply(f"Группа {chat_link} уже в списке игнорируемых.")
    else:
        await event.reply("Введите правильную ссылку на чат.")

@client.on(events.NewMessage(pattern='/ignore_bots'))
async def ignore_bots_command(event):
    config['ignore_bots'] = True
    save_config(config)
    print(f"ignore_bots изменен на: {config['ignore_bots']}")  # Добавляем логирование
    await event.reply("Боты теперь игнорируются.")

@client.on(events.NewMessage(pattern='/unignore_bots'))
async def unignore_bots_command(event):
    config['ignore_bots'] = False
    save_config(config)
    print(f"ignore_bots изменен на: {config['ignore_bots']}")  # Логирование изменения
    await event.reply("Боты больше не игнорируются.")

@client.on(events.NewMessage(pattern='/ignore_users'))
async def ignore_users_command(event):
    username = event.text.split(' ')[1] if len(event.text.split()) > 1 else ''
    if username:
        if username not in config['ignore_users']:
            config['ignore_users'].append(username)
            save_config(config)
            await event.reply(f"Пользователь {username} теперь игнорируется.")
        else:
            await event.reply(f"Пользователь {username} уже в списке игнорируемых.")
    else:
        await event.reply("Введите правильный username пользователя для игнорирования.")

@client.on(events.NewMessage(pattern='/unignore'))
async def unignore_command(event):
    chat_link = event.text.split(' ')[1] if len(event.text.split()) > 1 else ''
    if chat_link.startswith('https://t.me/'):
        chat_link = chat_link.split('/')[-1]
        if chat_link in config['ignore_groups']:
            config['ignore_groups'].remove(chat_link)
            save_config(config)
            await event.reply(f"Группа {chat_link} больше не игнорируется.")
        else:
            await event.reply(f"Группа {chat_link} не была добавлена в игнор.")
    else:
        await event.reply("Введите правильную ссылку на чат.")

async def main():
    print("Бот запущен, ждёт сообщений и удалений...")
    await start_client()
    await client.run_until_disconnected()

if __name__ == "__main__":
    try:
        client.loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("\nБот остановлен пользователем.")
