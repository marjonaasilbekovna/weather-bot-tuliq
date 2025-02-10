import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from weather import weather
from keyboard_buttons.inline.menu import menu, menu_country, sozlama, eslatish
from loader import dp,bot,db,ADMINS,TOKEN
from menucommands.set_bot_commands  import set_default_commands
from datetime import datetime, timedelta
import time


@dp.callback_query(lambda callback_query: callback_query.data in menu_country.keys())
async def weather_info(callback_query: CallbackQuery, state: FSMContext):
    selected_city = callback_query.data
    user_id = callback_query.from_user.id

    # Shaharni state-ga saqlaymiz
    await state.update_data(selected_city=selected_city)


    # Ob-havo ma'lumotlarini olish
    ob_havo_info = weather(selected_city)
    
    await callback_query.message.answer(f"{menu_country[selected_city]} shahridagi ob-havo ma'lumotlari:\n\n{ob_havo_info}", reply_markup=sozlama)

@dp.callback_query(F.data=="eslatma")
async def change_code(callback_query:CallbackQuery):
    await callback_query.message.answer("🤖 Ob-havo ma'lumotlarini eslatib turish uchun eslatma turini tugmalardan tanlang. !", reply_markup=eslatish)


#  bugungi ob havoni eslatish
@dp.callback_query(F.data == "bir")
async def hozir_eslatma(callback_query: CallbackQuery):
    await callback_query.message.answer(
        "⚙️ Sizga ob-havo ma'lumotlarini eslatib turishimiz uchun vaqtni to'g'ri formatda kiriting !\nmasalan: 20:00:00"
    )

@dp.message(lambda message: message.text)
async def timer(message: Message, state: FSMContext):
    eslatma_vaqti = message.text  
    user_data = await state.get_data()  
    selected_city = user_data.get("selected_city", None)

    if not selected_city:
        await message.answer("Shahar tanlanmagan. Iltimos, oldin shaharni tanlang.")
        return

    await message.answer("Eslatma saqlandi! Eslatma vaqti kelganda sizga ob-havo ma'lumotlarini yuboramiz.")

    # Vaqtni tekshirib, eslatmani yuborish
    while True:
        if time.strftime('%H:%M:%S') == eslatma_vaqti:
            ob_havo_info = weather(selected_city)  
            await message.answer(f"Eslatma vaqti yetdi! ⏰ {menu_country[selected_city]} shahridagi ob-havo ma'lumotlari:\n\n{ob_havo_info}", reply_markup=sozlama)
            break
        else:
            continue


# 3 kunlik ob-havo eslatmasi kodi
@dp.callback_query(F.data == "uch")
async def eslatma_3kun(callback_query: CallbackQuery):
    await callback_query.message.answer(
        "⚙️ Sizga 3 kun davomida ob-havo ma'lumotlarini eslatib turishimiz uchun vaqtni to'g'ri formatda kiriting\nmasalan: 20:00:00"
    )

@dp.message(lambda message: message.text)
async def timer_3kun(message: Message, state: FSMContext):
    eslatma_vaqti = message.text 
    user_data = await state.get_data()  
    selected_city = user_data.get("selected_city", None)

    if not selected_city:
        await message.answer("Shahar tanlanmagan. Iltimos, oldin shaharni tanlang.")
        return

    await message.answer("Uch kunlik eslatma saqlandi! \nBiz sizga shahringiz haqidagi ob-havo malumotlarini uch kun davomida siz kiritgan vaqtda yuboramiz.")

    # 3 kun davomida har kuni belgilangan vaqtda ob-havo eslatmasini yuborish
    for kun in range(3):
        while True:
            if time.strftime('%H:%M:%S') == eslatma_vaqti:
                ob_havo_info = weather(selected_city) 
                await message.answer(
                    f"{kun + 1}-kun eslatmasi ⏰ {menu_country[selected_city]} shahridagi ob-havo ma'lumotlari:\n\n{ob_havo_info}", 
                    reply_markup=sozlama
                )
            else:
                continue
    



# 5 kunlik ob-havo eslatmasi kodi
@dp.callback_query(F.data == "besh")
async def eslatma_5kun(callback_query: CallbackQuery):
    await callback_query.message.answer(
        "⚙️ Sizga 5 kun davomida ob-havo ma'lumotlarini eslatib turishimiz uchun vaqtni to'g'ri formatda kiriting\nmasalan: 20:00:00"
    )

@dp.message(lambda message: message.text)
async def timer_5kun(message: Message, state: FSMContext):
    eslatma_vaqti = message.text 
    user_data = await state.get_data()  
    selected_city = user_data.get("selected_city", None)

    if not selected_city:
        await message.answer("Shahar tanlanmagan. Iltimos, oldin shaharni tanlang.")
        return

    await message.answer("Besh kunlik eslatma saqlandi! \nBiz sizga shahringiz haqidagi ob-havo malumotlarini besh kun davomida siz kiritgan vaqtda yuboramiz.")

    # 5 kun davomida har kuni belgilangan vaqtda ob-havo eslatmasini yuborish
    for kun in range(5):
        while True:
            if time.strftime('%H:%M:%S') == eslatma_vaqti:
                ob_havo_info = weather(selected_city) 
                await message.answer(
                    f"{kun + 1}-kun eslatmasi ⏰ {menu_country[selected_city]} shahridagi ob-havo ma'lumotlari:\n\n{ob_havo_info}", 
                    reply_markup=sozlama
                )
                break
            else:
                continue


# Bir haftalik ob-havo eslatmasi uchun vaqtni so'rash
@dp.callback_query(F.data == "hafta")
async def eslatma_hafta(callback_query: CallbackQuery):
    await callback_query.message.answer(
        "⚙️ Sizga 7 kun davomida ob-havo ma'lumotlarini eslatib turishimiz uchun vaqtni to'g'ri formatda kiriting\nmasalan: 20:00:00"
    )

@dp.message(lambda message: message.text)
async def timer_hafta(message: Message, state: FSMContext):
    eslatma_vaqti = message.text 
    user_data = await state.get_data()  
    selected_city = user_data.get("selected_city", None)

    if not selected_city:
        await message.answer("Shahar tanlanmagan. Iltimos, oldin shaharni tanlang.")
        return
    
    await message.answer("Yetti kunlik eslatma saqlandi! \nBiz sizga shahringiz haqidagi ob-havo malumotlarini yetti kun davomida siz kiritgan vaqtda yuboramiz.")


    # 7 kun davomida har kuni belgilangan vaqtda ob-havo eslatmasini yuborish
    for kun in range(7):  
        while True:
            if time.strftime('%H:%M:%S') == eslatma_vaqti:
                ob_havo_info = weather(selected_city) 
                await message.answer(
                    f"{kun + 1}-kun eslatmasi ⏰ {menu_country[selected_city]} shahridagi ob-havo ma'lumotlari:\n\n{ob_havo_info}", 
                    reply_markup=sozlama
                )
                break
            else:
                continue


# orqaga qaytish tugmasi

@dp.callback_query(F.data=="back")
async def change_code(callback_query:CallbackQuery):
    await callback_query.message.answer("Shaharni tanlang", reply_markup=menu)



@dp.callback_query(F.data=="change")
async def change_code(callback_query:CallbackQuery):
    await callback_query.message.answer("Shahar dan birini tanlang", reply_markup=menu)
