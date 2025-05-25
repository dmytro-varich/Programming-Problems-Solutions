import re
import asyncio
import logging
from telethon import TelegramClient, events
from cachetools import cached, TTLCache

loop = asyncio.get_event_loop()

# Конфигурация кэша
CACHE_SIZE = 1000  # Размер кэша
CACHE_TTL = 300    # Время жизни записей в кэше (в секундах)

# Создание клиента Telegram
client = TelegramClient('dmytro_varich', api_id=api_id, api_hash=api_hash, proxy=None)

# Создание кэша
user_cache = TTLCache(maxsize=CACHE_SIZE, ttl=CACHE_TTL)
participants_cache = TTLCache(maxsize=CACHE_SIZE, ttl=CACHE_TTL)

# Функция для получения информации о пользователе с кэшированием
@cached(user_cache)
async def get_user_info(username):
    try:
        target_user = await client.get_entity(username)
        return target_user
    except Exception as e:
        logging.error(f'Error fetching user info for {username}: {e}')
        return None

# Функция для получения списка участников чата с кэшированием
@cached(participants_cache)
async def get_chat_participants(chat_id):
    try:
        participants = await client.get_participants(chat_id)
        return participants
    except Exception as e:
        logging.error(f'Error fetching chat participants for {chat_id}: {e}')
        return None

# Функция для обработки сообщений
async def handle_message(event):
    if await check_mentions(event.message.text) or await check_lust_link(event.message.text):
        recipient = await event.get_chat()

        if (event.is_private and (recipient.is_self or recipient.id == SECOND_ACCOUNT_ID or recipient.bot)):
            try:
                await event.delete()
            except Exception as e:
                logging.error(f"Ошибка при удалении сообщения: {e}")

        if event.is_group or event.is_channel:
            try:
                participants = await get_chat_participants(event.chat_id)
                count = 0
                for participant in participants:
                    if participant.id == SECOND_ACCOUNT_ID or participant.bot or participant.id == MAIN_ACCOUNT_ID:
                        count += 1
                if count == participants.total:
                    await event.delete()
            except Exception as e:
                logging.error(f"Ошибка при проверке группы/канала: {e}")

# Обработчик новых сообщений
@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    await handle_message(event)

# Обработчик редактированных сообщений
@client.on(events.MessageEdited(outgoing=True))
async def handler(event):
    await handle_message(event)

# Функция для проверки упоминаний пользователей
async def check_mentions(text):
    pattern = r'(?:^|\s)@[a-zA-Z\d_]{4,}(?![\w\d_])'
    return bool(re.search(pattern, text, flags=re.IGNORECASE))

# Функция для проверки ссылок на запрещенный контент
async def check_lust_link(text) -> bool:
    pattern = r"(https?://t\.me/\S+?)(?=[^_\da-zA-Z]|\s)"
    match_list = re.split(pattern, text)
    if match_list:
        try: 
            links = [m_l for m_l in match_list if 'https://t.me/' in m_l]
            for link in links:
                target_user = await get_user_info('@' + link.lstrip('https://t.me/'))
                if target_user:
                    first_name = target_user.first_name
                    last_name = target_user.last_name if last_name is not None else 'None'
                    if await check_prohibited_content(first_name) or await check_prohibited_content(last_name):
                        return True 
        except Exception as e:
            logging.error(f'Error in check_lust_link: {e}')
    return False

# Функция для проверки наличия ссылок на запрещенный контент в тексте
async def check_prohibited_content(text):
    prohibition_patterns = [
        r'\b18[+]', 
        r'\bporn',
        r'\bonlyfan',
        r'🔞',
        r'\bxxx\b',
        r'\bporn\b',
        r'\bsex',
        r'\badult\b',
        r'\bxxxvideo\b',
        r'\bpornhub\b',
        r'\bsexshop\b',
        r'\berotic\b',
        r'\bxxxmovies\b',
        r'\badult entertainment\b',
        r'\bsex chat\b',
        r'\blive cam\b',
        r'\bhot girls\b',
        r'\berotic stories\b',
        r'\bbeaty girl',
        r'\bonlyk', 
        r'\bхентай',
        r'\bhentai',
        r'\bbitch', 
        r'\bfuck', 
        r'\berotic', 
        r'\bdick\b', 
        r'\banal'
    ]
    for pattern in prohibition_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False

async def main():
    logging.info("Starting client...")
    async with client:
        await client.run_until_disconnected()
    logging.info("Client disconnected")

# prepare the logger
logging.basicConfig(level=logging.DEBUG)

# Запуск асинхронного цикла
loop.run_until_complete(main())