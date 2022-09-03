import subprocess
import requests


PATH_TO_WEBCALCULATOR = "C:\\Python\\infotecs_test_task\\webcalculator.exe"


def test_start():
    subprocess.run([PATH_TO_WEBCALCULATOR, "start", "127.200.200.200", "5346"], check=True)
    assert requests.get(url="http://127.200.200.200:5346/api/state", timeout=3)
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"], check=True)


def test_start_on_default_port():
    subprocess.run([PATH_TO_WEBCALCULATOR, "start", "127.200.200.200"], check=True)
    assert requests.get(url="http://127.200.200.200:17678/api/state", timeout=3)
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"], check=True)


def test_start_on_default_host_port():
    subprocess.run([PATH_TO_WEBCALCULATOR, "start"], check=True)
    assert requests.get(url="http://127.0.0.1:17678/api/state", timeout=3)
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"], check=True)


def test_stop():
    subprocess.run([PATH_TO_WEBCALCULATOR, "start"], check=True)
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"], check=True)
    try:
        requests.get(url="http://127.0.0.1:17678/api/state", timeout=3)
        assert False
    except requests.ConnectionError:
        assert True


def test_restart():
    subprocess.run([PATH_TO_WEBCALCULATOR, "start"], check=True)
    subprocess.run([PATH_TO_WEBCALCULATOR, "restart"], check=True)
    assert requests.get(url="http://127.0.0.1:17678/api/state", timeout=1.5)
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"], check=True)
