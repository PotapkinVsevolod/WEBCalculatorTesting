import subprocess
import requests
import json
import pytest

PATH_TO_WEBCALCULATOR = "C:\\Python\\infotecs_test_task\\webcalculator.exe"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = "17678"

def setup_module(module):
    subprocess.run([PATH_TO_WEBCALCULATOR, "start"])
    
def teardown_module(module):
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"])

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
    response = requests.post(url=f"http://{DEFAULT_HOST}:{DEFAULT_PORT}/api/addition", json={"x": x, "y": y})
    responseJSON = json.loads(response.text)
    assert responseJSON["result"] == expected_result

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
    response = requests.post(url=f"http://{DEFAULT_HOST}:{DEFAULT_PORT}/api/multiplication", json={"x": x, "y": y})
    responseJSON = json.loads(response.text)
    assert responseJSON["result"] == expected_result

@pytest.mark.parametrize("x, y, expected_result", [(2147483647, 2147483647, 1),
                                                   (-2147483648, -2147483648, 1),
                                                   (5, -4, -2),
                                                   (-500000, 50000, -10),
                                                   (0, 123123123, 0),
                                                   (0, -987987, 0),
                                                   (159260371, -1, -159260371)])
def test_division(x, y, expected_result):
    response = requests.post(url=f"http://{DEFAULT_HOST}:{DEFAULT_PORT}/api/division", json={"x": x, "y": y})
    responseJSON = json.loads(response.text)
    assert responseJSON["result"] == expected_result

@pytest.mark.parametrize("x, y, expected_result", [(2147483647, 2147483647, 0),
                                                   (-2147483648, -2147483648, 0),
                                                   (10, -3, -2),
                                                   (21, 7, 0),
                                                   (-300000, 30000, 0),
                                                   (0, 123234345, 0),
                                                   (0, -98787, 0),
                                                   (1100, -1, 0)])
def test_remainder(x, y, expected_result):
    response = requests.post(url=f"http://{DEFAULT_HOST}:{DEFAULT_PORT}/api/remainder", json={"x": x, "y": y})
    responseJSON = json.loads(response.text)
    assert responseJSON["result"] == expected_result
