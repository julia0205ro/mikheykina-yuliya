import requests
import pytest


@pytest.fixture
def url(request):
    return request.config.getoption('--url')


@pytest.fixture
def status_code(request):
    return request.config.getoption('--status_code')


def test_ya_api(url, status_code):
    response = requests.get(url=url)
    assert response.status_code == status_code
