from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart
from keyboard_buttons.inline.menu import menu


@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text=f"Assalomu alaykum hurmatli foydalanuvchi   -{full_name}-   ob-havo botimizga hush kelibsiz.\nBu bot orqali o'zingiga kerakli bo'lgan ob-havo 🌤️ ma'lumotlarini oson topishingiz mumkin.Sizga kerakli bo'lgan ob-havo ma'lumotini olish uchun kerakli viloyatingizni tugmalardan tanlang.",reply_markup=menu)
    except:
        await message.answer(text=f"Assalomu alaykum hurmatli foydalanuvchi   -{full_name}-   ob-havo botimizga hush kelibsiz.\nBu bot orqali o'zingiga kerakli bo'lgan ob-havo 🌤️ ma'lumotlarini oson topishingiz mumkin.Sizga kerakli bo'lgan ob-havo ma'lumotini olish uchun kerakli viloyatingizni tugmalardan tanlang.",reply_markup=menu)
