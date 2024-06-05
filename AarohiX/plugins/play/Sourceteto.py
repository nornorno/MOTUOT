import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
from random import  choice, randint

#writing by teto @G_7_Rr          
                
@app.on_message(filters.command(["السورس","ياسورس","مبرمج السورس","مطور السورس"],""))
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/862ce6e007a09bfd9d2a8.mp4",
        caption=f"""˛ ❅─────✧❅✦❅✧─────❅
▰▰▰▰▰▰▰▰▰▰▰▰▰
么 [𝚂𝙾𝚄𝚁𝙲𝙴:Dev¹:fox](https://t.me/F_o_x_5)
么 [𝚂𝙾𝚄𝚁𝙲𝙴:Dev²:fox](https://t.me/F_o_x_5)
么 [𝚂𝙾𝚄𝚁𝙲𝙴:Dev³:fox](https://t.me/F_o_x_5)
么 [𝚂𝙾𝚄𝚁𝙲𝙴:Dev⁴:𝐉ok](https://t.me/Jok_24)
么 [𝚂𝚞𝚙𝚙𝚘𝚛𝚝 𝚌𝚑𝚊𝚗𝚗𝚎¹](https://t.me/fox56789)
么 [Support group²](https://t.me/fox345645)
▰▰▰▰▰▰▰▰▰▰▰▰▰
❅─────✧❅✦❅✧─────❅
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support group", url=f"https://t.me/Jo_k_2"), 
                 ],[
                   InlineKeyboardButton(
                        "CH SOURCE", url=f"https://t.me/@Jok_24"),
                ],

            ]

        ),

    )
    
