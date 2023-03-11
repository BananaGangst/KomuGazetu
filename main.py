from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os, json, string
import time
from config import API_TOKEN

#ТОКЕН БОТА
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


version = "1.0" ##НАПИШИ ВЕРСИЮ Пример : "1.0"


async def on_startup(_):
	print("Бот запущен!")


@dp.message_handler(commands=['get_id'])
async def get_id(message: types.Message):
    await message.answer(message.from_user.id)

###########   ОСНОВНАЯ ЧАСТЬ   #############


#ФИЛЬТР И КОМАНДЫ
@dp.message_handler()
async def echo_send(message : types.Message):
	if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
		.intersection(set(json.load(open('cenz1.json')))) != set():
		await message.reply(f"🤬 Ссылки запрещены 🤬 \n@{message.from_user.username}")
		await message.delete()
	elif {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
		.intersection(set(json.load(open('cenz.json')))) != set():
		await message.reply(f"🤬 Маты запрещены 🤬 \n@{message.from_user.username}")
		await message.delete()



#РАБОТА БОТА=TRUE
#executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
if __name__ == '__main__':
    executor.start_polling(dp)
