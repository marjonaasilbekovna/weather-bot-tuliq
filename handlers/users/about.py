from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("""
Bizni tanlaganingizdan hursandmiz.
                         
✨ Ob-havo Botiga Xush Kelibsiz! ✨
🌦 Bu bot haqida:
                         
🔹 Sizning viloyatingiz va atrof-muhit haqidagi ob-havo ma’lumotlarini tez va oson yetkazib beruvchi ;
🔹 Zamonaviy va ishonchli xizmat ;
                         

💡 Ushbu bot  'Sifatedu'  o'quv markazi o'quvchilari tomonidan yaratilgan bo'lib sizga eng soʻnggi ob-havo yangiliklarini taqdim etish maqsadida ishlab chiqilgan.
                         

🔧 **Qanday ishlaydi:
                         
Faqat shahar nomini tugmalardan tanlng va biz darhol sizga ob-havo prognozini yuboramiz. 
Ob-havo ma'lumtlarini...
                         
- bir kun 
- uch kun 
- besh kun
- bir hafta

...shaklida eslatma tarzida olishingiz mumkin.                                                                                            
                         
😊  Biz bilan qoling va ob-havo haqidagi yangiliklardan doimo xabardor bo'ling!
                        """)
