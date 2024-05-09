# pip install cryptg telethon
from telethon import TelegramClient
import os 

# Remember to use your own values from my.telegram.org!
api_id = 0
api_hash = 'x'

chat = 0

client = TelegramClient('anon', api_id, api_hash)

async def main():
    for message in reversed(await client.get_messages(chat, None)):
        os.mkdir('./downloads/'+str(message.id))
        await message.download_media(file="./downloads/"+str(message.id))
    
with client:
    client.loop.run_until_complete(main())