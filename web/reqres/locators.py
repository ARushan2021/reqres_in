"""Модуль с локаторами для reqres"""
from selenium.webdriver.common.by import By


class LocatorsReqres:
    """Локаторы для работы с reqres.ru"""

    TITLE = (By.CSS_SELECTOR, '.tagline:nth-child(1)')
    STATUS_CODE = (By.XPATH, '//span[@data-key="response-code"]')
    RESPONSE_BODY = (By.XPATH, '//pre[@data-key="output-response"]')
    LOADING = (By.XPATH, '//div[@data-key="spinner"]')

    GET_SINGLE_USER = (By.XPATH, '//li[@data-id="users-single"]')
    CREATE_NEW_USER = (By.XPATH, '//li[@data-id="post"]')
    DELETE_USER = (By.XPATH, '//li[@data-id="delete"]')
