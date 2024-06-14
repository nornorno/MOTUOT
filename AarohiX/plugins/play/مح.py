from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from AarohiX import app
from pyrogram.errors import FloodWait
import asyncio

@app.on_message(filters.regex(r"^(مح|محمح|مووح)$"))
async def maker(client: Client, message: Message):
    try:
        # التحقق من وجود رسالة للرد عليها
        if message.reply_to_message:
            reply_name = message.reply_to_message.from_user.first_name
            reply_username = message.reply_to_message.from_user.username
            await message.reply_video(
                video="https://telegra.ph/file/83e7bdf0e2dad83402160.mp4",
                caption=f"• هذا القميل @{message.from_user.username} \n※ بعتلك بوسه يا 😘♥ @{reply_username} \nعيب كده اي المحن ده 😹",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                message.from_user.first_name, url=f"https://t.me/{message.from_user.username}"
                            ),
                            # إضافة زر لاسم المستخدم الذي تم الرد عليه
                            InlineKeyboardButton(
                                reply_name, url=f"https://t.me/{reply_username}"
                            ),
                        ],
                    ]
                )
            )
        else:
            await message.reply_text("❗️ لا يوجد رسالة للرد عليها.")
    except FloodWait as e:
        await asyncio.sleep(e.x)  # X هو عدد الثواني التي يجب الانتظار


@app.on_message(filters.regex(r"^تف$"))
async def maker(client: Client, message: Message):
    try:
        # التحقق من وجود رسالة للرد عليها
        if message.reply_to_message:
            reply_name = message.reply_to_message.from_user.first_name
            reply_username = message.reply_to_message.from_user.username
            await message.reply_video(
                video="https://te.legra.ph/file/e75cf159a6f4c827c399a.mp4",
                caption=f"• هذا القميل @{message.from_user.username} \n※ تف عليك😘♥ @{reply_username} \n 🤷‍♂️اي القرف ددها كان لزم تعصبو 😹",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                message.from_user.first_name, url=f"https://t.me/{message.from_user.username}"
                            ),
                            # إضافة زر لاسم المستخدم الذي تم الرد عليه
                            InlineKeyboardButton(
                                reply_name, url=f"https://t.me/{reply_username}"
                            ),
                        ],
                    ]
                )
            )
        else:
            await message.reply_text("❗️ لا يوجد رسالة للرد عليها.")
    except FloodWait as e:
        await asyncio.sleep(e.x)  # X هو عدد الثواني التي يجب الانتظار





@app.on_message(filters.regex(r"^تخ$"))
async def maker(client: Client, message: Message):
    try:
        # التحقق من وجود رسالة للرد عليها
        if message.reply_to_message:
            reply_name = message.reply_to_message.from_user.first_name
            reply_username = message.reply_to_message.from_user.username
            await message.reply_video(
                video="https://te.legra.ph/file/58e8cb4ab94a0ba409018.mp4",
                caption=f"• هذا القميل @{message.from_user.username} \n※ قتل الشخص دها 😘♥ @{reply_username} \n 💤سبوني عليه اخلص البشريه منو 👻👻 ",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                message.from_user.first_name, url=f"https://t.me/{message.from_user.username}"
                            ),
                            # إضافة زر لاسم المستخدم الذي تم الرد عليه
                            InlineKeyboardButton(
                                reply_name, url=f"https://t.me/{reply_username}"
                            ),
                        ],
                    ]
                )
            )
        else:
            await message.reply_text("❗️ لا يوجد رسالة للرد عليها.")
    except FloodWait as e:
        await asyncio.sleep(e.x)  # X هو عدد الثواني التي يجب الانتظار



@app.on_message(filters.regex(r"^صالح$"))
async def maker(client: Client, message: Message):
    try:
        # التحقق من وجود رسالة للرد عليها
        if message.reply_to_message:
            reply_name = message.reply_to_message.from_user.first_name
            reply_username = message.reply_to_message.from_user.username
            await message.reply_video(
                video="https://te.legra.ph/file/4d8dacc5020cf4533eed3.mp4",
                caption=f"• هذا القميل @{message.from_user.username} \n※ صالح هذه الشخص😘♥ @{reply_username} \n  🫠لقد تم حل جميع الخلافات 👨👨‍⚖️🗣️🗣️بين الطريفن 🫂هما الان زي السمنه علي العثل  ",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                message.from_user.first_name, url=f"https://t.me/{message.from_user.username}"
                            ),
                            # إضافة زر لاسم المستخدم الذي تم الرد عليه
                            InlineKeyboardButton(
                                reply_name, url=f"https://t.me/{reply_username}"
                            ),
                        ],
                    ]
                )
            )
        else:
            await message.reply_text("❗️ لا يوجد رسالة للرد عليها.")
    except FloodWait as e:
        await asyncio.sleep(e.x)  # X هو عدد الثواني التي يجب الانتظار




