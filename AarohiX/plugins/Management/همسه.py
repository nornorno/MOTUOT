from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

app = Client("my_account")

hmses = {}
@app.on_message(filters.regex(r"^همسه$"))
async def maker(client: Client, message: Message):
    user_id = message.reply_to_message.from_user.id
    my_id = message.from_user.id
    bar_id = message.chat.id
    start_link = f"https://t.me/{(await app.get_me()).username}?start=hms{my_id}to{user_id}in{bar_id}"
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("- اضغط لإرسال الهمسه!", url=start_link)]
        ]
    )
    await message.reply_text("\n╢ إضغط لإرسال همسه!\n", reply_markup=reply_markup, reply_to_message_id=message.message_id)

waiting_for_hms = False

@app.on_message(filters.command("start"), group=473)
async def hms_start(client, message):
    if message.text.split(" ", 1)[-1].startswith("hms"):
        global waiting_for_hms, hms_ids
        hms_ids = message.text
        waiting_for_hms = True
        await message.reply_text(
            "-> أرسل الهمسه الآن.\n√",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("إلغاء ❌️", callback_data="hms_cancel")
            ]])
        )

@app.on_message(filters.private & filters.text & ~filters.command("start"), group=921)
async def send_hms(client, message):
    global waiting_for_hms
    if waiting_for_hms:
        to_id = int(hms_ids.split("to")[-1].split("in")[0])
        from_id = int(hms_ids.split("hms")[-1].split("to")[0])
        in_id = int(hms_ids.split("in")[-1])
        
        hmses[str(to_id)] = {"hms": message.text, "bar": in_id}
        
        await message.reply_text("-> تم ارسال الهمسه.\n√")
        
        await app.send_message(
            chat_id=in_id,
            text=f"╖ لديك همسه جديدة!\n╜انت فقط من يستطيع رؤيتها 🔐",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("- اضغط لرؤية الهمسه 👀", callback_data="hms_answer")
            ]])
        )
        
        waiting_for_hms = False

@app.on_callback_query(filters.regex("hms_answer"))
async def display_hms(client, callback: CallbackQuery):
    in_id = callback.message.chat.id
    who_id = callback.from_user.id
    
    if hmses.get(str(who_id)) and hmses[str(who_id)]["bar"] == in_id:
        await callback.answer(hmses[str(who_id)]["hms"], show_alert=True)
    else:
        await callback.answer("الأمر ليس لك", show_alert=True)

@app.on_callback_query(filters.regex("hms_cancel"))
async def cancel_hms(client, callback: CallbackQuery):
    global waiting_for_hms
    waiting_for_hms = False
    
    await callback.message.edit_text("-> تم إلغاء الهمسه!\n√")

@app.on_message(filters.regex(r"^همسه$"))
async def maker(client: Client, message: Message):
    if message.reply_to_message and message.reply_to_message.from_user.is_bot:
        await message.reply("أنت تحاول أن تهمس للبوت؟ يا عبيط 😄")
    elif message.from_user.id == message.chat.id:
        await message.reply("أنت تحاول أن تهمس لنفسك؟ سلامة عقلك يا حب 😅")
    else:
       # متغير لتخزين الصورة المتحركة
    animated_image = 'https://te.legra.ph/file/d0bedd7b2d959f44ae9ab.mp4'  # استبدل بمسار الصورة المتحركة
        pass

# يجب تشغيل البوت في النهاية
app.run()
