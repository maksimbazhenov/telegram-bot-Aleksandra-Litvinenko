from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()

bot = Bot(token ='5388546617:AAHtm80VPJ_L5cyggNScnvqNiNXkP4KPCq8')
dp = Dispatcher(bot, storage=storage)
