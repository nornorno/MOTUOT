from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQueryResultArticle, InputTextMessageContent

app = Client("my_bot")

@app.on_message(filters.private & filters.text & ~filters.command)
async def receive_whisper(client, message: Message):
    # ... كود استقبال الرسائل ...

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

app.run()
