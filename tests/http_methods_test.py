import subprocess

import pytest
import requests

PATH_TO_WEBCALCULATOR = "C:\\Python\\infotecs_test_task\\resources\\webcalculator.exe"
API_URL = "http://127.0.0.1:17678/api/"
RUN_CONFIG = {"check": True, "stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL}

def setup_module():
    '''Запуск вебкалькулятора.'''
    subprocess.run([PATH_TO_WEBCALCULATOR, "start"], **RUN_CONFIG)

def teardown_module():
    '''Остановка вебкалькулятора.'''
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"], **RUN_CONFIG)

@pytest.mark.parametrize(
    "http_method, validity",
    [('OPTIONS', True),
     ('GET', True),
     ('POST', True),
     ('HEAD', False),
     ('PUT', False),
     ('PATCH', False),
     ('DELETE', False)])
def test_http_method_request_to_state_api_method_response_not_error_status_code(http_method, validity):
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
def test_http_method_request_to_calculate_api_methods_response_not_error_status_code(api_method, http_method, validity):
    response = requests.request(http_method, url=f'{API_URL}{api_method}', timeout=10)
    assert response.ok == validity
