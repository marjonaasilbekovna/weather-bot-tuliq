from aiogram.fsm.state import State, StatesGroup

class Vaqt(StatesGroup):
    vaqt = State() 
    UchKunlik = State()
    BeshKunlik = State()
    YettiKunlik = State()