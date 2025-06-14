from pyrogram import Client, filters
from pytube import YouTube
import os

API_ID = 23787144
API_HASH = "697fa4cd65f9a3c6044111c419f39a8f"
BOT_TOKEN = "8088181644:AAE-k-VfkFPGVLhxudxtgbxdBoz75PoRR-U"

app = Client("loadallbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

CHANNEL_USERNAME = "kkcloots"
WATERMARK_TEXT = "Kkc"

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("👋 Welcome to LoadAllBot!\n\nSend any YouTube or Instagram link to download.")

@app.on_message(filters.text & ~filters.command(["start"]))
async def handle_link(client, message):
    user = await client.get_chat_member(CHANNEL_USERNAME, message.from_user.id)
    if user.status not in ("member", "administrator", "creator"):
        await message.reply_text("❌ Please join our channel @kkcloots to use this bot.")
        return

    url = message.text.strip()

    if "youtube.com" in url or "youtu.be" in url:
        try:
            yt = YouTube(url)
            stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
            filename = stream.download(filename_prefix=WATERMARK_TEXT + "_")
            await message.reply_video(video=filename, caption=f"{WATERMARK_TEXT} | Downloaded from YouTube")
            os.remove(filename)
        except Exception as e:
            await message.reply_text(f"❌ Failed to download: {e}")
    else:
        await message.reply_text("⚠️ Currently, only YouTube links are supported.")

app.run()
