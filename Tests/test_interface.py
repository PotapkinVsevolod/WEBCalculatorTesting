import subprocess
import requests
import json

PATH_TO_WEBCALCULATOR = "C:\\Python\\infotecs_test_task\\webcalculator.exe"
TEST_DICT = {"x": 1, "y": 2}
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = "17678"

def setup_module(module):
    subprocess.run([PATH_TO_WEBCALCULATOR, "start"])
    
def teardown_module(module):
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"])

def test_state():
    response = requests.get(f'http://{DEFAULT_HOST}:{DEFAULT_PORT}/api/state')
    responseJSON = json.loads(response.text)
    assert type(responseJSON) == dict
    assert len(responseJSON) == 2
    assert responseJSON["statusCode"] == 0
    assert responseJSON["state"] == "OK"

def test_addition():
    response = requests.post(f'http://{DEFAULT_HOST}:{DEFAULT_PORT}/api/addition', json=TEST_DICT)
    responseJSON = json.loads(response.text)
    assert type(responseJSON) == dict
    assert len(responseJSON) == 2
    assert responseJSON["statusCode"] == 0
    assert type(responseJSON["result"]) == int

def test_multiplication():
    response = requests.post(f'http://{DEFAULT_HOST}:{DEFAULT_PORT}/api/multiplication', json=TEST_DICT)
    responseJSON = json.loads(response.text)
    assert type(responseJSON) == dict
    assert len(responseJSON) == 2
    assert responseJSON["statusCode"] == 0
    assert type(responseJSON["result"]) == int

def test_division():
    response = requests.post(f'http://{DEFAULT_HOST}:{DEFAULT_PORT}/api/division', json=TEST_DICT)
    responseJSON = json.loads(response.text)
    assert type(responseJSON) == dict
    assert len(responseJSON) == 2
    assert responseJSON["statusCode"] == 0
    assert type(responseJSON["result"]) == int

def test_remainder():
    response = requests.post(f'http://{DEFAULT_HOST}:{DEFAULT_PORT}/api/remainder', json=TEST_DICT)
    responseJSON = json.loads(response.text)
    assert type(responseJSON) == dict
    assert len(responseJSON) == 2
    assert responseJSON["statusCode"] == 0
    assert type(responseJSON["result"]) == int
