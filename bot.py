from pyrogram import Client, filters
from pyrogram.types import Message
import os

API_ID = 23787144
API_HASH = "697fa4cd65f9a3c6044111c419f39a8f"
BOT_TOKEN = "8088181644:AAE-k-VfkFPGVLhxudxtgbxdBoz75PoRR-U"
REQUIRED_CHANNEL = "kkcloots"
WATERMARK = "Kkc"

app = Client("LoadAllBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def is_joined(client, user_id):
    try:
        member = await client.get_chat_member(REQUIRED_CHANNEL, user_id)
        return member.status in ["member", "creator", "administrator"]
    except Exception:
        return False

@app.on_message(filters.command("start"))
async def start(client, message: Message):
    if not await is_joined(client, message.from_user.id):
        await message.reply_text("❌ Please join our channel @kkcloots to use this bot.")
        return
    await message.reply_text("👋 Welcome to LoadAllBot!
Send any YouTube link to download.")

@app.on_message(filters.text & filters.private)
async def download_handler(client, message: Message):
    if not await is_joined(client, message.from_user.id):
        await message.reply_text("❌ Please join our channel @kkcloots to use this bot.")
        return

    url = message.text.strip()
    if "youtube.com" not in url and "youtu.be" not in url:
        await message.reply_text("⚠️ Currently, only YouTube links are supported.")
        return

    await message.reply_text(f"📥 Downloading with watermark '{WATERMARK}'...
(Not implemented fully in this demo)")


app.run()
