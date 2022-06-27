import requests
from pytgcalls import.Client,idle
from callsmusic import run
from handlers import __version__
from handler.nopm.import User
from config import API_HASH, API_ID, BG_IMAGE, BOT_TOKEN


response = requests.get(BG_IMAGE)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)


bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers"),
)

Bot.start()
User.start()
print("\n[INFO] - STARTED VIDEO PLAYER BOT, JOIN @BOT_X_SUPPORT !")

idle()
Bot.stop()
User.stop()
print("\n[INFO] - STOPPED VIDEO PLAYER BOT, JOIN @BOT_X_CHANNEL")