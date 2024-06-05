import asyncio
import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

from AarohiX import app
from random import choice, randint

@app.on_message(filters.command(["ايدي"], ""))
async def madison(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    user_id = usr.id
    username = usr.username
    bio = usr.bio
    group = await client.get_chat(message.chat.id)
    
    # تحقق من وجود صورة للمستخدم
    user_photo = None
    async for photo in client.get_chat_photos(message.from_user.id, limit=1):
        user_photo = photo.file_id
    
    # إذا كانت هناك صورة، استخدمها في الرد
    if user_photo:
        await message.reply_photo(
            user_photo,
            caption=f"""╭⦿ᚐɴᴧᴍᴇ : {username}
╰⦿ᚐᴜsᴇꝛ : {name}
╭⦿ᚐɪᴅ :  {user_id}
╰⦿ᚐʙɪᴏ : {bio}
⦿ᚐᴄʜᴧᴛ : {group.title}
╰⦿ᚐᴄʜᴧᴛ ɪᴅ : {group.id}""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            name, url=f"https://t.me/{username}")
                    ],
                ]
            ),
        )
    else:
        # إذا لم يكن هناك صورة، استخدم رسالة نصية
        await message.reply_text(
            f"""╭⦿ᚐɴᴧᴍᴇ : {username}
╰⦿ᚐᴜsᴇꝛ : {name}
╭⦿ᚐɪᴅ :  {user_id}
╰⦿ᚐʙɪᴏ : {bio}
⦿ᚐᴄʜᴧᴛ : {group.title}
╰⦿ᚐᴄʜᴧᴛ ɪᴅ : {group.id}""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            name, url=f"https://t.me/{username}")
                    ],
                ]
            ),
        )
