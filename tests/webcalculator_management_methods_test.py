'''
Проверить с помощью тестов функционал управления приложением (раздел Управление приложением):
    возможность смены адреса хоста/порта; значения по умолчанию;
    возможность остановки / перезапуска приложения

Запуск приложения осуществляется с помощью команды start с указанием
дополнительных аргументов host и port.

В случае если указан только адрес хоста, будет использован порт по умолчанию (17678).
Если адрес хоста так же не указан будет использован адрес по умолчанию (127.0.0.1)

Пример запуска на локальной машине: webcalculator.exe start localhost 5413

Остановка приложения осуществляется командной stop.

Команда restart осуществляет перезапуск приложения.

После выполнения команды приложение продолжает работать на том же адресе и порту,
что и до перезапуска.

После того, как приложение запущено (см. Управление приложением), клиент может обратится
к нему по средствам HTTP-API по адресу и порту, указанному при запуске приложения
'''
import subprocess

import requests
import pytest

PATH_TO_WEBCALCULATOR = "C:\\Python\\infotecs_test_task\\resources\\webcalculator.exe"
RUN_CONFIG = {"check": True, "stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL}

def test_get_request_without_start_webcalculator_raise_connection_error():
    '''В случае если указан только адрес хоста, будет использован порт по умолчанию (17678).
    Если адрес хоста так же не указан будет использован адрес по умолчанию (127.0.0.1)'''
    with pytest.raises(requests.ConnectionError):
        requests.get(url="http://127.0.0.1:17678/api/state", timeout=10)

def test_start_webcalulator_on_default_host_port_get_request_response_not_error_status_code():  
    '''В случае если указан только адрес хоста, будет использован порт по умолчанию (17678).
       Если адрес хоста так же не указан будет использован адрес по умолчанию (127.0.0.1)'''
    subprocess.run([PATH_TO_WEBCALCULATOR, "start"], **RUN_CONFIG)
    response = requests.get(url="http://127.0.0.1:17678/api/state", timeout=10)
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"], **RUN_CONFIG)
    assert response.ok

def test_start_and_stop_webcalculator_get_request_raise_connection_error():
    '''Остановка приложения осуществляется командной stop.'''
    subprocess.run([PATH_TO_WEBCALCULATOR, "start"], **RUN_CONFIG)
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"], **RUN_CONFIG)
    with pytest.raises(requests.ConnectionError):
        requests.get(url="http://127.0.0.1:17678/api/state", timeout=10)

def test_start_webcalculator_on_specified_host_port_get_request_response_not_error_status_code():
    '''Запуск приложения осуществляется с помощью команды start с указанием
       дополнительных аргументов host и port.'''
    subprocess.run([PATH_TO_WEBCALCULATOR, "start", "127.200.200.200", "5346"], **RUN_CONFIG)
    response = requests.get(url="http://127.200.200.200:5346/api/state", timeout=10)
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"], **RUN_CONFIG)
    assert response.ok

def test_start_webcalulator_on_default_port_get_request_response_not_error_status_code():
    '''В случае если указан только адрес хоста, будет использован порт по умолчанию (17678).'''
    subprocess.run([PATH_TO_WEBCALCULATOR, "start", "127.200.200.200"], **RUN_CONFIG)
    response = requests.get(url="http://127.200.200.200:17678/api/state", timeout=10)
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"], **RUN_CONFIG)
    assert response.ok


def test_restart_webcalulator_get_request_response_not_error_status_code():
    '''После выполнения команды приложение продолжает работать на том же адресе и порту,
       что и до перезапуска.'''
    subprocess.run([PATH_TO_WEBCALCULATOR, "start"], **RUN_CONFIG)
    subprocess.run([PATH_TO_WEBCALCULATOR, "restart"], **RUN_CONFIG)
    response = requests.get(url="http://127.0.0.1:17678/api/state", timeout=10)
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"], **RUN_CONFIG)
    assert response.ok
