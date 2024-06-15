import asyncio
import os
import time
import requests
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# Assuming 'config' and 'strings' modules are properly defined elsewhere
from config import START_IMG_URL
from strings.filters import command

# Assuming 'AarohiX' is a module with the following imported classes
from AarohiX import Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app

# Random choice and randint are imported from the 'random' module
from random import choice, randint

# Bot developer's username
DEVELOPER_USERNAME = "@G_7_Rr"

@app.on_message(filters.command(["السورس", "ياسورس", "مبرمج السورس", "مطور السورس"], ""))
async def source_command_handler(client: Client, message: Message):
    # Video URL - assuming it's a valid URL
    video_url = "https://graph.org/file/862ce6e007a09bfd9d2a8.mp4"
    
    # Inline keyboard buttons with URLs
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Support group", url="https://t.me/Jo_k_2")],
        [InlineKeyboardButton("CH SOURCE", url="https://t.me/Jok_24")],
        [InlineKeyboardButton("مطور", url="https://t.me/F_o_x_5")],
        [InlineKeyboardButton("مساعد المطور", url="https://t.me/foxmuisic")]
    ])
    
    # Reply with the video and caption
    await message.reply_video(
        video=video_url,
        caption=f"""˛ ❅─────✧❅✦❅✧─────❅
▰▰▰▰▰▰▰▰▰▰▰▰▰
么 𝚂𝙾𝚄𝚁𝙲𝙴: Dev¹: fox
么 𝚂𝙾𝚄𝚁𝙲𝙴: Dev²: fox
么 𝚂𝙾𝚄𝚁𝙲𝙴: Dev³: fox
么 𝚂𝙾𝚄𝚁𝙲𝙴: Dev⁴: 𝐉ok
么 𝚂𝚞𝚙𝚙𝚘𝚛𝚝 𝚌𝚑𝚊𝚗𝚗𝚎¹
么 Support group²
么 مطور
么 مساعد المطورون 
▰▰▰▰▰▰▰▰▰▰▰▰▰
❅─────✧❅✦❅✧─────❅
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 .""",
        reply_markup=keyboard
    )

# Writing by teto @G_7_Rr
