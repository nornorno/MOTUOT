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
async def maker(client: Client, message: Message):
    try:
        if message.reply_to_message:
            reply_name = message.reply_to_message.from_user.first_name
            reply_username = message.reply_to_message.from_user.username
            # فرض أن لديك طريقة لتحديد الجنس هنا
            user_gender = determine_gender(message.from_user)
            reply_user_gender = determine_gender(message.reply_to_message.from_user)

            # تحقق إذا كان الجنس متطابق وقم بإرسال رسالة مخصصة
            if user_gender == reply_user_gender:
                await message.reply_text("مش بجوز انا 🏳️‍🌈🏳️‍🌈🏳️‍🌈🏳️‍🌈🏳️‍🌈شواذ انا ماذون راجل وست😂😂")
            else:
                # الكود الأصلي لإرسال الفيديو
                await message.reply_video(
                    video="https://te.legra.ph/file/cd20a066b3ce6e2db5564.mp4",
                    caption=f"• هذا العريس @{message.from_user.username} \n※ اجوز الوتكها دي دي @{reply_username} \n 👩‍❤️‍👩👨‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨💑👩‍❤️‍💋‍👩👨‍❤️‍💋‍👨وبنهم شهر العثل في شرم الشيخ  علي حسابي انا  ",
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
    except FloodWait as e:
        await asyncio.sleep(e.x)  # X هو عدد الثواني التي يجب الانتظار


@app.on_message(filters.regex(r"^طلاق$"))
async def maker(client: Client, message: Message):
    try:
        if message.reply_to_message:
            reply_name = message.reply_to_message.from_user.first_name
            reply_username = message.reply_to_message.from_user.username
            # هنا يمكنك تحديد جنس المستخدم والشخص الذي يتم الرد عليه
            # على سبيل المثال، يمكنك استخدام قاعدة بيانات خارجية أو الأسماء الأولى
            user_gender = "female"  # يجب تحديد هذا بناءً على معلوماتك
            reply_user_gender = "male"  # يجب تحديد هذا بناءً على معلوماتك

            # تحقق إذا كان المستخدم أنثى والشخص الذي يتم الرد عليه ذكر
            if user_gender == "female" and reply_user_gender == "male":
                await message.reply_text("عفوًا ولكن العصمة في يد 🤭 جوزك 🧔. اذهبي إلى ✈️ محكمة 🏫 وقومي بعمل طلب خلع ✈️.")
            else:
                # الكود الأصلي لإرسال الفيديو
                await message.reply_video(
                    video="https://te.legra.ph/file/9edc54f51694547ba1981.mp4",
                    caption=f"• هذا الرجل @{message.from_user.username} \n※ قام بطلاق مراته وأصبحت الآن الإكس بتاعته @{reply_username} \n بكرة تيجي ندمان يا جميل.",
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
    except FloodWait as e:
        await asyncio.sleep(e.x)  # X هو عدد الثواني التي يجب الانتظار


from pyrogram import Client, filters

@app.on_message(filters.regex(r"^خلع$"))
async def divorce(client: Client, message: Message):
    # الكود الأصلي لإرسال الفيديو
    await message.reply_video(video="https://te.legra.ph/file/11e7cbadb472de6ff3dd3.mp4")

    # كود الخلع
    if message.reply_to_message:
        reply_username = message.reply_to_message.from_user.username
        # تحقق من جنس المستخدم (يجب أن تكون لديك طريقة لتحديد الجنس)
        user_gender = determine_gender(message.from_user)
        if user_gender == "female":
            await message.reply_text(
                f"تم خلع جوزك @{reply_username} 💃💃💃💃💃 بنجاح 🫶 عشان اللي بعنا 🖕 خسر دلعنا."
            )
        elif user_gender == "male":
            await message.reply_text(
                "عفوًا، لكن هذا الأمر مخصص للإناث فقط."
            )
        else:
            await message.reply_text(
                "لم أتمكن من تحديد الجنس بشكل صحيح."
            )
    else:
        await message.reply_text("❗️ لا يوجد رسالة للرد عليها.")





@app.on_message(filters.regex(r"^مراتي$"))
async def maker(client: Client, message: Message):
    user_id = message.from_user.id
    # استعلم عن زوجة المستخدم من قاعدة البيانات
    wife_info = get_marriage_info(user_id)
    if wife_info:
        wife_username, wife_id = wife_info
        await message.reply(f"@{wife_username}، ردّي على جوزك!")
    else:
        await message.reply("أنت لست متزوجًا.")

@app.on_message(filters.command("جوزي") & filters.private)
async def my_husband(client, message):
    user_id = message.from_user.id
    # استعلم عن جوز المستخدمة من قاعدة البيانات
    husband_info = get_marriage_info(user_id)
    if husband_info:
        husband_username, husband_id = husband_info
        await message.reply(f"@{husband_username}، ردّ على مراتك!")
    else:
        await message.reply("أنتِ لستِ متزوجة.")

@app.on_message(filters.regex(r"^زواج$"))
async def maker(client: Client, message: Message):
    user_id = message.from_user.id
    # تحقق من حالة الزواج الحالية
    current_spouse_info = get_marriage_info(user_id)
    if current_spouse_info:
        current_spouse_username, current_spouse_id = current_spouse_info
        # إذا كان المستخدم متزوجًا بالفعل، أرسل تحذيرًا
        await message.reply(f"أنت متزوج بالفعل @{current_spouse_username}. أوعى توافقي!")
        # إرسال منشن للزوج/الزوجة الحالية
        await client.send_message(current_spouse_id, f"@{message.from_user.username} بيحاول يتزوج عليك/عليكِ!")
    else:
        # تنفيذ الكود إذا لم يكن المستخدم متزوجًا
        pass  # استبدل هذا بالكود الفعلي للزواج

# يجب تعريف الدالة determine_gender خارج الدالة maker
def determine_gender(user):
    # كود لتحديد الجنس
    pass
