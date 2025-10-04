"""
Run this script LOCALLY to generate your session string.
This only needs to be done once.
"""
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = input('Enter your API_ID: ')
API_HASH = input('Enter your API_HASH: ')

async def main():
    client = TelegramClient(StringSession(), API_ID, API_HASH)
    await client.start()
    
    session_string = client.session.save()
    print("\n" + "="*50)
    print("YOUR SESSION STRING:")
    print("="*50)
    print(session_string)
    print("="*50)
    print("\nSave this session string securely!")
    print("You'll need to add it as SESSION_STRING in Railway environment variables.")
    
    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())