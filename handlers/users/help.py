from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#help commands
@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer("🔰 Buyruqlar... \n\nBotdan foydalanish uchun - '/start' - tugmasini bosing va sizga kerakli bo'lgan viloyatni tugmalardan tanlang.Shahringi haqidagi ma'lumotni Eslatma eslatish uchun avval'Eslatma ⏰' tugmasini tanlang va o'zingizga kerakli eslatmani belgilang. Va vaqtini tug'ri formatta kiriting.\n\n\n'/about'  - Bot haqida qisqacha ma'lumot.\n'/xabar' - Adminga muroojatlaringizni yozib qoldirishingiz mumkin.")
