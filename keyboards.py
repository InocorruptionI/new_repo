from random import choice

from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, CallbackQuery, KeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram import F


start = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Преподаватель'), KeyboardButton(text='Ученик')]],
                                 resize_keyboard=True, input_field_placeholder='Выберите пункт')

Lecturer_menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Создать расписание', callback_data='create_schedule')],
                                                      [InlineKeyboardButton(text='Дополнить расписание', callback_data='add_schedule')],
                                                      [InlineKeyboardButton(text='архивировать расписание', callback_data='archive_data')]])


completion = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='завершить', callback_data='exit'),
                                                    InlineKeyboardButton(text='Добавить еще слот', callback_data='add_slot')]])








main_lang = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='English'),
                                          KeyboardButton(text='Русский')]],
                                resize_keyboard=True, one_time_keyboard=True,
                                input_field_placeholder='Выберите язык')


main_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='добавить бота в новую группу')],
                                          [KeyboardButton(text='добавить в группу нового пользователя')],
                                          [KeyboardButton(text='зафиксировать платеж')]],
                                resize_keyboard=True, input_field_placeholder='Выбери действие')


add_bot_in_group = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Вот моя ссылка, добавь меня в чат',
                                                                        url='https://t.me/T_a_s_k_manager_bot')]])

add_user_in_group = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='ссылка отправлена',
                                                                         callback_data='add_user')]])


actions_with_payments = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Нажми чтобы посмотреть действия с платежами',
                                                                             callback_data='actions_with_payments')]])


choice_action = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Добавить занятия', callback_data='action')]])


