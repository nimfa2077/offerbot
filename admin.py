from aiogram import types, Dispatcher, Bot, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from state import *
from config import *
import client

@dp.callback_query_handler(lambda c: c.data == "no")
async def otklonit(cal: types.CallbackQuery):
	await bot.send_message(chat_id=ADMIN_ID,  text="Предложение отклонено")
	await bot.send_message(chat_id=mes[cal.message.message_id], text="Твой мем был отклонен и не был опубликован в канале :(")

@dp.callback_query_handler(lambda c: c.data == "yes")
async def prinyat(cal: types.CallbackQuery, state: FSMContext):
	#await bot.send_message(chat_id=ADMIN_ID, text="Предложение отклонено")
	await bot.send_message(chat_id=ADMIN_ID, text="Введи новое описание:")
	async with state.proxy() as data:
		data['MID'] = cal.message

	await admin.wait_for_descr.set()

@dp.message_handler(state=admin.wait_for_descr)
async def  describe(message: types.Message, state: FSMContext):
	await bot.send_message(chat_id=ADMIN_ID, text="Сообщение было опубликовано в таком виде:")
	async with state.proxy() as data:
		#data['MID'] = cal.message.message_id
		mesage = data['MID']
		if mesage.caption.find("\n") != -1:
			nick = mesage.caption
			number = nick.find("\n\n@")
			nick = nick[number + 2:]
		else:
			nick = mesage.caption
		await bot.send_photo(chat_id=ADMIN_ID, photo=mesage.photo[-1].file_id, caption=message.text + "\n\n" + nick)
		await bot.send_photo(chat_id=CHANEL_ID, photo=mesage.photo[-1].file_id, caption=message.text + "\n\n" + nick)
		await bot.send_message(chat_id=mes[data["MID"].message_id], text="Твой мем был опубликован в канале!")
	await state.finish()

@dp.callback_query_handler(lambda c: c.data == "fyes")
async def forse(cal: types.CallbackQuery):
	await bot.send_message(chat_id=ADMIN_ID,  text="Опубликовано!")
	await bot.send_photo(chat_id=CHANEL_ID, photo=cal.message.photo[-1].file_id, caption=cal.message.caption)
	await bot.send_message(chat_id=mes[cal.message.message_id], text="Твой мем был опубликован в канале!")


executor.start_polling(dp, skip_updates="True")