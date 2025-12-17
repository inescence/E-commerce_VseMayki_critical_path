import allure
from base.base_test import BaseTest
from allure_commons.types import Severity


@allure.epic("ORDERS")
@allure.story("Оформление заказа")
@allure.suite("Smoke_tests")
@allure.severity(Severity.CRITICAL)

class TestCatalogPage(BaseTest):

    @allure.title("Оформление заказа")
    @allure.description("Выбор товара и создание заказа")
    @allure.severity("Critical")
    def test_add_to_cart(self):
        self.main_page.open()
        self.main_page.accept_cookies_button()
        self.main_page.submit_city_button()
        self.main_page.catalog_is_opened()

        self.catalog_page.find_the_one_size()

        self.main_page.click_product()
        self.main_page.choose_size()
        self.main_page.add_to_cart()
        self.main_page.click_buy_button()
        self.cart_page.cart_is_opened()
        self.cart_page.check_products()
        self.cart_page.click_plus_button()
        self.cart_page.click_favorite_button()
        self.cart_page.delete_button()
        self.cart_page.click_checkout_button()
        self.checkout_page.checkout_is_opened()
        self.checkout_page.add_name()
        self.checkout_page.add_surname()
        self.checkout_page.add_number()
        self.checkout_page.add_email()
        self.checkout_page.add_comment()
        self.checkout_page.save_comment()
        self.checkout_page.click_delivery_button()
        self.checkout_page.select_pickup_point()
        self.checkout_page.submit_point()
        self.checkout_page.checkout_is_opened()
        self.checkout_page.make_order()

        self.checkout_page.go_to_pay()
        self.checkout_page.check_qr()
        self.checkout_page.check_bank_payment()
        self.checkout_page.pay_button()

        self.checkout_page.check_bank_payment()
        self.checkout_page.check_yandex_pay()



