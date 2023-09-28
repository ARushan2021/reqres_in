"""Модуль с базовыми методами на вэб страницах"""

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import Config


class BasePage:
    """Класс для базовых метод на страницах"""
    driver = None

    @allure.step("Открытие странички")
    def go_to_site(self, base_url):
        """Метод для открытия сайта
        Args:
            base_url: url сайта
            """
        self.driver.get(base_url)

    def find_element(self, locator, time=Config.LOCATOR_SEARCH_TIME):
        """Метод для поиска локатора на странице.
        Если локатор не нашелся в течение заданного времени, то выкидывает ошибку.
        Args:
            locator: локатор для поиска на странице
            time: время в течение которого ищется локатор на странице
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Не удается найти элемент по локатору {locator}")

    def loading(self, locator, time=Config.LOCATOR_SEARCH_TIME):
        """Метод для проверки загрузки странички. Если элемент загрузки найден на страничке, то код на паузе.
        Элемент проверяется в течение 30 сек.
        Args:
            locator: локатор для поиска на странице
            time: время в течение которого ищется локатор на странице
        """
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator),
                                                      message=f'Страница не успела загрузиться!')


