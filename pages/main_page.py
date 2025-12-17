from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure

class MainPage(BasePage):

    _PAGE_URL = "https://www.vsemayki.stage/"
    _PAGE_CATALOG_URL = "https://www.vsemayki.stage/catalog"
    _PAGE_PRODUCT_URL = "https://www.vsemayki.stage/product/"

    _QUICK_VIEW_PRODUCT_CARD = "(//div[contains(@class, 'autotest-quickview-open-button')])[9]"
    _PRODUCT_CARD = "(//div[contains(@class, 'autotest-product-image')])[7]"
    _SIZE_BUTTON = "//a[contains(@class, 'autotest-product-size-variant')]"

    _CHECK_3D_BUTTON = "//span[@class='styles_content__28yl7']"

    _ADD_TO_CART = "//a[@id='autotest-product-card-add-to-cart']"
    _BUY_BUTTON = "//button[@id='autotest-product-card-go-to-cart']"

    _FAVORITE_BUTTON = "//div[@id='autotest-product-card-add-to-favorites']"


    def catalog_is_opened(self):
        self.driver.get(self._PAGE_CATALOG_URL)
        self.wait.until(EC.url_to_be(self._PAGE_CATALOG_URL))

    def click_product(self):
        with allure.step("Открыть карточку товара"):
            product = self.wait.until(EC.visibility_of_element_located(self._PRODUCT_CARD))
            product.click()
            self.wait.until(EC.url_contains(self._PAGE_PRODUCT_URL))


    def open_quick_view(self):
        self.driver.find_element(*self._QUICK_VIEW_PRODUCT_CARD).click()
        self.wait.until(EC.element_to_be_clickable(self._ADD_TO_CART)).click()
        self.wait.until(EC.element_to_be_clickable(self._BUY_BUTTON)).click()
        self.wait.until(EC.url_to_be(self._PAGE_CART_URL))

    def choose_size(self):
        with allure.step("Выбрать размер"):
            choose_size = self.wait.until(EC.element_to_be_clickable(self._SIZE_BUTTON))
            choose_size.click()


    # def add_favorite(self):
    #     favorite = self.wait.until(EC.element_to_be_clickable(self._FAVORITE_BUTTON))
    #     favorite.click()

    def add_to_cart(self):
        add_to_cart = self.wait.until(EC.element_to_be_clickable(self._ADD_TO_CART))
        # add_to_cart = self.driver.find_element(*self._ADD_TO_CART)
        add_to_cart.click()

    def click_buy_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self._BUY_BUTTON))
        button.click()
