from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime, timedelta
from AarohiX import app

@app.on_message(filters.command("today"))
async def send_today_date(client: Client, message: Message):
    # الحصول على التاريخ الحالي
    today = datetime.now()
    
    # حساب يوم الأسبوع
    day_of_week = today.strftime("%A")
    
    # حساب الأسبوع من السنة
    week_number = today.isocalendar()[1]
    
    # إنشاء الرسالة
    response = f"التاريخ اليوم هو: {today.strftime('%Y-%m-%d')}\n"
    response += f"يوم الأسبوع: {day_of_week}\n"
    response += f"رقم الأسبوع من السنة: {week_number}"
    
    # إرسال الرسالة
    await message.reply_text(response)
