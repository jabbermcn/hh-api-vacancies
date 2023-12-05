import os

from aiogram import Dispatcher

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

dp = Dispatcher()
