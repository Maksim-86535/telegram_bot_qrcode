from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.types import BufferedInputFile
import asyncio
from bot_token import TOKEN
import qrcode
from io import BytesIO

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привіт! 👋\nНадішли мені будь-яке посилання, і я перетворю його на QR-код 📷")

@dp.message()
async def qr_code(message: Message):
    await message.answer("Генерую QR-код...")

    # Генеруємо QR у буфер
    qr = qrcode.make(message.text)
    buffer = BytesIO()
    qr.save(buffer, format='PNG')
    buffer.seek(0)

    # Створюємо BufferedInputFile
    photo = BufferedInputFile(buffer.read(), filename="qrcode.png")

    # Відправляємо фото
    await message.answer_photo(photo=photo, caption="Ось твій Qr-код ✅")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
