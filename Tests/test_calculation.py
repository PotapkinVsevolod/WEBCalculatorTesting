import os
import requests
import json
import pytest

def setup_module(module):
    os.system('C:\\Python\\infotecs_test_task\\webcalculator.exe start')
    
def teardown_module(module):
    os.system('C:\\Python\\infotecs_test_task\\webcalculator.exe stop')

@pytest.mark.parametrize("x, y, expected_result", [(2147483647, 2147483647, 4294967294),
                                                   (-2147483648, -2147483648, -4294967296),
                                                   (3, -8, -5),
                                                   (-100000, 90000, -10000),
                                                   (12345678, 0, 12345678),
                                                   (-987, 0, -987),
                                                   (0, -98765432, -98765432),
                                                   (0, -123, -123),
                                                   (0, 0, 0)])
def test_addition(x, y, expected_result):
    response = json.loads(requests.post(url="http://localhost:17678/api/addition", json={"x": x, "y": y}).text)
    assert response["result"] == expected_result

@pytest.mark.parametrize("x, y, expected_result", [(2147483647, 2147483647, 4611686014132420609),
                                                   (-2147483648, -2147483648, 4611686018427387904),
                                                   (2, -4, -8),
                                                   (-900000, 80000, -72000000000),
                                                   (13243546, 0, 0),
                                                   (-97867564, 0, 0),
                                                   (0, 192837465, 0),
                                                   (0, -915, 0),
                                                   (0, 0, 0),
                                                   (256, -1, -256)])
def test_multiplication(x, y, expected_result):
    response = json.loads(requests.post(url="http://localhost:17678/api/multiplication", json={"x": x, "y": y}).text)
    assert response["result"] == expected_result

@pytest.mark.parametrize("x, y, expected_result", [(2147483647, 2147483647, 1),
                                                   (-2147483648, -2147483648, 1),
                                                   (5, -4, -2),
                                                   (-500000, 50000, -10),
                                                   (0, 123123123, 0),
                                                   (0, -987987, 0),
                                                   (159260371, -1, -159260371)])
def test_division(x, y, expected_result):
    response = json.loads(requests.post(url="http://localhost:17678/api/division", json={"x": x, "y": y}).text)
    assert response["result"] == expected_result

@pytest.mark.parametrize("x, y, expected_result", [(2147483647, 2147483647, 0),
                                                   (-2147483648, -2147483648, 0),
                                                   (10, -3, -2),
                                                   (21, 7, 0),
                                                   (-300000, 30000, 0),
                                                   (0, 123234345, 0),
                                                   (0, -98787, 0),
                                                   (1100, -1, 0)])
def test_remainder(x, y, expected_result):
    response = json.loads(requests.post(url="http://localhost:17678/api/remainder", json={"x": x, "y": y}).text)
    assert response["result"] == expected_result
