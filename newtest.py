from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import _asyncio

# Замените 'YOUR_TOKEN' на токен вашего бота
TOKEN = "6861921354:AAGUTDjoalD_HuAgpJiWkpJtlquENqUxeKY"

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Кнопки для примера (опционально)
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет"), KeyboardButton(text="Как дела?")],
    ],
    resize_keyboard=True
)

# Обработка команды /start
@dp.message(Command("start"))
async def start_command_handler(message: Message):
    await message.answer(
        "Привет! Я бот, готовый к работе. Напиши мне что-нибудь или нажми на кнопки ниже.",
        reply_markup=keyboard
    )

# Обработка команды /help
@dp.message(Command("help"))
async def help_command_handler(message: Message):
    await message.answer(
        "Я могу отвечать на текстовые сообщения. Вот что ты можешь сделать:\n"
        "- Используй /start для начала.\n"
        "- Используй /help для помощи.\n"
        "- Напиши что-нибудь, и я отвечу."
    )

# Обработка текстовых сообщений
@dp.message()
async def handle_text_message(message: Message):
    user_message = message.text
    response = f"Ты сказал: {user_message}"
    await message.answer(response)

# Запуск бота
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    _asyncio.run(main())