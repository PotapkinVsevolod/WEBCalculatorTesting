import subprocess

import requests

PATH_TO_WEBCALCULATOR = "C:\\Python\\infotecs_test_task\\webcalculator.exe"

def test_start_webcalulator_on_specified_host_port_ok():
    host = "127.200.200.200"
    port = "5346"

    subprocess.run([PATH_TO_WEBCALCULATOR, "start", host, port], check=True)
    response = requests.get(url=f"http://{host}:5346/api/state", timeout=3)
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"], check=True)

    assert response.ok

def test_start_webcalulator_on_default_port_ok():
    host = "127.200.200.200"

    subprocess.run([PATH_TO_WEBCALCULATOR, "start", host], check=True)
    response = requests.get(url=f"http://{host}:17678/api/state", timeout=3)
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"], check=True)

    assert response.ok

def test_start_webcalulator_on_default_host_port_ok():

    subprocess.run([PATH_TO_WEBCALCULATOR, "start"], check=True)
    response = requests.get(url="http://127.0.0.1:17678/api/state", timeout=3)
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"], check=True)

    assert response.ok

def test_stop_webcalulator_ok():

    subprocess.run([PATH_TO_WEBCALCULATOR, "start"], check=True)
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"], check=True)

    try:
        requests.get(url="http://127.0.0.1:17678/api/state", timeout=3)
        assert False
    except requests.ConnectionError:
        assert True


def test_restart_webcalulator_ok():

    subprocess.run([PATH_TO_WEBCALCULATOR, "start"], check=True)
    subprocess.run([PATH_TO_WEBCALCULATOR, "restart"], check=True)
    response = requests.get(url="http://127.0.0.1:17678/api/state", timeout=3)
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"], check=True)

    assert response.ok
