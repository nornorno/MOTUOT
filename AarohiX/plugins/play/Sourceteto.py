import asyncio
import os
import time
import requests
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AarohiX import Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app
from random import choice, randint

#  Define a custom function to get developer info
async def get_developer_info(client: Client, username: str):
    try:
        usr = await client.get_chat(username)
        name = usr.first_name
        photo = await app.download_media(usr.photo.big_file_id)  # Handle potential errors here
        return name, photo, usr
    except Exception as e:
        print(f"Error fetching developer info: {e}")
        return None, None, None

# Command for source info
@app.on_message(command(["سورس", "السورس"]))
async def source_command(client: Client, message: Message):
    await message.reply_video(
        video="https://telegra.ph/file/06ea0dffac061d340b30a.mp4",
        caption=f"""❅─────✧❅✦❅✧─────❅
▰▰▰▰▰▰▰▰▰▰▰▰▰
么- 𓏺We are developers, #not heroes, so don't bark #like dogs

么- 𓏺Whoever humbles #himself to god will be #exalted 𓏺
▰▰▰▰▰▰▰▰▰▰▰▰▰
❅─────✧❅✦❅✧─────❅
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✧❅¹مــطور❅✧", url="https://t.me/F_o_x_5"),
                    InlineKeyboardButton(
                        "✧❅²مــطور❅✧", url="https://t.me/F_o_x_5")
                ],
                [
                    InlineKeyboardButton(
                        "❅✧قـناه السـورس✧❅", url="https://t.me/F_o_x_5")
                ],
                [
                    InlineKeyboardButton(
                        text="اضغط لاضافتي لمجموعتك⚡",
                        url=f"https://t.me/{app.username}?startgroup=true"),
                ],
            ]
        ),
    )

# Command for getting developer info (Fox)
@app.on_message(command(["المطور فوكس"]))
async def developer_fox_command(client: Client, message: Message):
    name, photo, usr = await get_developer_info(client, "F_o_x_5")
    if name and photo and usr:
        await message.reply_photo(photo,
                                 caption=f"معلومات مطور السورس\n\n‍ ¦➻ 𝐍𝐀𝐌𝐄 :{name}\n\n ¦➻ 𝐔𝐒𝐄𝐑 :@{usr.username}\n\n ¦➻ 𝐈𝐃 :{usr.id}\n\n ¦➻ 𝐁𝐎𝐈 :{usr.bio}\n\nســورس ميــوزك العـالم",
                                 reply_markup=InlineKeyboardMarkup(
                                     [
                                         [
                                             InlineKeyboardButton(
                                                 name, url=f"https://t.me/{usr.username}")
                                         ],
                                     ]
                                 ),
                                 )
    else:
        await message.reply("لم يتم العثور على معلومات المطور")

# Consolidated command for getting developer info
@app.on_message(command(["مطور السورس", "الحاكم", "فوكس", "حكم", "مبرمج السورس"]))
async def source_developer_command(client: Client, message: Message):
    name, photo, usr = await get_developer_info(client, "F_o_x_5")
    if name and photo and usr:
        await message.reply_photo(photo,
                                 caption=f"معلومات مبرمج السورس.\n\n¦➻ 𝐍𝐀𝐌𝐄 :{name}\n\n ¦➻ 𝐔𝐒𝐄𝐑 :@{usr.username}\n\n ¦➻ 𝐈𝐃 :{usr.id}\n\n ¦➻ 𝐁𝐎𝐈 :{usr.bio}\n\nسـورس مـيوزك الـعالم",
                                 reply_markup=InlineKeyboardMarkup(
                                     [
                                         [
                                             InlineKeyboardButton(
                                                 name, url=f"https://t.me/{usr.username}")
                                         ],
                                     ]
                                 ),
                                 )
    else:
        await message.reply("لم يتم العثور على معلومات المطور")
