"""Модуль по подключению параметров"""

from .reqres.api_v1 import ApiV1
from utils.asserts import AssertTests


class Application:
    """Класс с подключением всех библиотек для тестирования API v1"""
    def __init__(self):
        self.api_v1 = ApiV1()
        self.asserts = AssertTests()
