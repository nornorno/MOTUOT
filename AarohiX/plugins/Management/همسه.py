from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

app = Client("7107627916:AAExR51c8AKgmxvtpgj00kb2O9S3FwhaAqc")

# متغير لتتبع حالة الرسالة
state = {}

@app.on_message(filters.private & filters.text & ~filters.command)
async def receive_whisper(client, message: Message):
    user_id = message.from_user.id
    if user_id in state and state[user_id] == 'waiting_for_whisper':
        # تخزين الهمسة
        whisper = message.text
        # طلب التأكيد من المستخدم
        confirm_button = InlineKeyboardButton("تأكيد", callback_data="confirm_whisper")
        cancel_button = InlineKeyboardButton("إلغاء", callback_data="cancel_whisper")
        reply_markup = InlineKeyboardMarkup([[confirm_button, cancel_button]])
        await message.reply("هل أنت متأكد من أنك تريد إرسال الهمسة؟", reply_markup=reply_markup)
        # تحديث حالة الرسالة
        state[user_id] = 'waiting_for_confirmation'
    else:
        # إرسال رسالة ترحيبية أو تعليمات
        await message.reply("مرحبًا، يمكنك إرسال همسة بالضغط على الزر أدناه.")

# الدالة التي تتعامل مع تأكيد الهمسة
@app.on_callback_query(filters.regex("confirm_whisper"))
async def confirm_whisper(client, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    if user_id in state and state[user_id] == 'waiting_for_confirmation':
        # ... إرسال الهمسة إلى المستلم ...
        # إعادة تعيين حالة المستخدم
        state[user_id] = None
        await callback_query.message.reply("تم إرسال الهمسة بنجاح.")

# الدالة التي تتعامل مع إلغاء الهمسة
@app.on_callback_query(filters.regex("cancel_whisper"))
async def cancel_whisper(client, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    # إلغاء الهمسة
    state[user_id] = None
    await callback_query.message.reply("تم إلغاء الهمسة.")

# بدء تشغيل البوت
app.run()
