import asyncio
import logging
import sys

from src.bot.bot import dp, bot
from src.hh.api import HHApi


async def foo():
    try:
        hh = HHApi()
        while True:
            await hh.vacancies_list()
            logging.debug("Ищем подходящие вакансии...")
    except Exception as e:
        logging.error(f'Ошибка функции foo(): {e}')


async def main() -> None:
    try:
        while True:
            asyncio.create_task(dp.start_polling(bot))
            await foo()
    except Exception as e:
        logging.error(f'Ошибка функции main(): {e}')


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
        asyncio.run(main())
    except Exception as e:
        logging.error(f'Ошибка запуска бота: {e}')
