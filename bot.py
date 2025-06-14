from pyrogram import Client, filters
from pyrogram.types import Message
import os

# Bot credentials
API_ID = 23787144
API_HASH = "697fa4cd65f9a3c6044111c419f39a8f"
BOT_TOKEN = "8088181644:AAE-k-VfkFPGVLhxudxtgbxdBoz75PoRR-U"

# Initialize bot client
app = Client("loadallbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Start command
@app.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply_text(
        "👋 Welcome to LoadAllBot!\n\n"
        "Send me any supported URL (YouTube, Instagram, etc.), and I’ll fetch it for you.\n\n"
        "⚠️ Channel join check is disabled for now."
    )

# Download handler (WIP — for now, just echoes back the message)
@app.on_message(filters.text & ~filters.command("start"))
async def handle_download(client, message: Message):
    url = message.text.strip()
    await message.reply_text(f"📥 You sent: {url}\n(Download feature coming soon!)")

# Run the bot
app.run()
