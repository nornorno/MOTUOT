import asyncio
import os
import time
import requests
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from config import START_IMG_URL
from AarohiX import app
from random import choice, randint

# تأكد من تعريف 'iddof' في مكان ما في الكود أو إزالة الشرط إذا لم تحتاجه
iddof = set()  # مثال على تعريف مجموعة iddof

@app.on_message(filters.command(["ايدي", "id", "ا"], prefixes="/"))
async def iddd(client, message):
    if message.chat.id in iddof:
        return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    username = "ليس لديه يوزر" if not usr.username else usr.username
    bio = "لا يوجد نبذة شخصية" if not usr.bio else usr.bio
    chat_title = message.chat.title if message.chat.title else "خاص"
    
    if hasattr(usr, 'photo') and usr.photo:
        photo = await app.download_media(usr.photo.big_file_id)
        caption = f"""🤡 ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{username}\n🎃 ¦𝙸𝙳 :`{usr.id}`\n💌 ¦𝙱𝙸𝙾 :{bio}\n✨ ¦𝙲𝙷𝙰𝚃: {chat_title}\n♻️ ¦𝙸𝙳.𝙶𝚁𝙾𝚄𝙿 :`{message.chat.id}`"""
        await message.reply_photo(
            photo,
            caption=caption,
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
        await message.reply_text(
            f"""🤡 ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{username}\n🎃 ¦𝙸𝙳 :`{usr.id}`\n💌 ¦𝙱𝙸𝙾 :{bio}\n✨ ¦𝙲𝙷𝙰𝚃: {chat_title}\n♻️ ¦𝙸𝙳.𝙶𝚁𝙾𝚄𝙿 :`{message.chat.id}`"""
        )

app.run()
