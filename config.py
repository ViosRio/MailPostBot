import os
API_ID = int(os.environ.get("API_ID", "20658336"))
API_HASH = os.environ.get("API_HASH", "cedfb5fb4ffee7ecc746b28afc7925e3") 
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

# TWİLİO SMS APİ
TWILIO_SID = "AC1efa1740d412dfd8a12328bde295c88e"  # Örnek SID
TWILIO_TOKEN = ""  # Örnek Token
TWILIO_SERVICE_SID = " "  # Messaging Service SID

# EMAİL GÖNDERİM SEND PULSE
SMTP_SERVER = "smtp-pulse.com"
SMTP_PORT = 2525  # 465 (SSL) veya 587 (TLS) de kullanabilirsin
SMTP_EMAIL = ""
SMTP_PASSWORD = "XRD"  # Gerçek şifreni koy!

BOT_USERNAME = os.environ.get("BOT_USERNAME" , "HostRioBot") 
SUDO=os.environ.get("SUDO","5910057231")
BOT_NAME = os.environ.get("BOT_NAME", "Send Bot")
START_IMG = os.environ.get("START_IMG","https://telegra.ph/file/4746e2442a584f37dcc86.jpg")
STKR = os.environ.get("STKR","CAACAgEAAx0CRjAUHgABAsULZASkFZUsTQTw2k-FvC2SBJnd-vAAAokCAALW9iBFzemsQBDIqWkuBA")
BANNED_USERS=os.environ.get("BANNED_USERS",None)
UPDATE_CHNL = os.environ.get("UPDATE_CHNL", "ViosTeam")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "ViosCeo")
SUDO=os.environ.get("SUDO","5910057231")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP","Bot4Chan")

