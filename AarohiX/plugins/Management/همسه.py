import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQueryResultArticle, InputTextMessageContent

# تعريف 'iddof' كمجموعة
iddof = set()

app = Client("my_account")

@app.on_message(filters.command("همسه") & filters.private)
async def whisper_command(client, message: Message):
    # ... كود الأمر 'همسه' في الخاص ...

@app.on_message(filters.command("همسه") & filters.group)
async def whisper_group(client, message: Message):
    # ... كود الأمر 'همسه' في المجموعات ...

@app.on_inline_query()
async def answer(client, inline_query):
    # ... كود الاستعلامات الداخلية ...

@app.on_callback_query()
async def callback_query_answer(client, callback_query: CallbackQuery):
    # ... كود الاستجابة للاستعلامات الداخلية ...

@app.on_message(filters.command("start"))
async def start(client, message: Message):
    # ... كود الأمر 'start' ...

# دالة main التي تُستدعى لتشغيل البوت
async def main():
    async with app:
        await app.start()
        # ... كود البوت ...
        await app.stop()

# تشغيل حلقة الحدث
if __name__ == "__main__":
    asyncio.run(main())
