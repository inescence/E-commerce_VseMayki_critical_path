from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.delivery_map_page import MapPage


class BaseTest:

    def setup_method(self):
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.delivery_map_page = MapPage(self.driver)
        # self.payment_page = PaymentPage(self.driver)