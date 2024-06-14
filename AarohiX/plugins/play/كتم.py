from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions

# تعريف البوت
app = Client("my_account")

# قوائم الإدارة
muted = set()       # المكتومين
restricted = set()  # المقيدين
banned = set()      # المحظورين

# الكتم
@app.on_message(filters.regex(r"^كتم$"))
async def maker(client: Client, message: Message):
    # التحقق من صلاحيات المستخدم الحالي
    member_status = await client.get_chat_member(message.chat.id, message.from_user.id)
    if member_status.status not in ["administrator", "creator"]:
        return await message.reply("◍ يجب أن تكون مشرفًا لاستخدام هذا الأمر.", reply_to_message_id=message.message_id)
    
    # التحقق من الرد على رسالة
    if not message.reply_to_message:
        return await message.reply("◍ يجب الرد على رسالة العضو لكتمه.", reply_to_message_id=message.message_id)
    
    # كتم العضو
    muted.add(message.reply_to_message.from_user.id)
    await message.reply(f"◍ تم كتم المستخدم {message.reply_to_message.from_user.mention} بنجاح.")

# إلغاء الكتم
@app.on_message(filters.regex(r"^الغاء كتم$"))
async def maker(client: Client, message: Message):
# التحقق من صلاحيات المستخدم الحالي
    member_status = await client.get_chat_member(message.chat.id, message.from_user.id)
    if member_status.status not in ["administrator", "creator"]:
        return await message.reply("◍ يجب أن تكون مشرفًا لاستخدام هذا الأمر.", reply_to_message_id=message.message_id)
    
    # إلغاء كتم العضو
    if message.reply_to_message.from_user.id in muted:
        muted.remove(message.reply_to_message.from_user.id)
        await message.reply(f"◍ تم إلغاء كتم المستخدم {message.reply_to_message.from_user.mention} بنجاح.")
    else:
        await message.reply("◍ العضو ليس مكتومًا.")


# مسح المكتومين
@app.on_message(filters.regex(r"^مسح المكتومين$"))
async def maker(client: Client, message: Message):
    # التحقق من صلاحيات المستخدم الحالي
    member_status = await client.get_chat_member(message.chat.id, message.from_user.id)
    if member_status.status not in ["administrator", "creator"]:
        return await message.reply("◍ يجب أن تكون مشرفًا لاستخدام هذا الأمر.", reply_to_message_id=message.message_id)
    
    # مسح قائمة المكتومين
    muted.clear()
    await message.reply("◍ تم مسح جميع المكتومين بنجاح.")


# كود عرض المكتومين
@app.on_message(filters.regex(r"^المكتومين$"))
async def maker(client: Client, message: Message):
    # عرض قائمة المكتومين
    if not muted:
        await message.reply("◍ لا يوجد مكتومين في الوقت الحالي.")
    else:
        muted_list = "\n".join([f"- {await app.get_users(user_id).mention}" for user_id in muted])
        await message.reply(f"قائمة المكتومين:\n{muted_list}")



# كود تقييد العضو
@app.on_message(filters.regex(r"^تقيد $"))
async def maker(client: Client, message: Message):
    # التحقق من صلاحيات المستخدم الحالي
    member_status = await client.get_chat_member(message.chat.id, message.from_user.id)
    if member_status.status not in ["administrator", "creator"]:
        return await message.reply("◍ يجب أن تكون مشرفًا لاستخدام هذا الأمر.", reply_to_message_id=message.message_id)
    
    # التحقق من الرد على رسالة
    if not message.reply_to_message:
        return await message.reply("◍ يجب الرد على رسالة العضو لتقييده.", reply_to_message_id=message.message_id)
    
    # تقييد العضو
    restricted.add(message.reply_to_message.from_user.id)
    await message.reply(f"◍ تم تقييد المستخدم {message.reply_to_message.from_user.mention} بنجاح.")

# كود إلغاء تقييد العضو
@app.on_message(filters.regex(r"^الغاء تقيد $"))
async def maker(client: Client, message: Message):
    # التحقق من صلاحيات المستخدم الحالي
    member_status = await client.get_chat_member(message.chat.id, message.from_user.id)
    if member_status.status not in ["administrator", "creator"]:
        return await message.reply("◍ يجب أن تكون مشرفًا لاستخدام هذا الأمر.", reply_to_message_id=message.message_id)
    
    # إلغاء تقييد العضو
    if message.reply_to_message.from_user.id in restricted:
        restricted.remove(message.reply_to_message.from_user.id)
        await message.reply(f"◍ تم إلغاء تقييد المستخدم {message.reply_to_message.from_user.mention} بنجاح.")
    else:
        await message.reply("◍ العضو ليس مقيدًا.")

# كود مسح المقيدين
@app.on_message(filters.regex(r"^مسح المقيدين $"))
async def maker(client: Client, message: Message):
    # التحقق من صلاحيات المستخدم الحالي
    member_status = await client.get_chat_member(message.chat.id, message.from_user.id)
    if member_status.status not in ["administrator", "creator"]:
        return await message.reply("◍ يجب أن تكون مشرفًا لاستخدام هذا الأمر.", reply_to_message_id=message.message_id)
    
    # مسح قائمة المقيدين
    restricted.clear()
    await message.reply("◍ تم مسح جميع المقيدين بنجاح.")

# كود عرض المقيدين
@app.on_message(filters.regex(r"^المقيدين$"))
async def maker(client: Client, message: Message):
    # عرض قائمة المقيدين
    if not restricted:
        await message.reply("◍ لا يوجد مقيدين في الوقت الحالي.")
    else:
        restricted_list = "\n".join([f"- {await app.get_users(user_id).mention}" for user_id in restricted])
        await message.reply(f"قائمة المقيدين:\n{restricted_list}")

