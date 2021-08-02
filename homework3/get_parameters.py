import requests
from conftest import base_url, status_code


def test_resp(base_url, status_code):
    assert requests.get(base_url).status_code.__str__() == status_code
