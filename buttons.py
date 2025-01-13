from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
Joke  = KeyboardButton(text='Joke')
Fact = KeyboardButton(text='Fact')
Help = KeyboardButton(text='Help')
main_menu.add(Joke,Fact,Help)               
