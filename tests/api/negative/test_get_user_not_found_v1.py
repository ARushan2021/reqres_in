"""Негативный тест"""
import allure
import pytest


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Negative keys')
@allure.epic('API Тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('id_user',
                         ['200',
                          '300'])
@allure.title('Неуспешный запрос информации о пользователе, неверный id')
def test_user_not_found_v1(base, id_user):

    response = base.api_v1.get_api_users(id_user=id_user)
    base.asserts.assert_empty_body(response=response, exp_status_code=404)

