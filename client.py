from aiogram import types,  executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from config import *
from state import *

bt_1 = InlineKeyboardButton(text= "Одобрить", callback_data="yes")
bt_2 = InlineKeyboardButton(text= "Одобрить без изменений", callback_data="fyes")
bt_3 = InlineKeyboardButton(text= "Отклонить", callback_data="no")

inline_kb_voit = InlineKeyboardMarkup().add(bt_1).add(bt_2).add(bt_3)

@dp.message_handler(commands=["start"])
async def start(messange: types.Message):
	await bot.send_message(messange.chat.id, text="Напиши /sendmeme чтобы предложить")
	#await waiting.waiting_for_messange.set()

@dp.message_handler(commands=["sendmeme"])
async def start_offering(messange: types.Message):
	await bot.send_message(messange.chat.id, text="Отправь мем, который хочешь залить в канал")
	await waiting.waiting_for_offer.set()

@dp.message_handler(state=waiting.waiting_for_offer, content_types=types.ContentTypes.PHOTO)
async def start_offering(message: types.Message, state: FSMContext):
	if message.caption == None:
		mess = await bot.send_photo(chat_id=ADMIN_ID, photo=message.photo[-1].file_id, caption=f"\n\n@{message.from_user.username}", reply_markup=inline_kb_voit)
	else:
		mess = await bot.send_photo(chat_id=ADMIN_ID, photo=message.photo[-1].file_id, caption=message.caption + f"\n\n@{message.from_user.username}", reply_markup=inline_kb_voit)
	mes[mess.message_id] = message.from_user.id
	await bot.send_message(message.chat.id, text="Твой мем был отправлен!")
	await state.finish()

if __name__ == "__main__":
	executor.start_polling(dp, skip_updates="True")