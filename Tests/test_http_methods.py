import subprocess

import requests

PATH_TO_WEBCALCULATOR = "C:\\Python\\infotecs_test_task\\webcalculator.exe"

def setup_module():
    '''Запуск вебкалькулятора.'''
    subprocess.run([PATH_TO_WEBCALCULATOR, "start"], check=True)

def teardown_module():
    '''Остановка вебкалькулятора.'''
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"], check=True)

def test_option_to_get_api_function():
    '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
    response = requests.options(
    url='http://127.0.0.1:17678/api/state',
    timeout=1.5)
    assert response.ok

def test_get_method_to_get_api_function_ok():
    '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
    response = requests.get(
    url='http://127.0.0.1:17678/api/state',
    timeout=1.5)
    assert response.ok

def test_post_to_get_api_function_not_ok():
    '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
    response = requests.post(
    url='http://127.0.0.1:17678/api/state',
    timeout=1.5)
    assert not response.ok

def test_head_to_get_api_function_not_ok():
    '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
    response = requests.head(
    url='http://127.0.0.1:17678/api/state',
    timeout=1.5)
    assert not response.ok

def test_put_to_get_api_function_not_ok():
    '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
    response = requests.put(
    url='http://127.0.0.1:17678/api/state',
    timeout=1.5)
    assert not response.ok

def test_patch_to_get_api_function_not_ok():
    '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
    response = requests.patch(
    url='http://127.0.0.1:17678/api/state',
    timeout=1.5)
    assert not response.ok

def test_delete_to_get_api_function_not_ok():
    '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
    response = requests.delete(
    url='http://127.0.0.1:17678/api/state',
    timeout=1.5)
    assert not response.ok

def test_option_to_post_api_function_ok():
    '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
    response = requests.options(
    url='http://127.0.0.1:17678/api/addition',
    timeout=1.5)
    assert response.ok

def test_get_method_to_post_api_function_not_ok():
    '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
    response = requests.get(
    url='http://127.0.0.1:17678/api/addition',
    timeout=1.5)
    assert not response.ok

def test_post_to_post_api_function_ok():
    '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
    response = requests.post(
    url='http://127.0.0.1:17678/api/addition',
    timeout=1.5)
    assert response.ok

def test_head_to_post_api_function_not_ok():
    '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
    response = requests.head(
    url='http://127.0.0.1:17678/api/addition',
    timeout=1.5)
    assert not response.ok

def test_put_to_post_api_function_not_ok():
    '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
    response = requests.put(
    url='http://127.0.0.1:17678/api/addition',
    timeout=1.5)
    assert not response.ok

def test_patch_to_post_api_function_not_ok():
    '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
    response = requests.patch(
    url='http://127.0.0.1:17678/api/addition',
    timeout=1.5)
    assert not response.ok

def test_delete_to_post_api_function_not_ok():
    '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
    response = requests.delete(
    url='http://127.0.0.1:17678/api/addition',
    timeout=1.5)
    assert not response.ok