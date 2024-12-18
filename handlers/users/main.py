import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from weather import weather
from keyboard_buttons.inline.menu import menu, menu_country, sozlama
from loader import dp,bot,db,ADMINS,TOKEN
from menucommands.set_bot_commands  import set_default_commands


# foydalanuvchi tanlagan shahar haqida malumot chiqarish
@dp.callback_query(lambda callback_query: callback_query.data in menu_country.keys())
async def weather_info(callback_query: CallbackQuery, state:FSMContext):
    selected_city = callback_query.data
    ob_havo_info = weather(selected_city)
    
    await callback_query.message.answer(f"{menu_country[selected_city]} shahridagi ob-havo ma'lumotlari:\n\n{ob_havo_info}", reply_markup=sozlama)
    
    await callback_query.message.delete()

@dp.callback_query(F.data=="change")
async def change_code(callback_query:CallbackQuery):
    await callback_query.message.answer("Shahar dan birini tanlang", reply_markup=menu)
