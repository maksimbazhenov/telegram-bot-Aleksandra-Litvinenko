from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
a1 = KeyboardButton('/Режим_работы')
a2 = KeyboardButton ('/Расположение')
a3 = KeyboardButton ('/Скидки')
a4 = KeyboardButton ('/Поделиться номером', request_contact=True)
a5 = KeyboardButton ('/Отправить местоположение', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(a1).add(a2).add(a3).row(a4).row(a5)