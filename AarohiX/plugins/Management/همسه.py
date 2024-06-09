from pyrogram import Client, filters
from pyrogram.types import Message
from AarohiX import app

# قاعدة البيانات المؤقتة لتخزين الهمسات
whispers = {}

@app.on_message(filters.command("همسه") & filters.group)
async def whisper_command(client: Client, message: Message):
    # تقسيم الرسالة إلى أجزاء
    parts = message.text.split(maxsplit=2)
    if len(parts) == 3:
        target_username = parts[1].lstrip('@')
        whisper_text = parts[2]
        
        # تخزين الهمسة في قاعدة البيانات المؤقتة
        whispers[target_username] = whisper_text
        
        # إخبار المستخدم أن الهمسة تم تخزينها
        await message.reply_text(f"همستك تم تخزينها وستُرسل إلى @{target_username}.")
    else:
        await message.reply_text("الرجاء استخدام الأمر بالصيغة: /همسه @username الرسالة")

@app.on_message(filters.command("استلم_الهمسه") & filters.private)
async def receive_whisper(client: Client, message: Message):
    # التحقق من وجود همسة للمستخدم
    if message.from_user.username in whispers:
        # إرسال الهمسة إلى المستخدم
        await message.reply_text(f"لديك همسة: {whispers[message.from_user.username]}")
        # حذف الهمسة بعد الإرسال
        del whispers[message.from_user.username]
    else:
        await message.reply_text("ليس لديك أي همسات.")

# تذكر إضافة الأمر /استلم_الهمسه إلى البوت لاستلام الهمسات.
