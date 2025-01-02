from aiogram.types import Message
from aiogram import Bot
from core.utils.solve_FSM import StateForm
from aiogram.fsm.context import FSMContext

async def A(m: Message, state: FSMContext):
    await m.answer(f'Введите коэффициент A: ')
    await state.set_state(StateForm.GET_A)


async def B(m: Message, state: FSMContext):
    await m.answer(f'Введите коэффициент B: ')
    await state.update_data(ratio_a=m.text)
    await state.set_state(StateForm.GET_B)

async def C(m: Message, state: FSMContext):
    await m.answer(f'Введите коэффициент C: ')
    await state.update_data(ratio_b=m.text)
    await state.set_state(StateForm.GET_C)

async def answer(m: Message, state: FSMContext):
    await m.answer(f'Корни :')
    await state.update_data(ratio_c=m.text)