@app.on_message(filters.regex(r"^خاصم$"))
async def maker(client: Client, message: Message):
    try:
        # التحقق من وجود رسالة للرد عليها
        if message.reply_to_message:
            reply_name = message.reply_to_message.from_user.first_name
            reply_username = message.reply_to_message.from_user.username
            await message.reply_video(
                video="https://te.legra.ph/file/54e1749ffc90fcc758b97.mp4",
                caption=f"• هذا القميل @{message.from_user.username} \n※ خاصم الشخص دها😘♥ @{reply_username} \n 👩‍❤️‍👩👨‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨💑👩‍❤️‍💋‍👩👨‍❤️‍💋‍👨وبنهم الان مصانع حديد عز ⚔️⚔️🛠️  حاولو تصالحو بنهم يا اهل البار الكرام ",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                message.from_user.first_name, url=f"https://t.me/{message.from_user.username}"
                            ),
                            # إضافة زر لاسم المستخدم الذي تم الرد عليه
                            InlineKeyboardButton(
                                reply_name, url=f"https://t.me/{reply_username}"
                            ),
                        ],
                    ]
                )
            )
        else:
            await message.reply_text("❗️ لا يوجد رسالة للرد عليها.")
    except FloodWait as e:
        await asyncio.sleep(e.x)  # X هو عدد الثواني التي يجب الانتظار




@app.on_message(filters.regex(r"^زواج$"))
async def marriage(client: Client, message: Message):
    if message.reply_to_message:
        reply_user = message.reply_to_message.from_user
        reply_name = reply_user.first_name
        reply_username = reply_user.username

        # تحقق إذا كان الشخص المردود عليه بوت
        if reply_user.is_bot:
            await message.reply_text("دها بوت يهبل 😂")
        else:
            # تحقق من الجنس وإجراء الزواج هنا
            # ...
            # الكود الأصلي لإرسال الفيديو
            await message.reply_video(
                video="https://te.legra.ph/file/cd20a066b3ce6e2db5564.mp4",
                caption=f"• هذا العريس @{message.from_user.username} \n※ اجوز الوتكها دي دي @{reply_username} \n 👩‍❤️‍👩👨‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨💑👩‍❤️‍💋‍👩👨‍❤️‍💋‍👨وبنهم شهر العثل في شرم الشيخ علي حسابي انا",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                message.from_user.first_name, url=f"https://t.me/{message.from_user.username}"
                            ),
                            InlineKeyboardButton(
                                reply_name, url=f"https://t.me/{reply_username}"
                            ),
                        ],
                    ]
                )
            )
    else:
        await message.reply_text("يرجى الرد على الشخص الذي تريد الزواج منه.")



@app.on_message(filters.regex(r"^طلاق$"))
async def divorce(client: Client, message: Message):
    # تحقق من وجود رسالة مردود عليها
    if message.reply_to_message:
        user_id = message.from_user.id
        spouse_id = message.reply_to_message.from_user.id

        # تحقق من وجود الزواج في قاعدة البيانات
        if is_married(user_id, spouse_id):
            # إجراء الطلاق
            divorce(user_id, spouse_id)
            await message.reply_text(f"تم الطلاق بنجاح بين {message.from_user.mention} و {message.reply_to_message.from_user.mention}.")
        elif is_bot(spouse_id):
            await message.reply_text("لا يمكنك الزواج من بوت!")
        else:
            await message.reply_text("أنت لست متزوجًا من هذا الشخص أصلاً.")
    else:
        await message.reply_text("يرجى الرد على الشخص الذي تريد الطلاق منه.")

# تحقق من وجود الزواج في قاعدة البيانات
def is_married(user_id, spouse_id):
    # هنا يجب تنفيذ الكود للتحقق من قاعدة البيانات
    # على سبيل المثال:
    # return db.check_marriage(user_id, spouse_id)
    pass

# إجراء الطلاق
def divorce(user_id, spouse_id):
    # هنا يجب تنفيذ الكود لإزالة الزواج من قاعدة البيانات
    # على سبيل المثال:
    # db.remove_marriage(user_id, spouse_id)
    pass

# تحقق إذا كان الشخص بوت
def is_bot(user_id):
    # هنا يجب تنفيذ الكود للتحقق مما إذا كان الشخص بوت
    # على سبيل المثال:
    # return db.check_if_bot(user_id)
    pass

