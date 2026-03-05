import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")

bot= Bot(token=TOKEN)
dp= Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Assalomu Aleykum {message.from_user.first_name}")

async def main():
    print('bot ishladi')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
