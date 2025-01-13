from aiogram import types,Bot,Dispatcher,executor
from buttons import main_menu
import time
api = '7263926581:AAF0gIyvsw7OTbsUWj5AJ4M3JPFWIXDU7rw'
bot = Bot(api)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_hi(sms:types.Message):
    await sms.answer(f'Hi {sms.from_user.first_name}!',
                     reply_markup=main_menu
                     ) 
    


@dp.message_handler(text='joke')
async def sendabout(sms:types.Message):
    await sms.reply(text='What do you call a magic dog?')
    time.sleep(5)
    await sms.reply(text="A labracadabrador.")
@dp.message_handler(text='Fact')
async def sendabout(sms:types.Message):
    await sms.reply(text='A cloud weighs around a million tonnes')
@dp.message_handler(text='Help')
async def send_image(sms:types.Message):
    await sms.reply(text='Press joke to see a joke or Press fact to see an interesting fact ')






if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)