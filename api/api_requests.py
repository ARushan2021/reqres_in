"""Модуль содержит базовый класс для отправки запросов"""

import requests
from utils.logger import Logger


class Request:
    """Обертка для отправки запросов"""

    def __init__(self):
        self.url = ''
        self.headers = {'Content-Type': 'application/json'}
        self.cookies = {}

    def custom_request(self, method, url, params=None, data=None, headers=None, cookies=None) -> requests.Response:
        """Кастомная функция по отправки запроса.
        Args:
            method: Метод запроса (GET, POST, ...)
            url: ссылка запроса
            params: для передачи параметров запроса в словаре
            data: body запроса
            headers: заголовки
            cookies: куки
        Returns:
            response: объект результата запроса
        """
        headers = self.headers if headers is None else headers
        cookies = self.cookies if cookies is None else cookies

        response = requests.request\
            (method=method, url=url, params=params, data=data, headers=headers, cookies=cookies)
        Logger.logging(response)
        return response
