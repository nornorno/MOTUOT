from pyrogram import Client, filters
from pyrogram.types import Message
import requests

# تعريف البوت
app = Client("my_account")

# قائمة المكتومين
muted = []

# الكتم
@app.on_message(filters.command("كتم") & filters.group)
async def mute_member(client: Client, message: Message):
    # التحقق من الرد على رسالة
    if not message.reply_to_message:
        return await message.reply("◍ يجب الرد على رسالة العضو لكتمه \n\n √", reply_to_message_id=message.message_id)

    # الحصول على معلومات العضو
    member_status = await client.get_chat_member(message.chat.id, message.from_user.id)

    # التحقق من رتبة العضو
    if member_status.status not in ["administrator", "creator"]:
        return await message.reply("◍ يجب أن تكون معك رتبة على الأقل لكي تستطيع كتم العضو \n\n √", reply_to_message_id=message.message_id)

    # التحقق من رتبة العضو المراد كتمه
    target_member_status = await client.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    if target_member_status.status in ["creator", "administrator"]:
        return await message.reply("◍ لا يمكن كتم الشخص بسبب رتبته \n\n √", reply_to_message_id=message.message_id)

    # التحقق من وجود العضو في قائمة المكتومين
    if message.reply_to_message.from_user.id in muted:
        return await message.reply("◍ العضو مكتوم بالفعل \n\n √")

    # كتم العضو
    muted.append(message.reply_to_message.from_user.id)
    await message.reply_text(f"◍ المستخدم {message.reply_to_message.from_user.mention}\n◍ تم كتمه من قبل {message.from_user.mention} \n\n √")

# إلغاء الكتم
@app.on_message(filters.command("الغاء كتم") & filters.group)
async def unmute_member(client: Client, message: Message):
    member = member = requests.get(f"https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={message.chat.id}&user_id={message.from_user.id}").json()
    if member["result"]["status"] not in ["creator", "administrator"]: return await message.reply_text(f"يجب ان تكون ادمن علي الاقل لاستخدام هذا الامر\n│ \n : {message.reply_to_message.from_user.mention}\n\n بنجاح ")
        
    if not len(muted): return await message.reply_text("- لا يوجد مكتومين لحذفهم!")
    muted.clear()
    await message.reply_text(f"تم مسح المكتومين \n│ \n : {message.reply_to_message.from_user.mention}\n\n بنجاح ")


# عرض المكتومين
@app.on_message(filters.command("المكتومين"))
async def list_muted_members(client: Client, message: Message):
    if not len(muted): return await message.reply_text("لا يوجد مكتومين \n\n √")
    names = "\n".join(["- " + (await app.get_chat(id)).first_name for id in muted])
    caption = f"- المكتومين: \n\n{names}"
    await message.reply(caption, reply_to_message_id=message.message_id)


# مسح المكتومين
@app.on_message(filters.command("مسح المكتومين"))
async def clear_muted_members(client: Client, message: Message):
    member = member = requests.get(f"https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={message.chat.id}&user_id={message.from_user.id}").json()
    if member["result"]["status"] not in ["creator", "administrator"]: return await message.reply_text(f"يجب ان تكون ادمن علي الاقل لاستخدام هذا الامر\n│ \n : {message.reply_to_message.from_user.mention}\n\n بنجاح ")
        
    if not len(muted): return await message.reply_text("- لا يوجد مكتومين لحذفهم!")
    muted.clear()
    await message.reply_text(f"تم مسح المكتومين \n│ \n : {message.reply_to_message.from_user.mention}\n\n بنجاح ")


# حذف رسائل المكتومين
@app.on_message(filters.text & filters.group, group=928)
async def delete_muted_messages(client: Client, message: Message):
    # التحقق إذا كان المرسل مكتومًا
    if message.from_user.id in muted:
        # حذف الرسالة
        await message.delete()


# حظر عضو
@app.on_message(filters.command("حظر") & filters.group)
async def ban_member(client: Client, message: Message):
      if message.reply_to_message:
        member = requests.get(f"https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={message.chat.id}&user_id={message.from_user.id}").json()
        memberB = requests.get(f"https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={message.chat.id}&user_id={message.reply_to_message.from_user.id}").json()
        if member["result"]["status"] == "administrator":
            if memberB["result"]["status"] in ["creator", "administrator"]:return await message.reply("- لا يمكنك طرد مشرف او مالك", reply_to_message_id=message.message_id)
            try:await app.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            except: return await message.reply_text(f"ليس لدي صلاحيات لطرد هذا العضو\n│ \n : {message.reply_to_message.from_user.mention}\n\n بنجاح ")

            await message.reply_text(f"تم طرد العضو \n : {message.reply_to_message.from_user.mention}\n\n بنجاح ")

            return
        elif member["result"]["status"] == "creator":
            try:await app.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            except: return await message.reply_text(f"ليس لدي صلاحيات لطرد العضو\n: {message.reply_to_message.from_user.mention}\n\n  بنجاح")

            await message.reply("- تم طرد العضو بنجاح!", reply_to_message_id=message.message_id)
            return
        else: await message.reply("- يجب ان تكون ادمن على الاقل لإستخدام هذا الامر.", reply_to_message_id=message.message_id)


# إلغاء حظر عضو
@app.on_message(filters.command("الغاء حظر") & filters.group)
async def unban_member(client: Client, message: Message):
    if message.reply_to_message:
        member = requests.get(f"https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={message.chat.id}&user_id={message.from_user.id}").json()
        if member["result"]["status"] == "administrator":
            if message.reply_to_message.from_user.id not in ban: return await message.reply("- هذا المستخدم غير محظور!")
            ban.remove(message.reply_to_message.from_user.id)
            await message.reply_text(f"تم الغاء حظر العضو\n│ \n : {message.reply_to_message.from_user.mention}\n\n بنجاح ")

            return
        elif member["result"]["status"] == "creator":
            if message.reply_to_message.from_user.id not in ban: return await message.reply("- هذا المستخدم غير محظور!")
            ban.remove(message.reply_to_message.from_user.id)
            await message.reply_text(f"تم الغاء  حظر\n│ \n : {message.reply_to_message.from_user.mention}\n\n بنجاح ")

            return
        else: await message.reply("- يجب ان تكون ادمن على الاقل لإستخدام هذا الامر.", reply_to_message_id=message.message_id)
         
