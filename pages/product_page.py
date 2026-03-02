from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
from data.links import Links

class ProductPage(BasePage):

    _PAGE_URL = Links.PRODUCT_PAGE

    _SIZE_BUTTON = "//a[contains(@class, 'autotest-product-size-variant')]"
    _ADD_TO_CART = "//a[@id='autotest-product-card-add-to-cart']"
    _GO_TO_CART_BUTTON = "//button[@id='autotest-product-card-go-to-cart']"
    _FAVORITE_BUTTON = "//div[@id='autotest-product-card-add-to-favorites']"

    @allure.step("Choose size")
    def choose_size(self):
        choose_size = self.wait.until(EC.element_to_be_clickable(self._SIZE_BUTTON))
        choose_size.click()

    @allure.step("Add favorite")
    def add_favorite(self):
        favorite = self.wait.until(EC.element_to_be_clickable(self._FAVORITE_BUTTON))
        favorite.click()

    @allure.step("Add to cart")
    def add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self._ADD_TO_CART)).click()
        self.wait.until(EC.text_to_be_present_in_element(self._GO_TO_CART_BUTTON, "Перейти в корзину"))

    @allure.step("Go to cart")
    def go_to_cart(self):
        go_to_cart = self.wait.until(EC.element_to_be_clickable(self._GO_TO_CART_BUTTON))
        go_to_cart.click()
        self.wait.until(EC.url_changes(self._PAGE_URL))



