from aiogram.fsm.state import StatesGroup, State

class Reg(StatesGroup):
    service = State()
    data_t = State()
    time = State()
    confirmation = State()