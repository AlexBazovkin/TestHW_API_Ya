import requests
headers = {"Authorization": "SuperSecretPasswordToken"}


def create_folder():
    responce_status = (requests.put('https://cloud-api.yandex.net/v1/disk/resources?path=%2Ftest_folder', headers=headers)).status_code
    return responce_status
