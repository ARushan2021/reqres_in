"""Модуль содержит все декораторы проекта"""

import os
import pytest

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
