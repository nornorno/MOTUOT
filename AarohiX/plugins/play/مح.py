from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
# من الأفضل إزالة الاستيراد غير المستخدم لتجنب الخطأ
# from strings.filters import command
from AarohiX import app
import config
from pyrogram.errors import FloodWait

@app.on_message(filters.command(["محح"], prefixes="/"))
async def maker(client: Client, message: Message):
    try:
        await message.reply_video(
            video="https://telegra.ph/file/83e7bdf0e2dad83402160.mp4",
            caption=f"• هذا القميل @{message.from_user.username} \n※ بعتلك بوسه يا 😘♥ @ \nعيب كده اي المحن ده 😹",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            message.from_user.first_name, url=f"https://t.me/{message.from_user.username}"
                        ),
                    ],
                    # يجب إزالة الزر الثاني لأنه يحتوي على خطأ في التنسيق
                ]
            )
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)  # X هو عدد الثواني التي يجب الانتظار
