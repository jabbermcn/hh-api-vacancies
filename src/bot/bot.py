import os

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
