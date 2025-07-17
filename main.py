from pyrogram import Client, filters
from pyrogram.types import Message
from config import BOT_TOKEN, API_ID, API_HASH
import utils

app = Client("milliy_videosave_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.command("start"))
async def start(client, message: Message):
    user = message.from_user
    await message.reply(f"👋 Salom, {user.first_name}!

@kulgumaxx kanaliga obuna bo‘lganingizdan so‘ng istalgan video havolasini yuboring. Biz uni siz uchun yuklab beramiz.")

@app.on_message(filters.text)
async def handle_link(client, message: Message):
    url = message.text
    await message.reply("🔄 Yuklab olinmoqda...")
    result = utils.download_video(url)
    if result["ok"]:
        await message.reply_video(result["file"], caption="✅ Yuklab olindi!")
    else:
        await message.reply("❌ Xatolik: " + result["error"])

app.run()