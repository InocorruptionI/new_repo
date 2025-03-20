from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, CallbackQuery, InlineQuery, InlineKeyboardButton, \
    InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from datetime import date, time, datetime

import keyboards as kb


class DateStates(StatesGroup):
    waiting_date = State()
    waiting_time = State()


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет! Ты ученик или преподаватель?', reply_markup=kb.start)


@router.message(F.text == 'Преподаватель')
async def callback_start_ru_en(message: Message):
    await message.answer('Выберите действие:', reply_markup=kb.Lecturer_menu)


@router.callback_query(F.data == 'create_schedule')
async def create_ched(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Окей, давай составлять расписание. Скажи мне на какой день/месяц/год ты хочешь его сделать.'
                          'Пришли мне это в формате "26.05.2025"')
    await state.set_state(DateStates.waiting_date)


@router.message(DateStates.waiting_date)
async def date_ched(message: Message, state: FSMContext):
    date1 = message.text
    try:
        day, month_l, year = date1.split('.')
        dt = date(int(year), int(month_l), int(day))
        if (len(day) == 2 and len(month_l) == 2 and len(year) == 4 and
                day.isdigit() and month_l.isdigit() and year.isdigit()):
            await message.answer(f'Отлично, дата есть {dt}, напиши теперь на какое время ты хочешь поставить слот в формате '
                                 f'ЧЧ:ММ')
            await state.clear()
            await state.set_state(DateStates.waiting_time)
        else:
            await message.answer('Пожалуйста используйте формат ДД.ММ.ГГГГ')
    except ValueError:
        await message.answer('Пожалуйста используйте формат ДД.ММ.ГГГГ')


@router.message(DateStates.waiting_time)
async def time_ched(message: Message, state: FSMContext):
    time1 = message.text
    try:
        hours, minutes = time1.split(':')
        if 1 <= len(minutes) <= 2 and 1 <= len(hours) <= 2 and minutes.isdigit() and hours.isdigit():
            await message.answer(f'Отлично, слот на {time1} готов.')
            await message.answer('Выбери действие:', reply_markup=kb.completion)
            await state.clear()
        else:
            await message.answer('Введи время в формате: ЧЧ:ММ')
    except ValueError:
        await message.answer('Введи время в формате: ЧЧ:ММ')


@router.callback_query(F.data == 'add_schedule')
async def add_ched(callback: CallbackQuery):
    await callback.message.answer('Подскажи мне на какую дату ты хочешь дополнить расписание:', )
