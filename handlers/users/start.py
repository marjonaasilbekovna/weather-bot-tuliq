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
        await message.answer(text=f"""Assalomu alaykum hurmatli foydalanuvchi   {full_name} 
🌤  Ob-havo botimizga hush kelibsiz.
                             

Bu bot orqali siz istalgan shahar yoki hududning hozirgi ob-havo ma’lumotlarini bilib olishingiz mumkin. 🌍

🌡 Foydalanish qo‘llanmasini bilish uchun '/help' - tugmasini bosing.
                             

☔ BU bot bilan siz o'z shahringiz ob-havosi haqidagi xabarni eslatma sifatida qabul qilishingiz mumkin.
                             
✨ Botning afzalliklari 

🔹 Qulay va sodda ;                                                 
🔹 Tez va oson ob-havo ma'lumotlarini olish ;
🔹 Ob- havo ma'lumotlarini eslatma tarzida qabul qilish ;
""",reply_markup=menu)
    except:
        await message.answer(text=f"""Assalomu alaykum hurmatli foydalanuvchi   {full_name} 
🌤  Ob-havo botimizga hush kelibsiz.
                             

Bu bot orqali siz istalgan shahar yoki hududning hozirgi ob-havo ma’lumotlarini bilib olishingiz mumkin. 🌍

🌡 Foydalanish qo‘llanmasini bilish uchun '/help' - tugmasini bosing.
                             

☔ BU bot bilan siz o'z shahringiz ob-havosi haqidagi xabarni eslatma sifatida qabul qilishingiz mumkin.
                             
✨ Botning afzalliklari 

🔹 Qulay va sodda ;                                                 
🔹 Tez va oson ob-havo ma'lumotlarini olish ;
🔹 Ob- havo ma'lumotlarini eslatma tarzida qabul qilish ;
""",reply_markup=menu)
