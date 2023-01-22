import asyncio
import logging
from aiogram import Bot, Dispatcher, types

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="5824861920:AAGQVuMawO58r4h6RyVLWeqOU8Pyor6q10Q")
# Диспетчер
dp = Dispatcher()

@dp.message(commands=["hello"])
async def cmd_hello(message: types.Message):
    await message.answer("Hello!")

@dp.message(commands=['you_here'])
async def cmd_you_here(message: types.Message):
    await message.reply('miss me?')

@dp.message(commands=['name'])
async def cmd_name(message: types.Message):
    await message.answer('Oleg')
    
@dp.message(commands=['you_stupid'])
async def cmd_you_stupid(message: types.Message):
    await message.answer('no you!')

async def main():
    await dp.start_polling(bot)
    dp.message.register(cmd_name, commands=['name'])

if __name__ == "__main__":
    asyncio.run(main())