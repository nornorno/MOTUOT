import asyncio
import os
import time
import requests
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from config import START_IMG_URL
from AarohiX import app
from random import choice, randint

# تعريف 'iddof' كمجموعة
iddof = set()

@app.on_message(filters.command("همسه") & filters.private)
async def whisper_command(client, message: Message):
    # تحقق إذا كان المستخدم قد قام بالرد على رسالة البوت
    if message.reply_to_message and message.reply_to_message.from_user.is_bot:
        await message.reply("أنت تحاول أن تهمس للبوت؟ يا عبيط 😄")
    # تحقق إذا كان المستخدم يحاول الهمس لنفسه
    elif message.from_user.id == message.chat.id:
        await message.reply("أنت تحاول أن تهمس لنفسك؟ سلامة عقلك يا حب 😅")
    else:
        # إرسال همسة للمستخدم المحدد
        await message.reply("قم بإرسال همسة لي")

@app.on_message(filters.command("همسه") & filters.group)
async def whisper_group(client, message: Message):
    # تحقق إذا كان المستخدم قد قام بالرد على رسالة البوت
    if message.reply_to_message and message.reply_to_message.from_user.is_bot:
        await message.reply("أنت تحاول أن تهمس للبوت؟ يا عبيط 😄", quote=True)
    # تحقق إذا كان المستخدم يحاول الهمس لنفسه
    elif message.from_user.id == message.reply_to_message.from_user.id:
        await message.reply("أنت تحاول أن تهمس لنفسك؟ سلامة عقلك يا حب 😅", quote=True)
    else:
        # إرسال همسة للمستخدم المحدد
        await message.reply("قم بإرسال همسة لي", quote=True)


# دالة main التي تُستدعى لتشغيل البوت
async def main():
    async with app:
        await app.start()
        # ... كود البوت
        await app.stop()

# تشغيل حلقة الحدث
if __name__ == "__main__":
    asyncio.run(main())
