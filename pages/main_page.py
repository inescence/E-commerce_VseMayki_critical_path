from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
from data.links import Links

class MainPage(BasePage):

    _PAGE_URL = Links.HOST

    # first opening
    _SUBMIT_CITY_BUTTON = "//button/span[text()='Все верно']"
    _COOKIES_BUTTON = "//button/span[text()='Принять']"

    _QUICK_VIEW_PRODUCT_CARD = "(//div[contains(@class, 'autotest-quickview-open-button')])[9]"
    _PRODUCT_CARD = "(//div[contains(@class, 'autotest-product-image')])[6]"

    @allure.step("Submit city button")
    def submit_city_button(self):
        self.wait.until(EC.element_to_be_clickable(self._SUBMIT_CITY_BUTTON)).click()

    @allure.step("Accept cookies button")
    def accept_cookies_button(self):
        self.wait.until(EC.element_to_be_clickable(self._COOKIES_BUTTON)).click()

    @allure.step("Click product card")
    def click_product_card(self):
        with allure.step("Открыть карточку товара"):
            self.wait.until(EC.visibility_of_element_located(self._PRODUCT_CARD)).click()

    @allure.step("Open quick view")
    def open_quick_view(self):
        self.wait.until(EC.element_to_be_clickable(self._QUICK_VIEW_PRODUCT_CARD)).click()