from pyrogram import Client, filters
from pyrogram.types import Message

@app.on_message(filters.command('id'))
async def getid(client: Client, message: Message):
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.message_id  # تم تغيير 'id' إلى 'message_id' لتجنب الالتباس
    reply = message.reply_to_message

    text = f"**Message ID:** `{message_id}`\n"
    text += f"**Your ID:** `{your_id}`\n"

    # إزالة الأوامر المكررة لتقسيم النص
    if len(message.command) >= 2:
        user_id = (await client.get_users(message.command[1])).id
        text += f"**User ID:** `{user_id}`\n"

    text += f"**Chat ID:** `{chat.id}`\n\n"

    # تبسيط الشروط باستخدام 'getattr'
    if reply and not getattr(reply, 'is_empty', True):
        text += f"**Replied Message ID:** `{reply.message_id}`\n"
        text += f"**Replied User ID:** `{reply.from_user.id}`\n\n"

        if reply.forward_from_chat:
            text += f"The forwarded channel, {reply.forward_from_chat.title}, has an ID of `{reply.forward_from_chat.id}`\n\n"

        if reply.sender_chat:
            text += f"ID of the replied chat/channel is `{reply.sender_chat.id}`"

    await message.reply_text(
        text,
        disable_web_page_preview=True
    )
