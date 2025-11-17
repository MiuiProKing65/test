from telethon import TelegramClient
import asyncio
from datetime import datetime

# --- Данные твоего приложения ---
api_id = 25889533
api_hash = "ea4dbf39e42c3a04639a7cdb281d6fe7"

# --- Твой номер телефона ---
phone = "+380959069373"

# Создаём клиент (файл сессии сохранится как "my_session.session")
client = TelegramClient("my_session", api_id, api_hash)

# Функция для записи в лог
def write_log(text):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {text}\n")

async def main():
    await client.start(phone=phone)

    # Получаем информацию о пользователе
    me = await client.get_me()
    username = f"@{me.username}" if me.username else me.phone
    write_log(f"✅ Авторизация прошла успешно! Вошёл как {username}")

    # Бесконечный цикл отправки сообщений в избранное
    while True:
        await client.send_message("me", "😎😎 (^_~) ( ﾟｏ⌒) (^_-)≡☆ (^ω~) (>ω^) (~人^) (^_-) ( -_・)😏😏")
        write_log("Сообщение отправлено в Избранное!")
        await asyncio.sleep(5)  # интервал 5 секунд

with client:
    client.loop.run_until_complete(main())