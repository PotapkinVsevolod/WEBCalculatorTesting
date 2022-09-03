'''Тесты, проверяющие основную функциональность приложения: правильность вычисления результата
при указании допустимых входных данных. Пример тела запроса: {“x”:42, “y”:24}. Значение - int. '''
import subprocess
import json
import requests
import pytest


def setup_module():
    '''Запуск вебкалькулятора.'''
    subprocess.run(["C:\\Python\\infotecs_test_task\\webcalculator.exe", "start"], check=True)

def teardown_module():
    '''Остановка вебкалькулятора.'''
    subprocess.run(["C:\\Python\\infotecs_test_task\\webcalculator.exe", "stop"], check=True)


@pytest.mark.parametrize(
    "_x, _y, expected_result",
    [
        (
            2147483647,
            2147483647,
            4294967294
        ),
        (
            -2147483648,
            -2147483648,
            -4294967296
        ),
        (
            3,
            -8,
            -5
        ),
        (
            -100000,
            90000,
            -10000
        ),
        (
            12345678,
            0,
            12345678
        ),
        (
            -987,
            0,
            -987
        ),
        (
            0,
            -98765432,
            -98765432
        ),
        (
            0,
            -123,
            -123
        ),
        (
            0,
            0,
            0
        )
    ]
)
def test_addition(_x, _y, expected_result):
    '''Тест, проверяющий корректность вычисления для API-метода addition (сложение).'''
    response = requests.post(
        url="http://127.0.0.1:17678/api/addition",
        json={"x": _x, "y": _y}, timeout=1.5
    )
    data = json.loads(response.text)
    assert data["result"] == expected_result


@pytest.mark.parametrize(
    "_x, _y, expected_result",
    [
        (
            2147483647,
            2147483647,
            4611686014132420609
        ),
        (
            -2147483648,
            -2147483648,
            4611686018427387904
        ),
        (
            2,
            -4,
            -8
        ),
        (
            -900000,
            80000,
            -72000000000
        ),
        (
            13243546,
            0,
            0
        ),
        (
            -97867564,
            0,
            0
        ),
        (
            0,
            192837465,
            0
        ),
        (
            0,
            -915,
            0
        ),
        (
            0,
            0,
            0
        ),
        (
            256,
            -1,
            -256
        )
    ]
)
def test_multiplication(_x, _y, expected_result):
    '''Тест, проверяющий корректность вычисления для API-метода multiplication (умножение).'''
    response = requests.post(
        url="http://127.0.0.1:17678/api/multiplication",
        json={"x": _x, "y": _y}, timeout=1.5
    )
    data = json.loads(response.text)
    assert data["result"] == expected_result


@pytest.mark.parametrize(
    "_x, _y, expected_result",
    [
        (
            2147483647,
            2147483647,
            1
        ),
        (
            -2147483648,
            -2147483648,
            1
        ),
        (
            5,
            -4,
            -2
        ),
        (
            -500000,
            50000,
            -10
        ),
        (
            0,
            123123123,
            0
        ),
        (
            0,
            -987987,
            0
        ),
        (
            159260371,
            -1,
            -159260371
        )
    ]
)
def test_division(_x, _y, expected_result):
    '''Тест, проверяющий корректность вычисления для API-метода division (целочисленное деление).'''
    response = requests.post(
        url="http://127.0.0.1:17678/api/division",
        json={"x": _x, "y": _y}, timeout=1.5
    )
    data = json.loads(response.text)
    assert data["result"] == expected_result


@pytest.mark.parametrize(
    "_x, _y, expected_result",
    [
        (
            2147483647,
            2147483647,
            0
        ),
        (
            -2147483648,
            -2147483648,
            0
        ),
        (
            10,
            -3,
            -2
        ),
        (
            21,
            7,
            0
        ),
        (
            -300000,
            30000,
            0
        ),
        (
            0,
            123234345,
            0
        ),
        (
            0,
            -98787,
            0
        ),
        (
            1100,
            -1,
            0
        )
    ]
)
def test_remainder(_x, _y, expected_result):
    '''Тест, проверяющий корректность вычисления для API-метода remainder (остаток от деления).'''
    response = requests.post(
        url="http://127.0.0.1:17678/api/remainder",
        json={"x": _x, "y": _y}, timeout=1.5
    )
    data = json.loads(response.text)
    assert data["result"] == expected_result
