import pytest
import requests
from main import create_folder
from main import headers


def test_create_folder():
    folder_availability_check = requests.get('https://cloud-api.yandex.net/v1/disk/resources?path=%2Ftest_folder', headers=headers)
    if create_folder() != 201 and folder_availability_check.status_code != 200:
        pytest.fail(reason='Folder was not created or already exists.')
