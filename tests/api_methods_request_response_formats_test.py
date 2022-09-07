'''
Написать автоматические тесты (далее тесты), проверяющие корректность формата запроса/ответа
для всех указанных в описании API-методов (раздел API интерфейс приложения).

Для обращения к необходимой api-функции (далее задаче) необходимо указать в адресе запроса
её имя в следующем формате: http://host:port/api/имя_задачи
________________________________________________________
|Задача        |Описание                  |Тип запроса  |
|______________|__________________________|_____________|
|state         |Проверка состояния сервера|GET          |
|______________|__________________________|_____________|
|addition      |Сложение x и y            |POST         |
|______________|__________________________|_____________|
|multiplication|Умножение x и y           |POST         |
|______________|__________________________|_____________|
|division      |Деление на цело x на y    |POST         |
|______________|__________________________|_____________|
|remainder     |Остаток от деления x на y |POST         |
|______________|__________________________|_____________|

Пример адреса запроса: http://192.168.7.54:12345/api/addition

Для задач типа POST тело запроса должно содержать json с ключами “x” и “y”,
и значениями типа integer. Пример тела запроса: {“x”:42, “y”:24}.

Ответ на задачу state должен иметь формат {'statusCode': 0, 'state': 'OК'}.

Ответ на остальные задачи {"statusCode": 0, "result": результат операции(int)}.

'''

import subprocess

import pytest
import requests

PATH_TO_WEBCALCULATOR = "C:\\Python\\infotecs_test_task\\resources\\webcalculator.exe"
API_URL = "http://127.0.0.1:17678/api/"

def setup_module():
    '''Запуск вебкалькулятора.'''
    subprocess.run([PATH_TO_WEBCALCULATOR, "start"],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def teardown_module():
    '''Остановка вебкалькулятора.'''
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def test_get_request_to_get_state_api_method_return_correct_json():
    '''Ожидаемый формат ответа - {'statusCode': 0, 'state': 'OК'}'''
    response_body = requests.get(url=f'{API_URL}state', timeout=1.5).json()
    assert len(response_body) == 2
    assert response_body["statusCode"] == 0
    assert response_body["state"] == "OK"


@pytest.mark.parametrize("api_method", ["addition", "multiplication", "division", "remainder"])
def test_post_request_to_post_api_methods_return_correct_json(api_method):
    '''Ожидаемый формат ответа - {"statusCode": 0, "result": результат операции(int)}'''
    response_body = requests.post(
        url=f'{API_URL}{api_method}', timeout=1.5, json={"x": 42, "y": 24}).json()
    assert len(response_body) == 2
    assert response_body["statusCode"] == 0
    assert isinstance(response_body["result"], int)
