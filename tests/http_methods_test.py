import subprocess

import requests

PATH_TO_WEBCALCULATOR = "C:\\Python\\infotecs_test_task\\resorces\\webcalculator.exe"

def setup_module():
    '''Запуск вебкалькулятора.'''
    subprocess.run([PATH_TO_WEBCALCULATOR, "start"], check=True)

def teardown_module():
    '''Остановка вебкалькулятора.'''
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"], check=True)

class TestGetApiFunctionByHttpMethods:
    def test_OptionsRequest_ReturnOkStatusCode(self):
        '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
        response = requests.options(
            url='http://127.0.0.1:17678/api/state',
            timeout=1.5)
        assert response.ok

    def test_GetRequest_ReturnOkStatusCode(self):
        '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
        response = requests.get(
            url='http://127.0.0.1:17678/api/state',
            timeout=1.5)
        assert response.ok

    def test_PostRequest_ReturnNotOkStatusCode(self):
        '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
        response = requests.post(
            url='http://127.0.0.1:17678/api/state',
            timeout=1.5)
        assert not response.ok

    def test_HeadRequest_ReturnNotOkStatusCode(self):
        '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
        response = requests.head(
            url='http://127.0.0.1:17678/api/state',
            timeout=1.5)
        assert not response.ok

    def test_PutRequest_ReturnNotOkStatusCode(self):
        '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
        response = requests.put(
            url='http://127.0.0.1:17678/api/state',
            timeout=1.5)
        assert not response.ok

    def test_PatchRequest_ReturnNotOkStatusCode(self):
        '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
        response = requests.patch(
            url='http://127.0.0.1:17678/api/state',
            timeout=1.5)
        assert not response.ok

    def test_DeleteRequest_ReturnNotOkStatusCode(self):
        '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
        response = requests.delete(
            url='http://127.0.0.1:17678/api/state',
            timeout=1.5)
        assert not response.ok



class TestPostApiFunctionByHttpMethods:
    def test_OptionsRequest_ReturnOkStatusCode(self):
        '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
        response = requests.options(
            url='http://127.0.0.1:17678/api/addition',
            timeout=1.5)
        assert response.ok

    def test_GetRequest_ReturnNotOkStatusCode(self):
        '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
        response = requests.get(
            url='http://127.0.0.1:17678/api/addition',
            timeout=1.5)
        assert not response.ok

    def test_PostRequest_ReturnOkStatusCode(self):
        '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
        response = requests.post(
            url='http://127.0.0.1:17678/api/addition',
            timeout=1.5)
        assert response.ok

    def test_HeadRequest_ReturnNotOkStatusCode(self):
        '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
        response = requests.head(
            url='http://127.0.0.1:17678/api/addition',
            timeout=1.5)
        assert not response.ok

    def test_PutRequest_ReturnNotOkStatusCode(self):
        '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
        response = requests.put(
            url='http://127.0.0.1:17678/api/addition',
            timeout=1.5)
        assert not response.ok

    def test_PatchRequest_ReturnNotOkStatusCode(self):
        '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
        response = requests.patch(
            url='http://127.0.0.1:17678/api/addition',
            timeout=1.5)
        assert not response.ok

    def test_DeleteRequest_ReturnNotOkStatusCode(self):
        '''Допустимы следующие типы запросов: POST/GET/OPTIONS'''
        response = requests.delete(
            url='http://127.0.0.1:17678/api/addition',
            timeout=1.5)
        assert not response.ok