# كود حظر العضو
@app.on_message(filters.regex(r"^حظر$"))
async def maker(client: Client, message: Message):
    # التحقق من صلاحيات المستخدم الحالي
    member_status = await client.get_chat_member(message.chat.id, message.from_user.id)
    if member_status.status not in ["administrator", "creator"]:
        return await message.reply("◍ يجب أن تكون مشرفًا لاستخدام هذا الأمر.", reply_to_message_id=message.message_id)
    
    # التحقق من الرد على رسالة
    if not message.reply_to_message:
        return await message.reply("◍ يجب الرد على رسالة العضو لحظره.", reply_to_message_id=message.message_id)
    
    # حظر العضو
    banned.add(message.reply_to_message.from_user.id)
    await client.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await message.reply(f"◍ تم حظر المستخدم {message.reply_to_message.from_user.mention} بنجاح.")

# كود إلغاء حظر العضو
@app.on_message(filters.regex(r"^الغاء حظر$"))
async def maker(client: Client, message: Message):
    # التحقق من صلاحيات المستخدم الحالي
    member_status = await client.get_chat_member(message.chat.id, message.from_user.id)
    if member_status.status not in ["administrator", "creator"]:
        return await message.reply("◍ يجب أن تكون مشرفًا لاستخدام هذا الأمر.", reply_to_message_id=message.message_id)
    
    # إلغاء حظر العضو
    if message.reply_to_message.from_user.id in banned:
        banned.remove(message.reply_to_message.from_user.id)
        await client.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        await message.reply(f"◍ تم إلغاء حظر المستخدم {message.reply_to_message.from_user.mention} بنجاح.")
    else:
        await message.reply("◍ العضو ليس محظورًا.")

# كود مسح المحظورين
@app.on_message(filters.regex(r"^مسح المحظورين $"))
async def maker(client: Client, message: Message)::
    # التحقق من صلاحيات المستخدم الحالي
    member_status = await client.get_chat_member(message.chat.id, message.from_user.id)
    if member_status.status not in ["administrator", "creator"]:
        return await message.reply("◍ يجب أن تكون مشرفًا لاستخدام هذا الأمر.", reply_to_message_id=message.message_id)
    
    # مسح قائمة المحظورين
    banned.clear()
    await message.reply("◍ تم مسح جميع المحظورين بنجاح.")

# كود عرض المحظورين
@app.on_message(filters.regex(r"^ المحظورين$"))
async def maker(client: Client, message: Message):
    # عرض قائمة المحظورين
    if not banned:
        await message.reply("◍ لا يوجد محظورين في الوقت الحالي.")
    else:
        banned_list = "\n".join([f"- {await app.get_users(user_id).mention}" for user_id in banned])
        await message.reply(f"قائمة المحظورين:\n{banned_list}")
        
@app.on_message(filters.regex(r"^ حذف$"))
async def maker(client: Client, message: Message):
    # التحقق من وجود رسالة مردود عليها
    if message.reply_to_message:
        # حذف الرسالة المردود عليها
        await client.delete_messages(
            chat_id=message.chat.id,
            message_ids=[message.reply_to_message.message_id]
        )

@app.on_message(filters.regex(r"^ مسح$"))
async def maker(client: Client, message: Message):
    # تحقق من وجود العداد في الأمر
    if len(message.command) > 1:
        # حاول تحويل العداد إلى رقم
        try:
            count = int(message.command[1])
        except ValueError:
            await message.reply_text("يرجى تحديد عدد صحيح للرسائل التي تريد مسحها.")
            return

        # جمع معرفات الرسائل للحذف
        message_ids = []
        async for msg in client.iter_history(message.chat.id, limit=count):
            message_ids.append(msg.message_id)

        # حذف الرسائل
        await client.delete_messages(chat_id=message.chat.id, message_ids=message_ids)
        await message.reply_text(f"تم مسح {count} رسائل.")
    else:
        await message.reply_text("يرجى تحديد عدد الرسائل التي تريد مسحها بعد الأمر '/مسح'.")

# جلب قائمة المشرفين
@app.on_message(filters.regex(r"^ المشرفين$"))
async def maker(client: Client, message: Message):
        # جلب قائمة المشرفين في المجموعة
    admins = await client.get_chat_members(message.chat.id, filter="administrators")
    # إنشاء رسالة تحتوي على أسماء المشرفين
    admin_names = "\n".join([admin.user.first_name for admin in admins if not admin.user.is_bot])
    await message.reply(f"قائمة المشرفين:\n{admin_names}")
# جلب قائمة البوتات
@app.on_message(filters.command("البوتات") & filters.group)
async def list_bots(client: Client, message: Message):
 # جلب قائمة البوتات في المجموعة
    bots = await client.get_chat_members(message.chat.id, filter="bots")
    # إنشاء رسالة تحتوي على أسماء البوتات
    bot_names = "\n".join([bot.user.first_name for bot in bots])
    await message.reply(f"قائمة البوتات:\n{bot_names}")
# حذف البوتات
@app.on_message(filters.regex(r"^ طرد البوتات$"))
async def maker(client: Client, message: Message):
    # جلب قائمة البوتات في المجموعة
    bots = await client.get_chat_members(message.chat.id, filter="bots")
    # طرد كل بوت من المجموعة
    for bot in bots:
        await client.kick_chat_member(message.chat.id, bot.user.id)
    await message.reply("تم طرد جميع البوتات من المجموعة.")
