import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from metaclasses.meta_locator import MetaLocator
from faker import Faker

faker = Faker()

class BasePage(metaclass=MetaLocator):

    # общие кнопки на всех страницах
    _LOGO_BUTTON = "//div[@class='style_logo__1a_-9']"
    _CATALOG_BUTTON = "(//a[text()='Каталог'])"
    _CREATE_DESIGN_BUTTON = "//a[text()='Свой дизайн']"

    _CART_BUTTON = "//div[@class='styles_header__icon_img__2fMCo']/i"
    _FAVORITE_BUTTON = "//div[@class='styles_header__icon_img__2fMCo']/a"
    _VIEWED_BUTTON = "//a[@class='styles_icon__8x6vM']"

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 15, 1)

    def open(self):
        with allure.step(f"Open {self._PAGE_URL} page"):
            self.driver.get(self._PAGE_URL)

    def is_opened(self):
        with allure.step(f"PAGE {self._PAGE_URL} is opened"):
            self.wait.until(EC.url_contains(self._PAGE_URL))


    def screenshot(self, screenshot_name=f"screen_{faker.time()}"):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )


#Общие кнопки для всех страниц:
    @allure.step("Click Catalog button")
    def click_catalog_button(self):
        self.wait.until(EC.element_to_be_clickable(self._CATALOG_BUTTON)).click()

    @allure.step("Click Custom button")
    def click_create_design_button(self):
        self.wait.until(EC.element_to_be_clickable(self._CREATE_DESIGN_BUTTON)).click()

    @allure.step("Click Cart button")
    def click_cart_button(self):
        self.wait.until(EC.element_to_be_clickable(self._CART_BUTTON)).click()

    @allure.step("Click Favorite button")
    def click_favorite_button(self):
        self.wait.until(EC.element_to_be_clickable(self._FAVORITE_BUTTON)).click()

    @allure.step("Click Viewed button")
    def click_viewed_button(self):
        self.wait.until(EC.element_to_be_clickable(self._VIEWED_BUTTON)).click()


