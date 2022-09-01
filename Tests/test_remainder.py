import os
import requests
import json

API_URL = "http://localhost:17678/api/remainder"

def setup_module(module):
    os.system('C:\\Python\\infotecs_test_task\\webcalculator.exe start')
    
def teardown_module(module):
    os.system('C:\\Python\\infotecs_test_task\\webcalculator.exe stop')


def test_max():
    test_dict = {"x": 2147483647, "y": 2147483647}
    response = json.loads(requests.post(url=API_URL, json=test_dict).text)
    assert response["result"] == 0

def test_min():
    test_dict = {"x": -2147483648, "y": -2147483648}
    response = json.loads(requests.post(url=API_URL, json=test_dict).text)
    assert response["result"] == 0

def test_max_min():
    test_dict = {"x": 2147483647, "y": -2147483648 }
    response = json.loads(requests.post(url=API_URL, json=test_dict).text)
    assert response["result"] == -1

def test_min_max():
    test_dict = {"x": -2147483648, "y": 2147483647 }
    response = json.loads(requests.post(url=API_URL, json=test_dict).text)
    assert response["result"] == 2147483646

def test_zero_max():
    test_dict = {"x": 0, "y": 2147483647}
    response = json.loads(requests.post(url=API_URL, json=test_dict).text)
    assert response["result"] == 0

def test_zero_min():
    test_dict = {"x": 0, "y": -2147483648}
    response = json.loads(requests.post(url=API_URL, json=test_dict).text)
    assert response["result"] == 0

def test_max_minus_one():
    test_dict = {"x": 2147483647, "y": -1}
    response = json.loads(requests.post(url=API_URL, json=test_dict).text)
    assert response["result"] == 0