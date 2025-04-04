from pytest import mark, param
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestProductCart:

    @mark.parametrize('selector', [
        param('//button[@id="button-cart"]', id='"Add to Cart" button is displayed'),
        param('//button[@formaction="http://localhost/en-gb?route=account/wishlist.add"]',
              id='"Like" button is displayed'),
    ])
    def test_buttons(self, browser, selector):
        browser.get(f'{browser.url}/en-gb/product/macbook')
        button = browser.find_element(By.XPATH, selector)
        assert button.is_displayed()

    def test_image_is_enabled(self, browser):
        browser.get(f'{browser.url}/en-gb/product/macbook')
        img = browser.find_element(By.XPATH,
                                   '//img[@src="http://localhost/image/cache/catalog/demo/macbook_2-74x74.jpg"]')
        assert img.is_enabled()

    @mark.parametrize('selector', [
        param('Apple', id='Link Apple is enabled'),
        param('Privacy', id='Link Privacy Policy is enabled'),
    ])
    def test_links_is_enabled(self, browser, selector):
        browser.get(f'{browser.url}/en-gb/product/macbook')

        link = WebDriverWait(browser, 4).until(EC.visibility_of_element_located(
            (By.LINK_TEXT, 'Apple')))
        assert link.is_enabled()
