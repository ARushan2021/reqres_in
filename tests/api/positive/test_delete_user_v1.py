"""Позитивный тест"""
import allure
import pytest


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Positive keys')
@allure.epic('API Тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('id_user',
                         ['20',
                          '32'])
@allure.title('Удаление пользователя')
def test_delete_user_v1(base, id_user):

    response = base.api_v1.delete_api(id_user=id_user)
    base.asserts.assert_empty_body(response=response, exp_status_code=204)
