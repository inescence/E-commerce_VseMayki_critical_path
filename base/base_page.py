import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from metaclasses.meta_locator import MetaLocator


class BasePage(metaclass=MetaLocator):

    _PAGE_URL = "https://www.vsemayki.stage/"
    _PAGE_CATALOG_URL = "https://www.vsemayki.stage/catalog"
    _PAGE_PRODUCT_URL = "https://www.vsemayki.stage/product/"

    _PAGE_CUSTOM_URL = "https://www.vsemayki.ru/custom"
    _PAGE_CART_URL = "https://www.vsemayki.ru/cart"
    _PAGE_FAVORITE_URL = "https://www.vsemayki.ru/favorites"
    _PAGE_VIEWED_URL = "https://www.vsemayki.ru/viewed"

    # first opening
    _SUBMIT_CITY_BUTTON = "//button/span[text()='Все верно']"
    _COOKIES_BUTTON = "//button/span[text()='Принять']"

    # общие кнопки на всех страницах
    _LOGO_BUTTON = "//div[@class='style_logo__1a_-9']"
    _CATALOG_BUTTON = "(//a[text()='Каталог'])[1]"  # div
    _CREATE_DESIGN_BUTTON = "//a[text()='Свой дизайн']"  # div

    _CART_BUTTON = "//div[@class='styles_header__icon_img__2fMCo']/i"
    _FAVORITE_BUTTON = "//div[@class='styles_header__icon_img__2fMCo']/a"
    _VIEWED_BUTTON = "//a[@class='styles_icon__8x6vM']"


    _ADVANCED = "//button[@id='details-button']"
    _ADVANCED_LINK = "//a[@id='proceed-link']"

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 20, 1)

    def open(self):
        # with allure.step(f"Open {self._PAGE_URL} page"):
            self.driver.get(self._PAGE_URL)
            self.wait.until(EC.url_to_be(self._PAGE_URL))

    def submit_city_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self._SUBMIT_CITY_BUTTON))
        button.click()

    def accept_cookies_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self._COOKIES_BUTTON))
        button.click()

#общие кнопки для всех страниц:
    def click_catalog_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self._CATALOG_BUTTON))
        button.click()
        self.wait.until(EC.url_to_be(self._PAGE_CATALOG_URL))


    def click_create_design_button(self):
        button = self.driver.find_element(*self._CREATE_DESIGN_BUTTON)
        button.click()
        self.wait.until(EC.url_to_be(self._PAGE_CUSTOM_URL))


    def click_cart_button(self):
        button = self.driver.find_element(*self._CART_BUTTON)
        button.click()
        self.wait.until(EC.url_to_be(self._PAGE_CART_URL))

    def click_favorite_button(self):
        button = self.driver.find_element(*self._FAVORITE_BUTTON)
        button.click()
        self.wait.until(EC.url_to_be(self._PAGE_FAVORITE_URL))


    def click_viewed_button(self):
        button = self.driver.find_element(*self._VIEWED_BUTTON)
        button.click()
        self.wait.until(EC.url_to_be(self._PAGE_VIEWED_URL))


