from pytest import mark, param
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAdminLoginPage:

    def test_find_form_element(self, browser):
        browser.get(f'{browser.url}/administration/')
        elem = WebDriverWait(browser, 4).until(EC.visibility_of_element_located(
            (By.ID, 'form-login')))
        assert elem.is_displayed()

    def test_find_footer_element(self, browser):
        browser.get(f'{browser.url}/administration/')
        login_button = browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
        assert login_button.is_displayed()

    def test_login_button(self, browser):
        browser.get(f'{browser.url}/administration/')
        elem = WebDriverWait(browser, 4).until(EC.visibility_of_element_located(
            (By.TAG_NAME, 'footer')))
        assert elem.is_displayed()

    @mark.parametrize('selector', [
            param('//input[@type="text"]', id='Username field is enabled'),
            param('//input[@type="password"]', id='Password field is enabled'),
    ])
    def test_form_fields(self, browser, selector):
        browser.get(f'{browser.url}/administration/')
        field = browser.find_element(By.XPATH, selector)
        assert field.is_enabled()
