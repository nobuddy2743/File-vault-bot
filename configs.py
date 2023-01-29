# (c) @PredatorHackerzZ || @TeleRoidGroup

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", ""))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", ""))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸🤖 **My Name:** [𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐞 𝐁𝐨𝐭](https://t.me/{BOT_USERNAME})
│
├🔸📝 **Language:** [𝐏𝐲𝐭𝐡𝐨𝐧𝟑](https://www.python.org)
│
├🔹📚 **Library:** [𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦](https://docs.pyrogram.org)
│
├🔹📡 **Hosted On:** 𝐕𝐏𝐒 
│
├🔸🔔 **Bot Updates:** [𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/tgnvs)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""<b>Donation</b>
	
<b>Thanks for showing interest in donation
Donate Us To Keep Alive
Continously Alive

You Can Send Any Amount
Donate Only One Rupee
Of 10₹,20₹,30₹,50₹,100₹ 😁

💸Payment Methods:
Only UPI
UPI:-</b> tgnvs@airtel

Click Here 👇👇👇
-<b> <a href=https://upier.vercel.app/pay/tgnvs@airtel>Donation Link</a></b>
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\n

This is a Permanent FileStore Bot. 
📢 Send Me any Media or File.I can Work In Channel too Add Me to Channel with Edit Permission.
"""
