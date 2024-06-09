from pyrogram import Client, filters
from pyrogram.types import Message
app = Client("my_account")

# تعريف الرتب
RANKS = {
    "member": "أنت عضو حقير 🏃‍♂️🧎‍♀️🧎‍♀️ شد حيلك عشان تاخد رتبة",
    "admin": "أنت أدمن 🕴️😇🥰 مجتهد",
    "creator": "أنت المنشئ يا عمري",
    "developer": "أنت المطور يقلبو اللي يجي جمبك هنفخ أمو 🫢",
    "source_developer": "أنا بابا حبيبي قلبي فوكس 🫠"
}

@app.on_message(filters.command("رتبتي"))
async def check_rank(client: Client, message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    # تحقق من رتبة المستخدم في الدردشة
    member = await app.get_chat_member(chat_id, user_id)
    rank = ""

    # تحديد الرتبة بناءً على صلاحيات المستخدم
    if member.status == "member":
        rank = RANKS["member"]
    elif member.status == "administrator":
        rank = RANKS["admin"]
    elif member.status == "creator":
        rank = RANKS["creator"]
    # تحقق إذا كان المستخدم هو مطور البوت (يمكنك تعديل هذا بناءً على معاييرك)
    elif user_id == YOUR_DEVELOPER_ID:
        rank = RANKS["developer"]
    # تحقق إذا كان المستخدم هو مطور السورس (يمكنك تعديل هذا بناءً على معاييرك)
    elif user_id == YOUR_SOURCE_DEVELOPER_ID:
        rank = RANKS["@F_o_x_5"]

    # إرسال الرسالة إلى المستخدم
    await message.reply_text(rank)

# يجب تعريف 'YOUR_DEVELOPER_ID' و 'YOUR_SOURCE_DEVELOPER_ID' بأرقام المعرفات الخاصة بك
