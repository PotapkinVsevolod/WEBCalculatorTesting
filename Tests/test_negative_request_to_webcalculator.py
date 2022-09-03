'''
______________________________________________________
|Код ошибки	|Описание ошибки                          |
|_____________________________________________________|
|1	        |Ошибка вычисления                        |
|2	        |Не хватает ключей в теле запроса         |
|3	        |Одно из значений не является целым числом|
|4	        |Превышен размер одного из значений       |
|5	        |Неправильный формат тела запроса         |
|0	        |Все хорошо                               |
|___________|_________________________________________|
'''

import subprocess
import json
import requests

def setup_module():
    '''Запуск вебкалькулятора.'''
    subprocess.run(["C:\\Python\\infotecs_test_task\\webcalculator.exe", "start"], check=True)


def teardown_module():
    '''Остановка вебкалькулятора.'''
    subprocess.run(["C:\\Python\\infotecs_test_task\\webcalculator.exe", "stop"], check=True)


def test_zero_division():
    '''Ожидаемый формат ответа - {"statusCode": 1, "statusMessage": сообщение об ошибке}'''
    response = requests.post(
        url="http://127.0.0.1:17678/api/division",
        json={"x": 5, "y": 0},
        timeout=1.5
    )
    data = json.loads(response.text)
    assert len(data) == 2
    assert data["statusCode"] == 1
    assert isinstance(data["statusMessage"], str)


def test_not_enough_keys():
    '''Ожидаемый формат ответа - {"statusCode": 2, "statusMessage": сообщение об ошибке}'''
    response = requests.post(
        url="http://127.0.0.1:17678/api/addition",
        json={"x": 23},
        timeout=1.5
    )
    data = json.loads(response.text)
    assert len(data) == 2
    assert data["statusCode"] == 2
    assert isinstance(data["statusMessage"], str)

def test_empty_json():
    '''Ожидаемый формат ответа - {"statusCode": 2, "statusMessage": сообщение об ошибке}'''
    response = requests.post(
        url="http://127.0.0.1:17678/api/addition",
        json={},
        timeout=1.5
    )
    data = json.loads(response.text)
    assert len(data) == 2
    assert data["statusCode"] == 2
    assert isinstance(data["statusMessage"], str)

def test_one_number_is_float():
    '''Ожидаемый формат ответа - {"statusCode": 3, "statusMessage": сообщение об ошибке}'''
    response = requests.post(
        url="http://127.0.0.1:17678/api/addition",
        json={"x": 2.2, "y": 3},
        timeout=1.5
    )
    data = json.loads(response.text)
    assert len(data) == 2
    assert data["statusCode"] == 3
    assert isinstance(data["statusMessage"], str)

def test_two_number_is_float():
    '''Ожидаемый формат ответа - {"statusCode": 3, "statusMessage": сообщение об ошибке}'''
    response = requests.post(
        url="http://127.0.0.1:17678/api/addition",
        json={"x": 2.2, "y": 1.3},
        timeout=1.5
    )
    data = json.loads(response.text)
    assert len(data) == 2
    assert data["statusCode"] == 3
    assert isinstance(data["statusMessage"], str)

def test_one_number_exceed():
    '''Требование к размеру значения - от -2147483648 до 2147483647
    Ожидаемый формат ответа - {"statusCode": 4, "statusMessage": сообщение об ошибке}'''
    response = requests.post(
        url="http://127.0.0.1:17678/api/addition",
        json={"x": 3, "y": 999999999999999999999},
        timeout=1.5
    )
    data = json.loads(response.text)
    assert len(data) == 2
    assert data["statusCode"] == 4
    assert isinstance(data["statusMessage"], str)

def test_two_number_exceed():
    '''Требование к размеру значения - от -2147483648 до 2147483647
    Ожидаемый формат ответа - {"statusCode": 4, "statusMessage": сообщение об ошибке}'''
    response = requests.post(
        url="http://127.0.0.1:17678/api/addition",
        json={"x": 999999999999999999999, "y": -999999999999999999999},
        timeout=1.5
    )
    data = json.loads(response.text)
    assert len(data) == 2
    assert data["statusCode"] == 4
    assert isinstance(data["statusMessage"], str)

def test_request_without_json():
    '''Ожидаемый формат ответа - {"statusCode": 5, "statusMessage": сообщение об ошибке}'''
    response = requests.post(
        url="http://127.0.0.1:17678/api/addition",
        timeout=1.5
    )
    data = json.loads(response.text)
    assert len(data) == 2
    assert data["statusCode"] == 5
    assert isinstance(data["statusMessage"], str)

def test_get_instead_of_post():
    '''Ожидаемый формат ответа - {"statusCode": 5, "statusMessage": сообщение об ошибке}'''
    response = requests.get(
        url="http://127.0.0.1:17678/api/addition",
        json={"x": 42, "y":24},
        timeout=1.5
    )
    data = json.loads(response.text)
    assert len(data) == 2
    assert data["statusCode"] == 5
    assert isinstance(data["statusMessage"], str)
