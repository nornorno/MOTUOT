import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message

# تعريف 'iddof' كمجموعة
iddof = set()

app = Client("my_account")

# الأمر 'همسه' في الخاص
@app.on_message(filters.command("همسه") & filters.private)
async def whisper_command(client, message: Message):
    # تحقق من وجود الرسالة المراد إرسالها كهمسة
    if ' ' in message.text:
        # استخراج الرسالة السرية ومعرف المستخدم المستهدف
        _, user_id, secret_message = message.text.split(' ', 2)
        try:
            # تحويل معرف المستخدم إلى عدد صحيح
            user_id = int(user_id)
            # إرسال الهمسة إلى المستخدم المستهدف
            await app.send_message(chat_id=user_id, text=secret_message)
            # إخطار المرسل بأن الهمسة تم إرسالها
            await message.reply_text("تم إرسال الهمسة بنجاح.")
        except ValueError:
            # إذا لم يكن معرف المستخدم عددًا صحيحًا
            await message.reply_text("خطأ: معرف المستخدم يجب أن يكون رقمًا.")
    else:
        # إذا لم تكن الرسالة تحتوي على معرف المستخدم والرسالة السرية
        await message.reply_text("الرجاء إدخال معرف المستخدم والرسالة السرية.")

# الأمر 'همسه' في المجموعات
@app.on_message(filters.command("همسه") & filters.group)
async def whisper_group(client, message: Message):
    # إرسال رسالة إلى المستخدم تفيد بأن الأمر يعمل فقط في الرسائل الخاصة
    await message.reply_text("هذا الأمر يعمل فقط في الرسائل الخاصة.")

# دالة main التي تُستدعى لتشغيل البوت
async def main():
    async with app:
        await app.start()
        # ... كود البوت ...
        await app.stop()

# تشغيل حلقة الحدث
if __name__ == "__main__":
    asyncio.run(main())
