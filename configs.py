import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "12380656"))
	API_HASH = os.environ.get("API_HASH","d927c13beaaf5110f25c505b7c071273")
	BOT_TOKEN = os.environ.get("BOT_TOKEN","")
	BOT_USERNAME = os.environ.get("BOT_USERNAME","")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", ""))
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL',"inshorturl.com")
	SHORTLINK_API = os.environ.get('SHORTLINK_API',"3b56a34f0b23cdb3f0da5c7acf68ad5d1dfed0cc")
	BOT_OWNER = int(os.environ.get("BOT_OWNER", ""))
	DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://deepaidb:51354579914@deepaidb.imzonfj.mongodb.net/?retryWrites=true&w=majority&appName=deepaidb")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [Straw Hat File Store](https://t.me/{BOT_USERNAME})
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** [Vps](https://heroku.com)
│
├🔸 **Owner:** [🌼 Anik 🌼](https://t.me/anik_x_probot) 
│
├🔹 **Bot Support:** [Contact](https://t.me/anik_x_suoporttt)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Owner:** [Js](https://t.me/anik_x_probot)

"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **Straw Hat FileStore Bot**.

You Can make this bot your own contact me @anik_x_suoporttt
"""
