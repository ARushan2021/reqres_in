import allure
import pytest

from web.reqres.steps_reqres import TestStepsReqres


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Positive keys')
@allure.epic('Web Тестирование портала "https://reqres.in/"')
@allure.title("Удаление пользователя")
@pytest.mark.parametrize('id_user',
                         ['2'])
def test_delete_user(driver, base, id_user):

    response = base.api_v1.delete_api(id_user=id_user)
    delete_user = TestStepsReqres()
    delete_user.steps_delete_user(response)

