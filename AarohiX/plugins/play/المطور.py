from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config


@app.on_message(
    command(["مطور", "مبرمج السورس", "نور"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://graph.org/file/cb20d47765beed1677341.jpg",
        caption="• Dev Bot ↦ ميوزك العالم \n ━━━━━━━━━━━━ \n • Dev ↦ Cr SoUrce:fox . \n • Bio ↦- 𓏺 Whoever humbles #himself to god will be #exalted 𓏺",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مطورالسورس", url=f"https://t.me/F_o_x_5"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Updates", url=f"https://t.me/F_o_x_5"
                    ),
                ],
            ]
        ),
    )
