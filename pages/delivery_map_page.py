from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
from data.links import Links

class MapPage(BasePage):

    _PAGE_URL = Links.DELIVERY_MAP_PAGE

    _DELIVERY_BUTTON = "//div[@id='autotest-checkout-delivery-pickup']"
    _PICKUP_POINT = "//div[contains(@class, 'autotest-pickup-point')]"
    _SUBMIT_POINT = "//button[@id='autotest-checkout-delivery-pickup-select']"

    @allure.step("Select pickup point")
    def select_pickup_point(self):
        pickup_point = self.wait.until(EC.element_to_be_clickable(self._PICKUP_POINT))
        pickup_point.click()

    @allure.step("Submit point")
    def submit_point(self):
        submit_point = self.wait.until(EC.element_to_be_clickable(self._SUBMIT_POINT))
        submit_point.click()