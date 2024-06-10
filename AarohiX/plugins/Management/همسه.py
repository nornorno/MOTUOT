import asyncio
import os
import time
import requests
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from config import START_IMG_URL
from AarohiX import app
from random import choice, randint
from pyrogram.types import CallbackQuery

# تعريف 'iddof' كمجموعة
iddof = set()

app = Client("7002439220:AAGHMvkHNKLhhzt_nxwjtk3jdcqJuZF-1wc")

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

@app.on_inline_query()
async def answer(client, inline_query):
    user = inline_query.from_user.username
    title = f"هذه همسه سريه ل {user} هو فقط من يستطيع روئيتها"
    message_text = f"اهذه همسه سريه ل {user} هو فقط من يستطيع روئيتها"
    results = [
        InlineQueryResultArticle(
            title=title,
            input_message_content=InputTextMessageContent(message_text),
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("اظغط للرؤيه", callback_data=f"{user}or{message_text}")
            ]])
        )
    ]
    await client.answer_inline_query(inline_query.id, results)

@app.on_callback_query()
async def callback_query_answer(client, callback_query: CallbackQuery):
    data = callback_query.data
    if data:
        ex = data.split("or")
        if callback_query.from_user.username in ex:
            await callback_query.answer(ex[1], show_alert=True)
        else:
            await callback_query.answer("الرساله ليست لك", show_alert=True)

@app.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply(
        "مرحبا\n"
        "🌐 انا بوت اهمسلي.\n\n"
        "💬 يمكنك استخدامي لارسال رسائل سرية (همسات) في اي مجموعة تشاء.\n"
        "🔮 انا اعمل عن بعد, هذا يعني انك تستيط استخدامي دون الحاجة لوجودي في المجموعة.\n"
        "💌 طريقة استخدامي سهلة جداً, قم بتحويل اي رسالة من الشخص الذي تريد ان تهمس له هنا\n\n"
        "هناك طرق اخرى للاستخدام يمكنك رؤيتها عبر الضغط على طرق اخرى لاستخدام البوت",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("المطور", url="t.me/F_o_x_5")
        ]])
    )




# دالة main التي تُستدعى لتشغيل البوت
async def main():
    async with app:
        await app.start()
        # ... كود البوت
        await app.stop()

# تشغيل حلقة الحدث
if __name__ == "__main__":
    asyncio.run(main())
