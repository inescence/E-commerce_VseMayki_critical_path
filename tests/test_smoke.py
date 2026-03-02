import time

import allure
from base.base_test import BaseTest
from allure_commons.types import Severity

@allure.epic("ORDERS")
@allure.story("Оформление заказа")
@allure.suite("Smoke_tests")
@allure.severity(Severity.CRITICAL)

class TestCreateOrder(BaseTest):
    @allure.title("Оформление заказа")
    @allure.description("Выбор товара и создание заказа")
    @allure.severity("Critical")
    def test_make_order(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.main_page.accept_cookies_button()
        self.main_page.submit_city_button()
        self.main_page.click_product_card()
        self.product_page.is_opened()
        self.product_page.choose_size()
        self.product_page.add_to_cart()
        self.product_page.go_to_cart()
        self.cart_page.is_opened()
        self.cart_page.click_plus_button()
        self.cart_page.click_favorite_button()
        self.cart_page.add_gift_wrapping_button()
        self.cart_page.choose_gift_button()
        self.cart_page.check_products()
        self.cart_page.click_checkout_button()
        self.checkout_page.is_opened()
        self.checkout_page.add_name()
        self.checkout_page.add_surname()
        self.checkout_page.add_number()
        self.checkout_page.add_email()
        self.checkout_page.add_comment()
        self.checkout_page.save_comment()
        self.checkout_page.click_delivery_button()
        self.delivery_map_page.is_opened()
        self.delivery_map_page.select_pickup_point()
        self.delivery_map_page.submit_point()
        self.checkout_page.is_opened()
        self.checkout_page.make_order()
        # self.payment_page.is_opened()



