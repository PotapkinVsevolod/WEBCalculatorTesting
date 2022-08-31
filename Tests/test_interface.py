import os
import requests
import json

TEST_DICT = {"y": 1, "x": 1}

def setup_module(module):
    os.system('C:\\Python\\webcalculator.exe start')
    
def teardown_module(module):
    os.system('C:\\Python\\webcalculator.exe stop')

def test_state():
    response = json.loads(requests.get('http://localhost:17678/api/state').text)
    assert type(response) == dict
    assert len(response) == 2
    assert response["statusCode"] == 0
    assert response["state"] == "OK"

def test_addition():
    response = json.loads(requests.post('http://localhost:17678/api/addition', json=TEST_DICT).text)
    assert type(response) == dict
    assert len(response) == 2
    assert response["statusCode"] == 0
    assert type(response["result"]) == int

def test_multiplication():
    response = json.loads(requests.post('http://localhost:17678/api/multiplication', json=TEST_DICT).text)
    assert type(response) == dict
    assert len(response) == 2
    assert response["statusCode"] == 0
    assert type(response["result"]) == int

def test_division():
    response = json.loads(requests.post('http://localhost:17678/api/division', json=TEST_DICT).text)
    assert type(response) == dict
    assert len(response) == 2
    assert response["statusCode"] == 0
    assert type(response["result"]) == int

def test_remainder():
    response = json.loads(requests.post('http://localhost:17678/api/remainder', json=TEST_DICT).text)
    assert type(response) == dict
    assert len(response) == 2
    assert response["statusCode"] == 0
    assert type(response["result"]) == int
