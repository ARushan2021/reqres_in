import allure
import pytest

from web.reqres.steps_reqres import TestStepsReqres


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Positive keys')
@allure.epic('Web Тестирование портала "https://reqres.in/"')
@allure.title("Получение информации о пользователе")
@pytest.mark.parametrize('id_user',
                         ['2'])
def test_get_single_user(driver, base, id_user):

    response = base.api_v1.get_api_users(id_user=id_user)
    get_single_user = TestStepsReqres()
    get_single_user.steps_get_single_user(response)
