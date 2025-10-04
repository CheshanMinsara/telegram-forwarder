import asyncio
import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# Configuration from environment variables
API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')
SESSION_STRING = os.environ.get('SESSION_STRING')
SOURCE_CHANNEL = os.environ.get('SOURCE_CHANNEL')
TARGET_CHANNEL = os.environ.get('TARGET_CHANNEL')

# Validate environment variables
if not all([API_ID, API_HASH, SESSION_STRING, SOURCE_CHANNEL, TARGET_CHANNEL]):
    raise ValueError("Missing required environment variables!")

# Create client with session string
client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def forward_handler(event):
    """Forward new messages from source to target channel"""
    try:
        # Forward the message
        await client.forward_messages(
            TARGET_CHANNEL,
            event.message
        )
        print(f"✓ Forwarded message {event.message.id}")
    except Exception as e:
        print(f"✗ Error forwarding message: {e}")

async def main():
    """Start the bot"""
    await client.connect()
    
    if not await client.is_user_authorized():
        print("Session string is invalid or expired!")
        return
    
    print("Bot is running and forwarding messages...")
    print(f"Source: {SOURCE_CHANNEL}")
    print(f"Target: {TARGET_CHANNEL}")
    
    # Verify channels exist
    try:
        source = await client.get_entity(SOURCE_CHANNEL)
        target = await client.get_entity(TARGET_CHANNEL)
        print(f"✓ Connected to source: {source.title}")
        print(f"✓ Connected to target: {target.title}")
    except Exception as e:
        print(f"✗ Error: {e}")
        return
    
    # Keep running
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
