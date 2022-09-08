'''
Реализовать несколько негативных тестов (например, проверяющие правильность
возвращаемых кодов ошибок)

В случае ошибки при обработке запроса формат {"statusCode": код ошибки(int),
"statusMessage": сообщение об ошибке}
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
    subprocess.run(
        ["C:\\Python\\infotecs_test_task\\resources\\webcalculator.exe", "start"],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def teardown_module():
    '''Остановка вебкалькулятора.'''
    subprocess.run(
        ["C:\\Python\\infotecs_test_task\\resources\\webcalculator.exe", "stop"],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

class TestCalculateError:
    def test_zero_division(self):
        '''Ожидаемый формат ответа - {"statusCode": 1, "statusMessage": сообщение об ошибке}
        Описание ошибки - Ошибка вычисления'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/division",
            json={"x": 5, "y": 0}, timeout=10).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 1
        assert isinstance(response_body["statusMessage"], str)
    
    def test_zero_remainder(self):
        '''Ожидаемый формат ответа - {"statusCode": 1, "statusMessage": сообщение об ошибке}
        Описание ошибки - Ошибка вычисления'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/remainder",
            json={"x": 5, "y": 0}, timeout=10).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 1
        assert isinstance(response_body["statusMessage"], str)

class TestNotEnoughKeysError:
    def test_not_enough_keys(self):
        '''Ожидаемый формат ответа - {"statusCode": 2, "statusMessage": сообщение об ошибке}
        Описание ошибки - Не хватает ключей в теле запроса'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={"x": 23}, timeout=10). json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 2
        assert isinstance(response_body["statusMessage"], str)

    def test_empty_json(self):
        '''Ожидаемый формат ответа - {"statusCode": 2, "statusMessage": сообщение об ошибке}
        Описание ошибки - Не хватает ключей в теле запроса'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={}, timeout=10).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 2
        assert isinstance(response_body["statusMessage"], str)

class TestNotIntegerValueError:
    def test_one_number_is_float(self):
        '''Ожидаемый формат ответа - {"statusCode": 3, "statusMessage": сообщение об ошибке}
        Описание ошибки - Одно из значений не является целым числом'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={"x": 2.2, "y": 3}, timeout=10).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 3
        assert isinstance(response_body["statusMessage"], str)

    def test_two_number_is_float(self):
        '''Ожидаемый формат ответа - {"statusCode": 3, "statusMessage": сообщение об ошибке}
        Описание ошибки - Одно из значений не является целым числом'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={"x": 2.2, "y": 1.3}, timeout=10).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 3
        assert isinstance(response_body["statusMessage"], str)
   
    def test_one_number_is_bool(self):
        '''Ожидаемый формат ответа - {"statusCode": 3, "statusMessage": сообщение об ошибке}
        Описание ошибки - Одно из значений не является целым числом'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={"x": True, "y": 3}, timeout=10).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 3
        assert isinstance(response_body["statusMessage"], str)

    def test_one_number_is_string(self):
        '''Ожидаемый формат ответа - {"statusCode": 3, "statusMessage": сообщение об ошибке}
        Описание ошибки - Одно из значений не является целым числом'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={"x": "f", "y": 1}, timeout=10).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 3
        assert isinstance(response_body["statusMessage"], str)
  
    def test_one_number_is_dict(self):
        '''Ожидаемый формат ответа - {"statusCode": 3, "statusMessage": сообщение об ошибке}
        Описание ошибки - Одно из значений не является целым числом'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={"x": {}, "y": 1}, timeout=10).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 3
        assert isinstance(response_body["statusMessage"], str)
  
    def test_one_number_is_set(self):
        '''Ожидаемый формат ответа - {"statusCode": 3, "statusMessage": сообщение об ошибке}
        Описание ошибки - Одно из значений не является целым числом'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={"x": (), "y": 1}, timeout=10).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 3
        assert isinstance(response_body["statusMessage"], str)

    def test_one_number_is_list(self):
        '''Ожидаемый формат ответа - {"statusCode": 3, "statusMessage": сообщение об ошибке}
        Описание ошибки - Одно из значений не является целым числом'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={"x": [], "y": 1}, timeout=10).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 3
        assert isinstance(response_body["statusMessage"], str)

class TestValueSizeError:
    def test_one_number_max_exceed(self):
        '''Требование к размеру значения - от -2147483648 до 2147483647
        Ожидаемый формат ответа - {"statusCode": 4, "statusMessage": сообщение об ошибке}
        Описание ошибки - Превышен размер одного из значений'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={"x": 2147483648, "y": 3}, timeout=10).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 4
        assert isinstance(response_body["statusMessage"], str)

    def test_one_number_min_exceed(self):
        '''Требование к размеру значения - от -2147483648 до 2147483647
        Ожидаемый формат ответа - {"statusCode": 4, "statusMessage": сообщение об ошибке}
        Описание ошибки - Превышен размер одного из значений'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={"x": 3, "y": -2147483649}, timeout=10).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 4
        assert isinstance(response_body["statusMessage"], str)
   
    def test_really_big_size(self):
        '''Требование к размеру значения - от -2147483648 до 2147483647
        Ожидаемый формат ответа - {"statusCode": 4, "statusMessage": сообщение об ошибке}
        Описание ошибки - Превышен размер одного из значений'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={"x": 3, "y": -99999999999999999999999999999999999}, timeout=10).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 4
        assert isinstance(response_body["statusMessage"], str)

class TestInvalidRequestBodyError:
    def test_request_without_json(self):
        '''Ожидаемый формат ответа - {"statusCode": 5, "statusMessage": сообщение об ошибке}
        Описание ошибки - Неправильный формат тела запроса'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition", timeout=10).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 5
        assert isinstance(response_body["statusMessage"], str)

    def test_three_numbers_json(self):
        '''Ожидаемый формат ответа - {"statusCode": 5, "statusMessage": сообщение об ошибке}
        Описание ошибки - Неправильный формат тела запроса'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={"x": 42, "y": 24, "z": 12}, timeout=10).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 5
        assert isinstance(response_body["statusMessage"], str)

    def test_other_names_of_keys(self):
        '''
        Ожидаемый формат ответа - {"statusCode": 5, "statusMessage": сообщение об ошибке}
        Описание ошибки - Неправильный формат тела запроса'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition",
            json={"z": 42, "e": 24}, timeout=10).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 5
        assert isinstance(response_body["statusMessage"], str)

    def test_str_instead_of_json(self):
        '''Ожидаемый формат ответа - {"statusCode": 5, "statusMessage": сообщение об ошибке}
        Описание ошибки - Неправильный формат тела запроса'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition", timeout=10, json="I am Json Statham").json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 5
        assert isinstance(response_body["statusMessage"], str)

            
    def test_different_keys_values_json(self):
        '''Ожидаемый формат ответа - {"statusCode": 5, "statusMessage": сообщение об ошибке}
        Описание ошибки - Неправильный формат тела запроса'''
        response_body = requests.post(
            url="http://127.0.0.1:17678/api/addition", timeout=10,
            json={
                "werwerwer": 1231231313,
                "fififififi": 999999999999999999999999999999,
                "212313131": "asdfghhrewedfghrewsdf",
                83848234234: True,
                True: False,
                123131: 13131313,
                1.1: 1231,
                None: [],
                131: {},
                "aagag": ()
            }).json()
        assert len(response_body) == 2
        assert response_body["statusCode"] == 5
        assert isinstance(response_body["statusMessage"], str)