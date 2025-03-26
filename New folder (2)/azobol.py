import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "7991412037:AAE3lXzplwNiGoIjnPXyeop3LUoQWCyVBuk"

# Kanal havolalari
CHANNELS = [
    ("1 - kanal", "https://t.me/+8lWDxmPiwJo0Mzli"),
    ("2 - kanal", "https://t.me/hayrotik")
]

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def ask_to_join_channel(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text=name, url=url)] for name, url in CHANNELS
        ]
    )

    await message.answer(
        "❌ Kechirasiz, botimizdan foydalanishdan oldin quyidagi kanallarga a'zo bo‘lishingiz kerak",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
