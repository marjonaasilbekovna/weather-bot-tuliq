from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("Bu 'Ob-havo' boti bo'lib, bu bot orqali siz o'z viloyatingiz haqida ob-havo ma'lumotini tez va oson topishungiz mumkin bo'ladi.\n\nBu bot 'Sifatedu' o'quv markazi o'quvchilari tomonidan yaratilgan.")

