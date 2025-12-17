from base.base_page import BasePage
import time
from selenium.webdriver.support import expected_conditions as EC
import allure

class CartPage(BasePage):

    _PAGE_CART_URL = "https://www.vsemayki.stage/cart"

    _PRODUCTS_IN_CART = "//section[contains(@class, 'autotest-cart-item')]"
    _CHECKBOX_SELECT_ALL = "//input[@type='checkbox']"

    _PLUS_BUTTON = "//button[@type='button']" # and text()='+'
    # _SIZE_BUTTON = "//span[@class='select-text--3pSXN']"
    # _COLOR_BUTTON = "//div[@class='styles_cartItem__39-wL']"
    _DEL_BUTTON = "//span[@title='Удалить товар']"
    # _FAVORITE_BUTTON = "//span[@title='избранное']"
    # _ADD_GIFT_WRAPPER_BUTTON = "//button[@id='autotest-cart-open-gift-wrap-modal']"
    # _SUBMIT_GIFT_WRAPPER_BUTTON = "" #//span[@data-autotest='component-2' and text()='Добавить в корзину']"

    _CHECKOUT_BUTTON = "//a[@id='autotest-cart-go-to-checkout']"


    def cart_is_opened(self):
        self.wait.until(EC.url_to_be(self._PAGE_CART_URL))


    def check_products(self):
        check_prods = self.wait.until(EC.visibility_of_element_located(self._PRODUCTS_IN_CART))
        assert check_prods is not None
        time.sleep(3)


#допилить проверку чекбокса по атрибуту checked
    # def check_select_all(self):
    #     checkbox_on = self.wait.until(EC.visibility_of_element_located(self._CHECKBOX_SELECT_ALL))
        # assert checkbox_on is checked

    def click_plus_button(self):
        plus = self.wait.until(EC.element_to_be_clickable(self._PLUS_BUTTON))
        plus.click()

    # def click_favorite_button(self):
    #     favorite = self.wait.until(EC.element_to_be_clickable(self._FAVORITE_BUTTON)).click()
    #     favorite.click()
    #
    # def add_gift_wrapping(self):
    #     add_button = self.driver.find_element(*self._ADD_GIFT_WRAPPER_BUTTON)
    #     add_button.click()
    #
    # def submit_gift_button(self):
    #     submit = self.wait.until(EC.element_to_be_clickable(self._SUBMIT_GIFT_WRAPPER_BUTTON))
    #     submit.click()


    def delete_button(self):
        delete = self.wait.until(EC.element_to_be_clickable(self._DEL_BUTTON))
        delete.click()

    def click_checkout_button(self):
        go_to_order = self.wait.until(EC.visibility_of_element_located(self._CHECKOUT_BUTTON))
        go_to_order.click()
