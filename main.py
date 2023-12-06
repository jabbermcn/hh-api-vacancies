import asyncio
import logging
import sys

from src.bot.bot import dp, bot
from src.hh.api import HHApi


async def foo():
    """Функция для поиска вакансий."""
    try:
        hh = HHApi()
        while True:
            logging.debug("Ищем подходящие вакансии...")
            await hh.vacancies_list()
            await asyncio.sleep(30)
    except Exception as e:
        logging.error(f'Ошибка функции foo(): {e}', exc_info=True)


async def main() -> None:
    """Основная функция для запуска бота и поиска вакансий."""
    try:
        while True:
            asyncio.create_task(dp.start_polling(bot))
            await foo()
    except Exception as e:
        logging.error(f'Ошибка функции main(): {e}', exc_info=True)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.DEBUG, stream=sys.stdout,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        asyncio.run(main())
    except Exception as e:
        logging.error(f'Ошибка запуска бота: {e}', exc_info=True)
