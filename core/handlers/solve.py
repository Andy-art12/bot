from os.path import defpath

from aiogram.types import Message
from aiogram import Bot
from core.utils.solve_FSM import StateForm
from aiogram.fsm.context import FSMContext
from core.keyboards.first_kb import first_kb
from core.keyboards.grade_kb import get_inline_kb

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
    contex_data = await state.get_data()
    a = float(contex_data.get('ratio_a'))
    b = float(contex_data.get('ratio_b'))
    c = float(contex_data.get('ratio_c'))
    d = b ** 2 - 4 * a * c
    if d < 0:
        await m.answer(f'Нет корней', reply_markup=first_kb())
    if d == 0:
        await m.answer(f'1 корень: {(-b + d**0.5)/(2*a)}', reply_markup=first_kb())
    if d > 0:
        await m.answer(f'2 корня {(-b + d**0.5)/(2*a)} и {(-b - d**0.5)/(2*a)}', reply_markup=first_kb())

async def choise_class( m:Message):
    await m.answer('выберите класс', reply_markup=get_inline_kb())
    # await bot.send_message(m.from_user.id, text='выберите класс',reply_markup=get_inline_kb())
