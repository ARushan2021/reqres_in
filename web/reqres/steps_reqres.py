"""Модуль с шагами по тестированию reqres.ru"""
import json

import allure

from utils.asserts import AssertTests
from web.base_page import BasePage
from web.reqres.common import ReqresCommon
from web.reqres.locators import LocatorsReqres


class BaseStepsReqres(BasePage):
    """Класс с базовыми шагами по тестированию reqres.ru"""

    @allure.step("Нажатие кнопки 'Запроса'")
    def click_api_method(self, locator_button):
        """Метод для нажатия нужного api-метода и скроллинг странички
            Args:
                locator_button: локатор кнопки
        """
        self.find_element(locator_button).click()
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.loading(locator=LocatorsReqres.LOADING)


class TestStepsReqres(BaseStepsReqres):
    """Класс с шагами по тестированию reqres.ru"""

    def steps_get_single_user(self, response):
        """Метод для тестирования получения информации о пользователе"""

        self.go_to_site(base_url=ReqresCommon.BASE_URL)
        heading_site = self.find_element(LocatorsReqres.TITLE).text
        AssertTests.assert_title(exp_heading=ReqresCommon.EXP_HEADING, heading_site=heading_site)
        self.click_api_method(locator_button=LocatorsReqres.GET_SINGLE_USER)
        response_body_api = response.json()
        status_code_api = response.status_code
        status_code = int(self.find_element(LocatorsReqres.STATUS_CODE).text)
        response_body_web = self.find_element(LocatorsReqres.RESPONSE_BODY).text
        response_body_web = json.loads(response_body_web)
        AssertTests.check_status_code(status_code=status_code, exp_status_code=status_code_api)
        AssertTests.assert_web_with_api(response_body_web=response_body_web,
                                        response_body_api=response_body_api)

    def steps_create_new_user(self, response):
        """Метод для тестирования создания нового пользователя"""

        self.go_to_site(base_url=ReqresCommon.BASE_URL)
        heading_site = self.find_element(LocatorsReqres.TITLE).text
        AssertTests.assert_title(exp_heading=ReqresCommon.EXP_HEADING, heading_site=heading_site)
        self.click_api_method(locator_button=LocatorsReqres.CREATE_NEW_USER)
        response_body_api = response.json()
        status_code_api = response.status_code
        status_code = int(self.find_element(LocatorsReqres.STATUS_CODE).text)
        response_body_web = self.find_element(LocatorsReqres.RESPONSE_BODY).text
        response_body_web = json.loads(response_body_web)
        AssertTests.check_status_code(status_code=status_code, exp_status_code=status_code_api)
        AssertTests.assert_job_and_name_web_with_api(response_body_web=response_body_web,
                                                     response_body_api=response_body_api)

    def steps_delete_user(self, response):
        """Метод для тестирования удаления пользователя"""

        self.go_to_site(base_url=ReqresCommon.BASE_URL)
        heading_site = self.find_element(LocatorsReqres.TITLE).text
        AssertTests.assert_title(exp_heading=ReqresCommon.EXP_HEADING, heading_site=heading_site)
        self.click_api_method(locator_button=LocatorsReqres.DELETE_USER)
        response_body_api = response.text
        status_code_api = response.status_code
        status_code = int(self.find_element(LocatorsReqres.STATUS_CODE).text)
        response_body_web = self.find_element(LocatorsReqres.RESPONSE_BODY).text
        response_body_web = response_body_web if len(response_body_web) < 3 else json.loads(response_body_web)
        AssertTests.check_status_code(status_code=status_code, exp_status_code=status_code_api)
        AssertTests.assert_web_with_api(response_body_web=response_body_web,
                                        response_body_api=response_body_api)


