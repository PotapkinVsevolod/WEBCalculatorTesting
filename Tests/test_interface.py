'''Тесты проверяющие корректность формата запроса/ответа для всех API-методов:
state, addition, multiplication, division, remainder.'''
import subprocess
import json
import requests


def setup_module():
    '''Запуск вебкалькулятора.'''
    subprocess.run(["C:\\Python\\infotecs_test_task\\webcalculator.exe", "start"], check=True)


def teardown_module():
    '''Остановка вебкалькулятора.'''
    subprocess.run(["C:\\Python\\infotecs_test_task\\webcalculator.exe", "stop"], check=True)


def test_state():
    '''Тест проверяющий корректность формата запроса/ответа API-метода state.'''
    response = requests.get(
        url='http://127.0.0.1:17678/api/state',
        timeout=1.5
    )
    data = json.loads(response.text)
    assert len(data) == 2
    assert data["statusCode"] == 0
    assert data["state"] == "OK"


def test_addition():
    '''Тест проверяющий корректность формата запроса/ответа API-метода addition.'''
    response = requests.post(
        url='http://127.0.0.1:17678/api/addition',
        json={"x": 1, "y": 2}, timeout=1.5
    )
    data = json.loads(response.text)
    assert len(data) == 2
    assert data["statusCode"] == 0
    assert isinstance(data["result"], int)


def test_multiplication():
    '''Тест проверяющий корректность формата запроса/ответа API-метода multiplication.'''
    response = requests.post(
        url='http://127.0.0.1:17678/api/multiplication',
        json={"x": 1, "y": 2}, timeout=1.5
    )
    data = json.loads(response.text)
    assert len(data) == 2
    assert data["statusCode"] == 0
    assert isinstance(data["result"], int)


def test_division():
    '''Тест проверяющий корректность формата запроса/ответа API-метода division.'''
    response = requests.post(
        url='http://127.0.0.1:17678/api/division',
        json={"x": 1, "y": 2}, timeout=1.5
    )
    data = json.loads(response.text)
    assert len(data) == 2
    assert data["statusCode"] == 0
    assert isinstance(data["result"], int)


def test_remainder():
    '''Тест проверяющий корректность формата запроса/ответа API-метода remainder.'''
    response = requests.post(
        url='http://127.0.0.1:17678/api/remainder',
        json={"x": 1, "y": 2}, timeout=1.5
    )
    data = json.loads(response.text)
    assert len(data) == 2
    assert data["statusCode"] == 0
    assert isinstance(data["result"], int)
