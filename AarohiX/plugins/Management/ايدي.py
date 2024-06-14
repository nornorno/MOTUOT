import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# تعريف 'iddof' كمجموعة
iddof = set()

# قائمة معرفات مطوري السورس
developers_ids = {6401339012}  # استبدل بمعرفات المطورين الحقيقية

# تعريف البوت
app = Client("my_bot")

@app.on_message(filters.regex(r"^(ايدي|id|ا)$"))
async def maker(client: Client, message: Message):
    if message.chat.id in iddof:
        return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    username = "ليس لديه يوزر" if not usr.username else usr.username
    bio = "لا يوجد نبذة شخصية" if not usr.bio else usr.bio
    chat_title = message.chat.title if message.chat.title else "خاص"
    
    # تحديد رتبة المستخدم
    rank = "مطور السورس" if usr.id in developers_ids else "مستخدم عادي"
    
    # إنشاء الرسالة
    caption = f"""🤡 ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{username}\n🎃 ¦𝙸𝙳 :`{usr.id}`\n💌 ¦𝙱𝙸𝙾 :{bio}\n✨ ¦𝙲𝙷𝙰𝚃: {chat_title}\n♻️ ¦𝙸𝙳.𝙶𝚁𝙾𝚄𝙿 :`{message.chat.id}`\n🎖️ ¦𝚁𝙰𝙽𝙺 :{rank}"""
    
    # إرسال الترحيب إذا كان المستخدم مطور السورس
    if rank == "مطور السورس":
        caption += "\n\n🎉 مرحبًا بك في المجموعة، أنت مطور السورس! 🎉"
    
    if hasattr(usr, 'photo') and usr.photo:
        photo = await app.download_media(usr.photo.big_file_id)
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
        await message.reply_text(caption)

# دالة main التي تُستدعى لتشغيل البوت
async def main():
    async with app:
        await app.start()
        # ... كود البوت
        await app.stop()

# تشغيل حلقة الحدث
if __name__ == "__main__":
    asyncio.run(main())
