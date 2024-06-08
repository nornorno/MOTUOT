import asyncio
import os
import time
import requests
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from config import START_IMG_URL
from AarohiX import app
from random import choice, randint

@app.on_message(filters.command(["ايدي", "id", "ا"], prefixes="/")
)
async def iddd(client, message):
    if message.chat.id in iddof:
        return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    if hasattr(usr, 'photo') and usr.photo:
        photo = await app.download_media(usr.photo.big_file_id)
        await message.reply_photo(
            photo,
            caption=f"""🤡 ¦𝙽𝙰𝙼𝙴 :{message.from_user.mention}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{message.from_user.username}\n🎃 ¦𝙸𝙳 :`{message.from_user.id}`\n💌 ¦𝙱𝙸𝙾 :{usr.bio}\n✨ ¦𝙲𝙷𝙰𝚃: {message.chat.title}\n♻️ ¦𝙸𝙳.𝙶𝚁𝙾𝚄𝙿 :`{message.chat.id}`""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            name, url=f"https://t.me/{message.from_user.username}")
                    ],
                ]
            ),
        )
    else:
        await message.reply_text("المستخدم ليس لديه صورة شخصية.")

# تأكد من تعريف 'iddof' في مكان ما في الكود أو إزالة الشرط إذا لم تحتاجه
