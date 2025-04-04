from pytest import mark, param
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestUserRegistrationPage:

    @mark.parametrize('selector', [
        param('input-firstname', id='First name field is enabled'),
        param('input-lastname', id='Last name field is enabled'),
    ])
    def test_form_fields(self, browser, selector):
        browser.get(f'{browser.url}/index.php?route=account/register')
        field = WebDriverWait(browser, 4).until(EC.visibility_of_element_located(
            (By.ID, selector)))
        assert field.is_enabled()

    def test_find_label(self, browser):
        browser.get(f'{browser.url}/index.php?route=account/register')
        elem = WebDriverWait(browser, 4).until(EC.visibility_of_element_located(
            (By.XPATH, '//legend[text()="Your Password"]')))
        assert elem.is_displayed()

    def test_find_button(self, browser):
        browser.get(f'{browser.url}/index.php?route=account/register')
        button = WebDriverWait(browser, 4).until(EC.visibility_of_element_located(
            (By.XPATH, '//button[@class="btn btn-primary"]')))
        assert button.is_displayed()

    def test_find_checkbox(self, browser):
        browser.get(f'{browser.url}/index.php?route=account/register')
        checkbox = WebDriverWait(browser, 4).until(EC.visibility_of_element_located(
            (By.NAME, 'agree')))
        assert checkbox.is_enabled()
