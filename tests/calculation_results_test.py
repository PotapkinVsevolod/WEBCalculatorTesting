'''
Написать тесты, проверяющие основную функциональность приложения:
правильность вычисления результата при указании допустимых входных данных.

Для обращения к необходимой api-функции (далее задаче) необходимо указать в адресе запроса
её имя в следующем формате: http://host:port/api/имя_задачи
________________________________________________________
|Задача        |Описание                  |Тип запроса  |
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

На входные значения налагаются следующие ограничения:
    Только целые числа
    Каждое число должно быть в диапазоне от -2147483648 до 2147483647
'''
import subprocess

import requests
import pytest

PATH_TO_WEBCALCULATOR = "C:\\Python\\infotecs_test_task\\resources\\webcalculator.exe"

def setup_module():
    '''Запуск вебкалькулятора.'''
    subprocess.run([PATH_TO_WEBCALCULATOR, "start"],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def teardown_module():
    '''Остановка вебкалькулятора.'''
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


@pytest.mark.parametrize(
    "x, y, expected_result",
    [(2147483647, 2147483647, 4294967294),
     (-2147483648, -2147483648, -4294967296),
     (3, -8, -5),
     (-100000, 90000, -10000),
     (12345678, 0, 12345678),
     (-987, 0, -987),
     (0, -98765432, -98765432),
     (1, -123, -122),
     (101, -1, 100),
     (0, 0, 0),
     (2147483646, 1, 2147483647)])
def test_x_plus_y_equals_expected_result(x, y, expected_result):
    '''Ожидаемый формат ответа - {"statusCode": 0, "result": результат операции(int)}'''
    response_body = requests.post(
        url="http://127.0.0.1:17678/api/addition",
        json={"x": x, "y": y}, timeout=1.5).json()
    assert response_body["result"] == expected_result


@pytest.mark.parametrize(
    "x, y, expected_result",
    [(2147483647, 2147483647, 4611686014132420609),
     (-2147483648, -2147483648, 4611686018427387904),
     (2, -4, -8),
     (-11111111, 8, -88888888),
     (13243546, 1, 13243546),
     (-97867564, 0, 0),
     (0, -915, 0),
     (0, 0, 0),
     (256, -1, -256)])
def test_x_times_y_equals_expected_result(x, y, expected_result):
    '''Ожидаемый формат ответа - {"statusCode": 0, "result": результат операции(int)}'''
    response_body = requests.post(
        url="http://127.0.0.1:17678/api/multiplication",
        json={"x": x, "y": y}, timeout=1.5).json()
    assert response_body["result"] == expected_result

@pytest.mark.parametrize(
    "x, y, expected_result",
    [(2147483647, 2147483647, 1),
     (-2147483648, -2147483648, 1),
     (-2147483648, 2147483647, -2),
     (5, -4, -2),
     (1, -1, -1),
     (-500000, 50000, -10),
     (0, 123123123, 0),
     (0, -987987, 0),
     (12345, 1, 12345),
     (159260371, -1, -159260371)])
def test_x_divided_by_y_equals_expected_result(x, y, expected_result):
    '''Ожидаемый формат ответа - {"statusCode": 0, "result": результат операции(int)}'''
    response_body = requests.post(
        url="http://127.0.0.1:17678/api/division",
        json={"x": x, "y": y}, timeout=1.5).json()
    assert response_body["result"] == expected_result

@pytest.mark.parametrize(
    "x, y, expected_result",
    [(2147483647, 2147483647, 0),
     (-2147483648, -2147483648, 0),
     (2147483647, -2147483648, -1),
     (10000, 10001, 10000),
     (10, -3, -2),
     (21, 7, 0),
     (-300000, 30000, 0),
     (0, 123234345, 0),
     (0, -98787, 0),
     (1100, -1, 0)])
def test_the_remainder_after_dividing_x_by_y_equals_expected_result(x, y, expected_result):
    '''Ожидаемый формат ответа - {"statusCode": 0, "result": результат операции(int)}'''
    response_body = requests.post(
        url="http://127.0.0.1:17678/api/remainder",
        json={"x": x, "y": y}, timeout=1.5).json()
    assert response_body["result"] == expected_result
    