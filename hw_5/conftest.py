import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='http://localhost:80')


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    driver = None

    if browser_name == 'chrome':
        driver = webdriver.Chrome()
    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
    elif browser_name == 'edge':
        driver = webdriver.Edge()

    driver.get(url)
    driver.url = url
    yield driver
    driver.quit()
