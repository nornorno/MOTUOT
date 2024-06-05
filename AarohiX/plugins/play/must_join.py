from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AarohiX import app

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not "https://t.me/Jo_k_5":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("Jo_k_5", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/Jo_k_5".isalpha():
                link = "https://t.me/Jo_k_5"
            else:
                chat_info = await bot.get_chat("WX_PM")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"**⭓ᴍᴜꜱɪᴄ✘ᴛᴇᴛσ♪\n╮⦿ عزيزي : {msg.from_user.mention}\n╯⦿ عليك الاشتراك فالقناه اولا.**",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("ᴍᴜꜱɪᴄ ᴜᴘᴅᴀᴛᴇᴅ", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOIN chat @Jo_k_5 !")
      
