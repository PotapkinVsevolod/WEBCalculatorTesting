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
import requests

def setup_module():
    '''Запуск вебкалькулятора.'''
    subprocess.run(["C:\\Python\\infotecs_test_task\\webcalculator.exe", "start"], check=True)


def teardown_module():
    '''Остановка вебкалькулятора.'''
    subprocess.run(["C:\\Python\\infotecs_test_task\\webcalculator.exe", "stop"], check=True)

class TestCalculateError:
    def test_zero_division(self):
        '''Ожидаемый формат ответа - {"statusCode": 1, "statusMessage": сообщение об ошибке}
        Описание ошибки - Ошибка вычисления'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/division",
            json={"x": 5, "y": 0}, timeout=1.5).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 1
        assert isinstance(response_body["statusMessage"], str)


class TestNotEnoughKeysError:
    def test_not_enough_keys(self):
        '''Ожидаемый формат ответа - {"statusCode": 2, "statusMessage": сообщение об ошибке}
        Описание ошибки - Не хватает ключей в теле запроса'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={"x": 23}, timeout=1.5). json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 2
        assert isinstance(response_body["statusMessage"], str)

    def test_empty_json(self):
        '''Ожидаемый формат ответа - {"statusCode": 2, "statusMessage": сообщение об ошибке}
        Описание ошибки - Не хватает ключей в теле запроса'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={}, timeout=1.5).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 2
        assert isinstance(response_body["statusMessage"], str)

class TestNotIntegerValueError:
    def test_one_number_is_float(self):
        '''Ожидаемый формат ответа - {"statusCode": 3, "statusMessage": сообщение об ошибке}
        Описание ошибки - Одно из значений не является целым числом'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={"x": 2.2, "y": 3}, timeout=1.5).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 3
        assert isinstance(response_body["statusMessage"], str)

    def test_two_number_is_float(self):
        '''Ожидаемый формат ответа - {"statusCode": 3, "statusMessage": сообщение об ошибке}
        Описание ошибки - Одно из значений не является целым числом'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={"x": 2.2, "y": 1.3}, timeout=1.5).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 3
        assert isinstance(response_body["statusMessage"], str)

class TestValueSizeError:
    def test_one_number_exceed(self):
        '''Требование к размеру значения - от -2147483648 до 2147483647
        Ожидаемый формат ответа - {"statusCode": 4, "statusMessage": сообщение об ошибке}
        Описание ошибки - Превышен размер одного из значений'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={"x": 3, "y": 999999999999999999999}, timeout=1.5).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 4
        assert isinstance(response_body["statusMessage"], str)

    def test_two_number_exceed(self):
        '''Требование к размеру значения - от -2147483648 до 2147483647
        Ожидаемый формат ответа - {"statusCode": 4, "statusMessage": сообщение об ошибке}
        Описание ошибки - Превышен размер одного из значений'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={"x": 999999999999999999999, "y": -999999999999999999999}, timeout=1.5).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 4
        assert isinstance(response_body["statusMessage"], str)

class TestInvalidRequestBodyError:
    def test_request_without_json(self):
        '''Ожидаемый формат ответа - {"statusCode": 5, "statusMessage": сообщение об ошибке}
        Описание ошибки - Неправильный формат тела запроса'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition", timeout=1.5).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 5
        assert isinstance(response_body["statusMessage"], str)

    def test_three_numbers_json(self):
        '''Ожидаемый формат ответа - {"statusCode": 5, "statusMessage": сообщение об ошибке}
        Описание ошибки - Неправильный формат тела запроса'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={"x": 42, "y": 24, "z": 12}, timeout=1.5).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 5
        assert isinstance(response_body["statusMessage"], str)

    def test_other_names_of_keys(self):
        '''Ожидаемый формат ответа - {"statusCode": 5, "statusMessage": сообщение об ошибке}
        Описание ошибки - Неправильный формат тела запроса'''
        response_body = requests.get(
            url="http://127.0.0.1:17678/api/addition",
            json={"z": 42, "e": 24}, timeout=1.5).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 5
        assert isinstance(response_body["statusMessage"], str)

