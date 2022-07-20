from os import path

from pyrogram import Client, filters
from pyrogram.types import Message

from time import time
from datetime import datetime
from config import ALIVE_IMG, BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command, other_filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(filters.command(["alive", f"alive@{BOT_USERNAME}"]))
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=f"""**💫 𝗛𝗜 𝗜'𝗠 [{BOT_NAME}](https://t.me/{BOT_USERNAME})**

 **💔 𝗠𝗨𝗦𝗜𝗖 𝗕𝗢𝗧 𝗪𝗢𝗥𝗞𝗜𝗡𝗚 𝗙𝗜𝗡𝗘**

 **👅 𝗠𝗨𝗦𝗜𝗖 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 1.0 𝗕𝗘𝗧𝗔 **

 **👻 𝗢𝗪𝗡𝗘𝗥 [{OWNER_NAME}](https://t.me/{OWNER_NAME})**

 **❣️ 𝗨𝗣𝗧𝗜𝗠𝗘 `{uptime}`**

**💫𝗧𝗛𝗔𝗡𝗞𝗦 𝗙𝗢𝗥 𝗨𝗦𝗜𝗡𝗚 [𝗨𝗟𝗧𝗥𝗢𝗡](https://t.me/ULTRON_X_ROBOT) 𝗕𝗢𝗧**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "这 sᴜᴘᴘᴏʀʏ [🇮🇳]", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "这 ᴜᴘᴅᴀᴛᴇs [🇮🇳]", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
    )
