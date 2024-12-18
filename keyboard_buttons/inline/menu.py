from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


menu_country = {
    "navoi": "Navoiy",
    "tashkent": "Toshkent",
    "samarkand": "Samarqand",
    "jizzakh": "Jizzax",
    "fergana": "Farg'ona",
    "bukhara": "Buxoro",
    "namangan": "Namangan",
    "andijan": "Andijon",
    "zarafshan": "Zarafshon",
    "urgench": "Urgench",
    "khiva": "Xiva",
    "sirdaryo": "Sirdaryo",
    "nukus": "Nukus",
    "termiz": "Termiz"
}

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Navoiy", callback_data="navoi"), 
            InlineKeyboardButton(text="Toshkent", callback_data="tashkent")
        ],
        [
            InlineKeyboardButton(text="Samarqand", callback_data="samarkand"), 
            InlineKeyboardButton(text="Jizzax", callback_data="jizzakh")
        ],
        [
            InlineKeyboardButton(text="Farg'ona", callback_data="fergana"),
            InlineKeyboardButton(text="Buxoro", callback_data="bukhara")           
        ],
        [
            InlineKeyboardButton(text="Namangan", callback_data="namangan"),
            InlineKeyboardButton(text="Andijon", callback_data="andijan")
        ],
        [
            InlineKeyboardButton(text="Zarafshon", callback_data="zarafshan"),
            InlineKeyboardButton(text="Urgench", callback_data="urgench")
        ],
        [
            InlineKeyboardButton(text="Xiva", callback_data="khiva"),
            InlineKeyboardButton(text="Sirdaryo", callback_data="sirdaryo")
        ],
        [
            InlineKeyboardButton(text="Termiz", callback_data="termiz"),
            InlineKeyboardButton(text="Nukus", callback_data="nukus")
        ]
    ]
)

sozlama = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zgartirish", callback_data="change"), 
        ]
    ]
)