from pyrogram import Client, filters

@app.on_message(filters.regex(r"^خلع$"))
async def khul_divorce(client: Client, message: Message):
    if message.reply_to_message:
        reply_user = message.reply_to_message.from_user
        reply_username = reply_user.username

        # تحقق من جنس المستخدم باستخدام الاسم أو المعرف
        user_gender = determine_gender(message.from_user)
        
        # تأكد من أن الأمر مخصص للإناث فقط
        if user_gender == "female":
            # تحقق من وجود الزواج في قاعدة البيانات
            if is_married(message.from_user.id, reply_user.id):
                # إجراء الخلع
                perform_khul(message.from_user.id, reply_user.id)
                await message.reply_text(
                    f"تم خلع @{reply_username} بنجاح 💃💃💃. الآن أنتِ حرة!"
                )
            else:
                await message.reply_text("أنتِ لستِ متزوجة من هذا الشخص أصلاً.")
        elif user_gender == "male":
            await message.reply_text("عفوًا، لكن هذا الأمر مخصص للإناث فقط.")
        else:
            await message.reply_text("لم أتمكن من تحديد الجنس بشكل صحيح.")
    else:
        await message.reply_text("❗️ لا يوجد رسالة للرد عليها.")

# تحقق من وجود الزواج في قاعدة البيانات
def is_married(user_id, spouse_id):
    # هنا يجب تنفيذ الكود للتحقق من قاعدة البيانات
    pass

# إجراء الخلع
def perform_khul(user_id, spouse_id):
    # هنا يجب تنفيذ الكود لإزالة الزواج من قاعدة البيانات
    pass

# تحديد جنس المستخدم من الاسم أو المعرف
def determine_gender(user):
    # هنا يجب تنفيذ الكود لتحديد الجنس
    # يمكن استخدام الأسماء الأولى أو المعرفات لتقدير الجنس
    pass





@app.on_message(filters.regex(r"^مراتي$"))
async def maker(client: Client, message: Message):
    user_id = message.from_user.id
    print(f"تم استلام الأمر مراتي من المستخدم {user_id}")  # رسالة تصحيح

    # استعلم عن زوجة المستخدم من قاعدة البيانات
    wife_info = get_marriage_info(user_id)
    if wife_info:
        wife_username, wife_id = wife_info
        await message.reply(f"@{wife_username}، ردّي على جوزك!")
    else:
        print("لم يتم العثور على معلومات الزواج في قاعدة البيانات")  # رسالة تصحيح
        await message.reply("أنت لست متزوجًا.")

@app.on_message(filters.command("جوزي") & filters.private)
async def my_husband(client, message):
    user_id = message.from_user.id
    # استعلم عن زوج المستخدمة من قاعدة البيانات
    husband_info = get_marriage_info(user_id)
    if husband_info:
        husband_username, husband_id = husband_info
        await message.reply(f"@{husband_username}، ردّ على مراتك!")
    else:
        await message.reply("أنتِ لستِ متزوجة.")

# يجب تعريف الدالة get_marriage_info خارج الدالة my_husband
def get_marriage_info(user_id):
    # كود لاستعلام عن معلومات الزواج من قاعدة البيانات
    pass


@app.on_message(filters.regex(r"^زواج$"))
async def marriage_contract(client: Client, message: Message):
    user_id = message.from_user.id
    # تحقق من حالة الزواج الحالية للمستخدم
    current_spouse_info = get_marriage_info(user_id)
    if current_spouse_info:
        current_spouse_username, current_spouse_id = current_spouse_info
        # إذا كان المستخدم متزوجًا بالفعل، أرسل تحذيرًا
        await message.reply(f"أنت متزوج بالفعل @{current_spouse_username}. لا يمكنك زواج  آخر!")
        # إرسال تنبيه للزوج/الزوجة الحالية
        await client.send_message(current_spouse_id, f"@{message.from_user.username} يحاول زواج  آخر!")
    else:
        # تنفيذ الكود لعقد القران إذا لم يكن المستخدم متزوجًا
        # هنا يمكنك إضافة الكود الخاص بعقد القران
        pass

# يجب تعريف الدالة get_marriage_info خارج الدالة marriage_contract
def get_marriage_info(user_id):
    # كود لاستعلام عن معلومات الزواج من قاعدة البيانات
    pass

# يجب تعريف الدالة determine_gender خارج الدالة marriage_contract
def determine_gender(user):
    # كود لتحديد الجنس
    pass

