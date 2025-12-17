from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.catalog_page import CatalogPage


class BaseTest:

    def setup_method(self):
        self.main_page = MainPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.catalog_page = CatalogPage(self.driver)