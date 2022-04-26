from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BOT_TOKEN = ""
bot = Bot(BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
ADMIN_ID = ""
CHANEL_ID = ""
mes = {}
