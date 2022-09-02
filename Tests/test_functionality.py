import requests
import subprocess

PATH_TO_WEBCALCULATOR = "C:\\Python\\infotecs_test_task\\webcalculator.exe"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = "17678"

def test_default_host_port():
    subprocess.run([PATH_TO_WEBCALCULATOR, "start"])
    assert requests.get(url=f"http://{DEFAULT_HOST}:{DEFAULT_PORT}/api/state")
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"])

def test_default_port():
    subprocess.run([PATH_TO_WEBCALCULATOR, "start", "127.200.200.200"])
    assert requests.get(url=f"http://127.200.200.200:{DEFAULT_PORT}/api/state")
    subprocess.run([PATH_TO_WEBCALCULATOR, "stop"])
