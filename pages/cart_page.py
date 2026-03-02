from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
from data.links import Links

class CartPage(BasePage):

    _PAGE_URL = Links.CART_PAGE

    _PRODUCTS_IN_CART = "//section[contains(@class, 'autotest-cart-item')]"
    _CHECKBOX_SELECT_ALL = "//input[@type='checkbox']"
    _EDITING_BUTTON = "//input[@type='number']"
    _PLUS_BUTTON = "//button[@type='button' and text()='+']"
    _SIZE_BUTTON = "//span[@class='select-text--3pSXN']"
    _COLOR_BUTTON = "//div[@class='styles_cartItem__39-wL']"
    _DEL_BUTTON = "//span[@title='Удалить товар']"
    _FAVORITE_BUTTON = "//span[@title='избранное']"
    _ADD_GIFT_WRAPPER_BUTTON = "//button[@id='autotest-cart-open-gift-wrap-modal']"
    _CHOOSE_GIFT_WRAPPER_BUTTON = "(//button/span[text()='Добавить в корзину'])[2]"

    _CHECKOUT_BUTTON = "//a[@id='autotest-cart-go-to-checkout']"

    @allure.step("Check products in cart")
    def check_products(self):
        self.wait.until(EC.visibility_of_element_located(self._PRODUCTS_IN_CART))

    @allure.step("Click plus button")
    def click_plus_button(self):
        self.wait.until(EC.element_to_be_clickable(self._PLUS_BUTTON)).click()

    @allure.step("Click favorite button")
    def click_favorite_button(self):
        favorite = self.wait.until(EC.element_to_be_clickable(self._FAVORITE_BUTTON))
        favorite.click()

    @allure.step("Add gift wrapping button")
    def add_gift_wrapping_button(self):
        add_button = self.wait.until(EC.element_to_be_clickable(self._ADD_GIFT_WRAPPER_BUTTON))
        add_button.click()

    @allure.step("Choose gift button")
    def choose_gift_button(self):
        choose_gift = self.wait.until(EC.element_to_be_clickable(self._CHOOSE_GIFT_WRAPPER_BUTTON))
        choose_gift.click()

    @allure.step("Click delete button")
    def delete_button(self):
        delete = self.wait.until(EC.element_to_be_clickable(self._DEL_BUTTON))
        delete.click()

    @allure.step("Click checkout button")
    def click_checkout_button(self):
        go_to_order = self.wait.until(EC.visibility_of_element_located(self._CHECKOUT_BUTTON))
        go_to_order.click()