from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = '22939302'
api_hash = 'a8fac63e89cb8c003cbcfef3a21e550f'
phone_number = '+919027401844'

# Run this script once to generate the session string
with TelegramClient(StringSession(), api_id, api_hash) as client:
    client.start(phone=phone_number)
    session_string = client.session.save()
    with open ('session_string.session', 'w') as f:
        f.write(session_string)
    print("Session String:", session_string)