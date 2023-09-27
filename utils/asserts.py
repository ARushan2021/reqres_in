"""Модуль с шагами по проверке"""
import json
import allure
from config import Config


class AssertTests:
    """Класс проверок для Тестов"""

    @staticmethod
    def check_status_code(status_code, exp_status_code):
        """Метод проверки статус кода.
        Args:
            status_code: полученный статус код
            exp_status_code: ожидаемый статус код
        """

        msg = f'Статус код ответа "{status_code}" отличен от "{exp_status_code}"'
        assert int(status_code) == exp_status_code, msg

    @staticmethod
    def validate_time_response(response):
        """Метод для проверки времени ответа
        Args:
            response: полученный ответ
        """

        time_response = response.elapsed.total_seconds()
        assert time_response < Config.TIME_RESPONSE, \
            f'Ошибка! Время ответа на запрос превысило 2 сек. и составило: {time_response}'

    @staticmethod
    @allure.step('Проверка статус кода, времени ответа на запрос, полей email и first_name в теле ответа')
    def assert_create_new_user(response, exp_status_code, body_request):
        """Метод для проверки:
        - полей email и first_name в теле ответа
        - проверка статус кода
        - проверка времени ответа.
        Args:
            response: полученный ответ
            exp_status_code: ожидаемый статус код
            body_request: тело для отправки запроса
        """
        response_body = response.json()
        status_code = response.status_code
        AssertTests.check_status_code(status_code, exp_status_code)
        AssertTests.validate_time_response(response)
        dict_body_request = eval(body_request)
        assert dict_body_request['email'] == response_body['email'], \
            f'email отправлен - {dict_body_request["email"]}, email из тела ответа - {response_body["email"]}'
        assert dict_body_request['first_name'] == response_body['first_name'], \
            f'first_name отправленное - {dict_body_request["first_name"]}, ' \
            f'first_name из тела ответа - {response_body["first_name"]}'

    @staticmethod
    @allure.step('Проверка статус кода, времени ответа на запрос, поля id в теле ответа')
    def assert_single_user(response, exp_status_code, id_user):
        """Метод для проверки:
        - поля id в теле ответа
        - проверка статус кода
        - проверка времени ответа.
        Args:
            response: полученный ответ
            exp_status_code: ожидаемый статус код
            id_user: id пользователя в запроса
        """
        response_body = response.json()
        status_code = response.status_code
        AssertTests.check_status_code(status_code, exp_status_code)
        AssertTests.validate_time_response(response)
        response_id = response_body['data']['id']
        assert response_id == int(id_user), f'Отправили id - {id_user} получили ответ с id - {response_id}'

    @staticmethod
    @allure.step('Проверка статус кода, времени ответа на запрос, пустого тела ответа')
    def assert_empty_body(response, exp_status_code):
        """Метод для проверки:
            - статус кода
            - проверка времени ответа
            - пустого тело ответа
        Args:
            response: полученный ответ
            exp_status_code: ожидаемый статус код
        """
        response_body = response.text
        assert response_body == '' or '{}'
        status_code = response.status_code
        AssertTests.check_status_code(status_code, exp_status_code)
        AssertTests.validate_time_response(response)

    @staticmethod
    @allure.step('Проверка статус кода, времени ответа на запрос, ошибки в теле ответа "error": "Missing password"')
    def assert_register_unsuccessful(response, exp_status_code):
        """Метод для проверки:
            - статус кода
            - проверка времени ответа
            - ошибки в теле ответа "error": "Missing password"
        Args:
            response: полученный ответ
            exp_status_code: ожидаемый статус код
        """
        response_body = response.json()
        assert response_body == {"error": "Missing password"}, f'Ошибка в теле ответа {response_body}'
        status_code = response.status_code
        AssertTests.check_status_code(status_code, exp_status_code)
        AssertTests.validate_time_response(response)