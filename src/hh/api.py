import asyncio
import json
import logging
import os
from datetime import datetime

import aiohttp
from aiohttp import ClientSession
from ujson import dumps

from src.bot.bot import bot
from dotenv import load_dotenv

load_dotenv()


class HHApi(object):
    BASE_URL: str = 'https://api.hh.ru'
    APPLICATION_QUERY: dict = {
        'per_page': '100',
        'text': 'Python, Django OR FastAPI',
        'experience': ['noExperience', 'between1And3'],
        'professional_role': 96,
        'period': 6,
        'order_by': 'publication_time',
    }
    APPLICATION_URL: str = '/vacancies'
    HEADERS = {
        'Content-Type': 'application/json',
        'User-Agent': 'PostmanRuntime/7.33.0',
    }
    vacancies_requests = []

    @staticmethod
    def create_session(func):
        async def wrapper(*args, **kwargs):
            async with ClientSession(
                    base_url=HHApi.BASE_URL,
                    headers=HHApi.HEADERS,
                    json_serialize=dumps
            ) as session:
                return await func(*args, **kwargs, session=session)

        return wrapper

    @classmethod
    @create_session
    async def _get(cls, url: str, query: dict = None, session: ClientSession = None):
        response = await session.get(
            url=url,
            params=query,
            verify_ssl=False
        )
        try:
            return await response.json()
        except (json.JSONDecodeError, aiohttp.ContentTypeError, aiohttp.ClientConnectionError,
                aiohttp.ClientPayloadError) as e:
            logging.error(f"Error: {e.__class__.__name__} - {str(e)}")

    @classmethod
    def load_requests_ids(cls):
        try:
            with open('requests_ids.json', 'r') as file:
                requests_ids = json.load(file)
        except FileNotFoundError:
            requests_ids = set()
        return requests_ids

    @classmethod
    def save_requests_ids(cls, requests_ids):
        with open('requests_ids.json', 'w') as file:
            json.dump(list(requests_ids), file)

    async def vacancies_list(self):
        requests_ids = self.load_requests_ids()

        try:
            response = await self._get(
                url=self.APPLICATION_URL,
                query=self.APPLICATION_QUERY
            )

            for item in response['items']:
                vacancy_id = item['id']
                alternate_url = item['alternate_url']

                if vacancy_id not in requests_ids:
                    requests_ids.add(vacancy_id)
                    self.save_requests_ids(requests_ids)

                    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    message = f'*Появилась вакансия* - ID {vacancy_id} ' \
                              f'({timestamp}), посмотреть по ссылке:' \
                              f' \n{alternate_url}.'
                    await bot.send_message(chat_id=os.getenv('CHAT_ID'), text=message, parse_mode='Markdown')
                    await asyncio.sleep(10)  # API hh.ru приниимает не больше 20 запросов в минуту

        except Exception as e:
            logging.error(f'Ошибка получения списка вакансий: {e}')
