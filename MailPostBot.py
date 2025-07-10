#-----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
# Powered By Deep seek

import os
from pyrogram import Client, filters, enums, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatAction, ParseMode
from pyrogram.types import CallbackQuery
from config import *
import requests
import threading
import json
import asyncio, time
from random import choice
from datetime import datetime
import logging

FORMAT = "[LEGEND-MUKESH] %(message)s"
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

StartTime = time.time()
Mukesh = Client(
    "chat-gpt",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

START = f"""
๏ 𝗠𝗲𝗿𝗵𝗮𝗯𝗮 🌹

Süpriz Mail Kutusuna Hediye bırakabilirim Ama Noel Baba Değilim 
"""

s = bytearray.fromhex("68 74 74 70 73 3A 2F 2F 67 69 74 68 75 62 2E 63 6F 6D 2F 4E 6F 6F 62 2D 6D 75 6B 65 73 68 2F 43 68 61 74 67 70 74 2D 62 6F 74").decode()
SOURCE = s
SOURCE_TEXT = f"""
๏ Heyyo,
"""

x = ["❤️", "🎉", "✨", "🪸", "🎉", "🎈", "🎯"]
g = choice(x)
MAIN = [
    [InlineKeyboardButton(text="Sahip", url=f"https://t.me/{OWNER_USERNAME}")],
    [InlineKeyboardButton(text="Gruba Ekle", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
    [InlineKeyboardButton(text="Yardım Komutlar ", callback_data="HELP")],
]

PNG_BTN = [
    [InlineKeyboardButton(text="Gruba Ekle", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
    [InlineKeyboardButton(text="Grup", url=f"https://t.me/{SUPPORT_GRP}")],
]

SOURCE_BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('source', url=f"{SOURCE}")]])
HELP_READ = "**Kullanım :**  \n\n /smtp = Süpriz Mail Gönder\n\n /ping = Bot Sağlık Sorunları\n\n /plus = Anonim Davetiye Yolla\n\n Bot Version2.1"
HELP_BACK = [
    [InlineKeyboardButton(text="Source ", url=f"https://github.com/ViosRio/MailPostBot")],
    [InlineKeyboardButton(text="⬅️ ", callback_data="HELP_BACK")],
]

@Mukesh.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]))
async def start(client, m: Message):
    try:
        accha = await m.reply_text(text=f"{g}")
        await asyncio.sleep(0.2)
        await accha.edit("✦ Yükleniliyor..")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(sticker=STKR)
        await asyncio.sleep(0.3)
        await umm.delete()
        await m.reply_photo(photo=START_IMG, caption=START, reply_markup=InlineKeyboardMarkup(MAIN))
    except Exception as y:
        await m.reply(str(y))

@Mukesh.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
        if query.message.text != HELP_READ:
            await query.message.edit_text(text=HELP_READ, reply_markup=InlineKeyboardMarkup(HELP_BACK))
    elif query.data == "HELP_BACK":
        if query.message.text != START:
            await query.message.edit_text(text=START, reply_markup=InlineKeyboardMarkup(MAIN))

@Mukesh.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["", "+", ".", "/", "-", "?", "$"]))
async def restart(client, message):
    await message.reply_photo(START_IMG, caption=HELP_READ, reply_markup=InlineKeyboardMarkup(HELP_BACK))

@Mukesh.on_message(filters.command(["source", "repo"], prefixes=["", "+", ".", "/", "-", "?", "$"]))
async def source(bot, m):
    await m.reply_photo(START_IMG, caption=SOURCE_TEXT, reply_markup=SOURCE_BUTTONS)

@Mukesh.on_message(filters.command(["ping", "alive"], prefixes=["+", "/", "-", "?", "$", "&", "."]))
async def ping(client, message: Message):
    start = datetime.now()
    txxt = await message.reply("Bekleyiniz.."); await asyncio.sleep(0.25)
    await txxt.edit_text("✦ Başarılı.."); await asyncio.sleep(0.35)
    await txxt.delete()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await message.reply_photo(photo=START_IMG, caption=f"Hey !!\n**[{BOT_NAME}](t.me/{BOT_USERNAME}) `{ms}` ms\n\n**🌹 || [sahip](https://t.me/{OWNER_USERNAME})||", reply_markup=InlineKeyboardMarkup(PNG_BTN))



@Mukesh.on_message(filters.command(["sendpulse", "sp"]))
async def sendpulse_handler(client: Client, message: Message):
    # Adım 1: E-posta adresi iste
    await message.reply("📧 **Pekala, e-posta adresini giriniz:**")
    user_states[message.from_user.id] = {"step": "awaiting_email"}

@Mukesh.on_message(filters.text & filters.private)
async def handle_user_input(client: Client, message: Message):
    user_id = message.from_user.id
    if user_id not in user_states:
        return

    state = user_states[user_id]
    
    if state["step"] == "awaiting_email":
        # E-posta doğrulama
        if "@" not in message.text or "." not in message.text.split("@")[1]:
            await message.reply("❌ Geçersiz e-posta formatı! Tekrar deneyin:")
            return

        user_states[user_id]["email"] = message.text.strip()
        user_states[user_id]["step"] = "awaiting_message"
        await message.reply("✍️ **Gönderilecek mesajı yazın:**")

    elif state["step"] == "awaiting_message":
        email = user_states[user_id]["email"]
        user_message = message.text.strip()
        
        # Kullanıcıyı bilgilendir
        processing_msg = await message.reply(f"⏳ `{email}` adresine mesaj gönderiliyor...")
        
        # SendPulse API çağrısı
        success = await send_via_sendpulse(email, user_message)
        
        if success:
            await processing_msg.edit(f"✅ **Başarılı!**\n`{email}` adresine mesaj gönderildi!")
        else:
            await processing_msg.edit("❌ Gönderim başarısız! API hatası oluştu.")
        
        del user_states[user_id]  # İşlem tamamlandı

async def send_via_sendpulse(email, message_text):
    try:
        token_url = "https://api.sendpulse.com/oauth/access_token"
        token_data = {
            "grant_type": "client_credentials",
            "client_id": SENDPULSE_API_ID,
            "client_secret": SENDPULSE_API_SECRET
        }
        token_response = requests.post(token_url, data=token_data)
        
        if token_response.status_code != 200:
            return False

        access_token = token_response.json().get("access_token")
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "email": email,
            "sender": {"name": BOT_NAME, "email": "noreply@viosproject.ai"},
            "subject": f"{BOT_NAME} Mesajı",
            "text": message_text
        }
        
        response = requests.post(
            "https://api.sendpulse.com/smtp/emails",
            headers=headers,
            data=json.dumps(payload)
        
        return response.status_code == 200
        
    except Exception:
        return False
    


if SOURCE != s:
    print("So sad, you have changed source...")
    sys.exit(1)

if __name__ == "__main__":
    print(f""" {BOT_NAME} Başarılı!
    """)
    try:
        Mukesh.start()
        print(f"""JOIN  @MR_SUKKUN
GIVE STAR TO THE REPO 
{BOT_NAME} Başarılı !  
        """)
        idle()
        Mukesh.stop()
        print("Bot stopped. Bye !")
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
