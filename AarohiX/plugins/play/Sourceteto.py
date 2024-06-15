import asyncio
import os
import time
import requests
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# تحميل الإعدادات من ملف الإعدادات
from config import START_IMG_URL
# تحميل الأوامر من ملف الأوامر
from strings.filters import command

# تحميل الوحدات من ملف AarohiX
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

# استيراد الوظائف العشوائية من وحدة random
from random import choice, randint

# كتابة بواسطة teto @G_7_Rr

@app.on_message(filters.command(["السورس", "ياسورس", "مبرمج السورس", "مطور السورس"], ""))
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video="https://telegra.ph/file/06ea0dffac061d340b30a.mp4",
        caption="""˛ ❅─────✧❅✦❅✧─────❅
▰▰▰▰▰▰▰▰▰▰▰▰▰
么 𝚂𝙾𝚄𝚁𝙲𝙴:Dev¹:𝚗𝚘𝚞𝚛
么 𝚂𝙾𝚄𝚁𝙲𝙴:Dev²:𝚊𝚑𝚖𝚎𝚍
▰▰▰▰▰▰▰▰▰▰▰▰▰
❅─────✧❅✦❅✧─────❅
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("❅✧جـروب الدعـم✧❅", url="https://t.me/cr_nox")],
                [InlineKeyboardButton("❅✧قــناه الـسورس❅✧", url="https://t.me/vzo_a")],
                [InlineKeyboardButton("❅✧جـروب الدعـم✧❅", url="https://t.me/F_o_x_5")]
            ]
        ),
    )
