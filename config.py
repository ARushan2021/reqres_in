"""Модуль содержит все константы касающиеся проекта"""
import datetime


class Config:

    DIRECTORY_LOGS = 'logs/'
    DIRECTORY_TEST_REPORTS = 'test_reports/'
    TIME_RESPONSE = 4
    DIRECTORY_AND_NAME_LOGS = f'logs/log_{str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))}.log'
    LOCATOR_SEARCH_TIME = 30
    DIRECTORY_DRIVER_CHROME = "driver/chromedriver.exe"


