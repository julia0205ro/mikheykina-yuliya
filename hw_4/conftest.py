import requests
import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--dog-url',
        default='https://dog.ceo/api'
    )

    parser.addoption(
        '--dog-method',
        default='get'
    )

    parser.addoption(
        '--brewery-url',
        default='https://api.openbrewerydb.org/v1/breweries'
    )

    parser.addoption(
        '--brewery-method',
        default='get'
    )

    parser.addoption(
        '--jsonplaceholder-url',
        default='https://jsonplaceholder.typicode.com'
    )

    parser.addoption(
        '--jsonplaceholder-method',
        default='get',
        choices=['get', 'post', 'put', 'patch', 'delete'],
    )


@pytest.fixture
def base_dog_url(request):
    return request.config.getoption('--dog-url')


@pytest.fixture
def request_dog_method(request):
    return getattr(requests, request.config.getoption('--dog-method'))


@pytest.fixture
def base_brewery_url(request):
    return request.config.getoption('--brewery-url')


@pytest.fixture
def request_brewery_method(request):
    return getattr(requests, request.config.getoption('--brewery-method'))


@pytest.fixture
def base_jsonplaceholder_url(request):
    return request.config.getoption('--jsonplaceholder-url')


@pytest.fixture
def request_jsonplaceholder_method(request):
    return getattr(requests, request.config.getoption('--jsonplaceholder-method'))
