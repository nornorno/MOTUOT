from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from AarohiX import app
from pyrogram.errors import FloodWait
import asyncio

@app.on_message(filters.command(["محح"], prefixes="/"))
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


@app.on_message(filters.command(["تف"], prefixes="/"))
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





@app.on_message(filters.command(["تخ"], prefixes="/"))
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



@app.on_message(filters.command(["سامحني"], prefixes="/"))
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




@app.on_message(filters.command(["خاصم"], prefixes="/"))
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





