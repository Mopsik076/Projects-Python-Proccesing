import asyncio
import logging
from aiogram import Bot, Dispatcher, types
import aiogram.utils.markdown as fmt
import aiohttp
from aiogram.utils.emoji import emojize

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="5824861920:AAGQVuMawO58r4h6RyVLWeqOU8Pyor6q10Q")
# Диспетчер
dp = Dispatcher()

@dp.message(commands=["hello"])
async def cmd_hello(message: types.Message):
    await message.answer(
        fmt.text(
            fmt.text(fmt.hbold('Hello')),
            fmt.text('May name is',fmt.hunderline('Oleg')),
            sep='\n'),
        parse_mode='HTML')

@dp.message(text='hello')
async def hello(message: types.Message):
    await message.answer(fmt.text(fmt.hbold('Hello user')), parse_mode='HTML')

@dp.message_handler(content_types=[types.ContentType.ANIMATION])
async def reply_gif(message: types.Message):
    await message.reply_animation(message.animation.file_id)

@dp.message_handler(content_types=[types.ContentType.STICKER])
async def reply_gif(message: types.Message):
    await message.reply_animation(message.sticker.file_id)

@dp.message_handler(content_types=[types.ContentType.ANY])
async def reply_gif(message: types.Message):
    await message.reply_animation(message.anyany.file_id)

async def main():
    await dp.start_polling(bot)
    dp.message.register(cmd_name, commands=['name'])

if __name__ == "__main__":
    asyncio.run(main())