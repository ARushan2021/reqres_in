"""Модуль содержит все декораторы проекта"""

import os
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from web.base_page import BasePage

from api.application import Application
from config import Config


@pytest.fixture(scope='session')
def base():
    """Декоратор по настройке только для API тестов"""
    return Application()


@pytest.fixture(scope='session')
def clear_test_reports_and_logs():
    """Декоратор по очистке каталогов logs и test_reports
    В каталоге test_reports оставляет файл environment.properties"""
    f = os.listdir(Config.DIRECTORY_TEST_REPORTS)
    f.remove('environment.properties')
    for i in range(0, len(f)):
        os.remove(f'{Config.DIRECTORY_TEST_REPORTS}/{f[i]}')
    for c in os.listdir(Config.DIRECTORY_LOGS):
        os.remove(os.path.join(Config.DIRECTORY_LOGS, c))


@pytest.fixture(scope='session')
def driver():
    """Декоратор перед сессией - открывает страницу в браузере
    после окончания сессии - закрывает браузер."""
    s = Service(Config.DIRECTORY_DRIVER_CHROME)
    driver = webdriver.Chrome(service=s)
    BasePage.driver = driver
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    """Декоратор для скриншота в конце каждого web теста"""
    outcome = yield
    report = outcome.get_result()
    driver = item.funcargs.get('driver')
    if report.when == 'call' and driver is not None:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
