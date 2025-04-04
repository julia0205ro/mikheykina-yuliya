from pytest import mark, param
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException


class TestCatalog:

    def test_compare_button(self, browser):
        browser.get(f'{browser.url}/en-gb/catalog/laptop-notebook')
        compare_button = WebDriverWait(browser, 4).until(EC.visibility_of_element_located(
            (By.ID, 'compare-total')))
        assert compare_button.is_enabled()

    @mark.parametrize('selector', [
        param('//select[@id="input-sort"]', id='Sort field is_enabled'),
        param('//select[@id="input-limit"]', id='Limits is_enabled'),
    ])
    def test_fields(self, browser, selector):
        browser.get(f'{browser.url}/en-gb/catalog/laptop-notebook')
        field = WebDriverWait(browser, 4).until(EC.visibility_of_element_located(
            (By.XPATH, selector)))
        assert field.is_enabled()

    def test_cart_button(self, browser):
        browser.get(f'{browser.url}/en-gb/catalog/laptop-notebook')
        cart_button = WebDriverWait(browser, 4).until(EC.visibility_of_element_located(
            (By.XPATH, '//button[text()=" 0 item(s) - $0.00"]')))
        assert cart_button.is_displayed()

    @mark.parametrize('width, height, visibility', [
        param(900, 800, True, id='Category button is displayed at a screen size of 900x800'),
        param(1500, 800, False, id='Category button is not displayed at a screen size of 1500x800'),
    ])
    def test_category_button(self, browser, width, height, visibility):
        browser.get(f'{browser.url}/en-gb/catalog/laptop-notebook')
        browser.set_window_size(width, height)
        try:
            element = WebDriverWait(browser, 4).until(EC.visibility_of_element_located(
                (By.XPATH, '//button[@class="navbar-toggler"]')))
            is_visible = element.is_displayed()
        except TimeoutException:
            is_visible = False
        assert is_visible == visibility
