from data.links import Links
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure

class CheckoutPage(BasePage):

    _PAGE_URL = Links.CHECKOUT_PAGE
    _ORDER_STATUS_URL = "https://www.vsemayki.ru/newpayment/"

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

    @allure.step("Enter name")
    def add_name(self):
        name = self.wait.until(EC.element_to_be_clickable(self._NAME_FIELD))
        name.click()
        name.send_keys('name_test')

    @allure.step("Enter surname")
    def add_surname(self):
        surname = self.wait.until(EC.visibility_of_element_located(self._SURNAME_FIELD))
        surname.click()
        surname.send_keys("family_name")

    @allure.step("Enter phone number")
    def add_number(self):
        phone_number = self.wait.until(EC.visibility_of_element_located(self._NUMBER_FIELD))
        phone_number.click()
        phone_number.send_keys("999-999-99-99")

    @allure.step("Enter email")
    def add_email(self):
        email = self.wait.until(EC.visibility_of_element_located(self._EMAIL_FIELD))
        email.click()
        email.send_keys("autotest@vsemayki.ru")


    @allure.step("Сlick delivery button")
    def click_delivery_button(self):
        delivery_button = self.wait.until(EC.element_to_be_clickable(self._DELIVERY_BUTTON))
        delivery_button.click()

    @allure.step("Enter comment")
    def add_comment(self):
        add_comment = self.wait.until(EC.visibility_of_element_located(self._ADD_COMMENT_BUTTON))
        add_comment.click()
        add_comment.send_keys("Заказ в работу не брать, для теста")

    @allure.step("Save comment")
    def save_comment(self):
        self.wait.until(EC.element_to_be_clickable(self._SAVE_COMMENT_BUTTON)).click()

    @allure.step("Make order and screenshot")
    def make_order(self):
        self.wait.until(EC.element_to_be_clickable(self._ORDER_BUTTON)).click()
        self.wait.until(EC.url_contains(self._ORDER_STATUS_URL))
        self.screenshot()






