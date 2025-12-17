import time

from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage(BasePage):

    _PAGE_CHECKOUT_URL = "https://www.vsemayki.stage/cart/delivery"

    _PAYMENT_URL = "https://www.vsemayki.stage/newpayment?order"

    _DELIVERY_URL = "https://www.vsemayki.stage/cart/delivery#map"

    _NAME_FIELD = "//input[@autocomplete='given-name']"
    _SURNAME_FIELD = "//input[@autocomplete='family-name']"
    _NUMBER_FIELD = "//input[@autocomplete='tel']"
    _EMAIL_FIELD = "//input[@autocomplete='email']"
    _ORDER_BUTTON = "//button[@id='autotest-checkout-order']"
    _ADD_COMMENT_BUTTON = "//button[@id='autotest-order-comment-add']"
    _TEXT_COMMENT_FIELD = "//textarea[@id='order_comment']"
    _SAVE_COMMENT_BUTTON = "//span[text()='Сохранить']"

    _DELIVERY_BUTTON = "//div[@id='autotest-checkout-delivery-pickup']"
    _PICKUP_POINT = "//div[contains(@class, 'autotest-pickup-point')]"
    _SUBMIT_POINT = "//button[@id='autotest-checkout-delivery-pickup-select']"


    def checkout_is_opened(self):
        self.wait.until(EC.url_to_be(self._PAGE_CHECKOUT_URL))


    def add_name(self):
        name = self.wait.until(EC.visibility_of_element_located(self._NAME_FIELD))
        name.click()
        name.send_keys('name_test')



    def add_surname(self):
        surname = self.wait.until(EC.visibility_of_element_located(self._SURNAME_FIELD))
        surname.click()
        surname.send_keys("family_name")

    def add_number(self):
        number = self.wait.until(EC.visibility_of_element_located(self._NUMBER_FIELD))
        number.click()
        number.send_keys("999-999-99-99")

    def add_email(self):
        email = self.wait.until(EC.visibility_of_element_located(self._EMAIL_FIELD))
        email.click()
        email.send_keys("test@test.ru")

    def add_comment(self):
        comment = self.wait.until(EC.visibility_of_element_located(self._ADD_COMMENT_BUTTON))
        comment.click()
        comment.send_keys("Заказ в работу не брать, для теста")



    def save_comment(self):
        save = self.wait.until(EC.element_to_be_clickable(self._SAVE_COMMENT_BUTTON))
        save.click()

    def click_delivery_button(self):
        self.wait.until(EC.element_to_be_clickable(self._DELIVERY_BUTTON)).click()
        self.wait.until(EC.url_to_be(self._DELIVERY_URL))

    def select_pickup_point(self):
        pickup_point = self.wait.until(EC.element_to_be_clickable(self._PICKUP_POINT))
        pickup_point.click()

    def submit_point(self):
        submit = pickup_point = self.wait.until(EC.element_to_be_clickable(self._SUBMIT_POINT))
        submit.click()


    def make_order(self):
        order = self.wait.until(EC.element_to_be_clickable(self._ORDER_BUTTON))
        order.click()
        self.wait.until(EC.url_contains(self._PAYMENT_URL))






