import subprocess

import pytest
import requests

PATH_TO_WEBCALCULATOR = "C:\\Python\\infotecs_test_task\\resources\\webcalculator.exe"
API_URL = "http://127.0.0.1:17678/api/"

def setup_module():
    '''Запуск вебкалькулятора.'''
    subprocess.run(["C:\\Python\\infotecs_test_task\\resources\\webcalculator.exe", "start"], check=True)


def teardown_module():
    '''Остановка вебкалькулятора.'''
    subprocess.run(["C:\\Python\\infotecs_test_task\\resources\\webcalculator.exe", "stop"], check=True)

@pytest.mark.parametrize(
    "http_method, validity",
    [('OPTIONS', True),
     ('GET', True),
     ('POST', True),
     ('HEAD', False),
     ('PUT', False),
     ('PATCH', False),
     ('DELETE', False)])
def test_HttpMethodToStateApiMethodsRequest(http_method, validity):
    response = requests.request(http_method, url=f'{API_URL}state', timeout=10)
    assert response.ok == validity


@pytest.mark.parametrize("api_method", ["addition", "multiplication", "division", "remainder"])
@pytest.mark.parametrize(
    "http_method, validity",
    [("OPTIONS", True),
     ("GET", True),
     ("POST", True),
     ("HEAD", False),
     ("PUT", False),
     ("PATCH", False),
     ("DELETE", False)])
def test_HttpMethodsToCalculateApiMethodRequests(api_method, http_method, validity):
    response = requests.request(http_method, url=f'{API_URL}{api_method}', timeout=10)
    assert response.ok == validity
