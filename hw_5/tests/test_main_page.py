from pytest import mark, param
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException


class TestMainPage:

    @mark.parametrize('selector', [
        param('//div[@id="search"]//button[@type="button"]', id='Search button is displayed'),
        param('//div[@id="header-cart"]//button[@type="button"]', id='Items cart button is displayed'),
    ])
    def test_buttons(self, browser, selector):
        browser.get(browser.url)
        button = browser.find_element(By.XPATH, selector)
        assert button.is_displayed()

    def test_search_field(self, browser):
        browser.get(browser.url)
        button = browser.find_element(By.NAME, 'search')
        assert button.is_enabled()

    @mark.parametrize('selector', [
        param('//img[@alt="Starbucks"]', id='Starbucks logo is displayed'),
        param('//img[@alt="iPhone 6"]', id='iPhone 6 photo is displayed'),
    ])
    def test_carousel_elems(self, browser, selector):
        """Выставлен долгий таймаут и реализована обработка ошибок,
        так как элементы находятся в карусели
        и она не всегда успевают провернуться"""

        browser.get(browser.url)
        error_text = 'Элемент не успел прогрузиться'

        try:
            elem = WebDriverWait(browser, 20).until(EC.visibility_of_element_located(
                (By.XPATH, selector)))
        except TimeoutException as e:
            print(f'{error_text}: {e}')
            elem = None
        assert elem.is_displayed()
