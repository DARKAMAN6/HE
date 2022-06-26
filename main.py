import requests
from pytgcalls import idle
from callsmusic import run
from handlers import __version__
from pyrogram import Client as Bot
from config import API_HASH, API_ID, BG_IMAGE, BOT_TOKEN
from helpers.nopm.import User

response = requests.get(BG_IMAGE)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers"),
)


bot.start()
User.start
print(f"[INFO]: Tʀᴏᴊᴀɴs Mᴜsɪᴄ v{__version__} Sᴛᴀʀᴛᴇᴅ !")

run()

idle()
bot.stop
User.stop
print("\n[INFO] - STOPPED VIDEO PLAYER BOT, JOIN @BOT_X_SUPPORT")

