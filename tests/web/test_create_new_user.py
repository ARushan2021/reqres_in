import allure
import pytest

from api.reqres.common import Common
from web.reqres.steps_reqres import TestStepsReqres


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Positive keys')
@allure.epic('Web Тестирование портала "https://reqres.in/"')
@allure.title("Создание нового пользователя")
@pytest.mark.parametrize('body_request',
                         [f'{Common.REQUEST_BODY_POST3}'])
def test_create_new_user(driver, base, body_request):

    response = base.api_v1.post_api_users(body_request)
    create_new_user = TestStepsReqres()
    create_new_user.steps_create_new_user(response)

