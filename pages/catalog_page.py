import allure
from base.base_page import BasePage
from allure_commons.types import Severity
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# @allure.epic("Products")
# @allure.story("Проверка товара с одним размером")
# @allure.suite("Smoke_tests")
# @allure.severity(Severity.NORMAL)

class CatalogPage(BasePage):

    _PRODUCT_CARDS = "//div[contains(@class, 'autotest-product-image')]"
    _QUICK_VIEW = "//div[contains(@class, 'autotest-quickview-open-button']"
    _NOT_ONE_SIZE = "//span[@data-autotest='Select']"

    def find_the_one_size(self):
        with allure.step("Найти товар с одним размером"):
            products = self.wait.until(EC.visibility_of_element_located(self._PRODUCT_CARDS))
            for product in products:
                try:
                    quick_view_button = product.find_element(*self._QUICK_VIEW)
                    quick_view_button.click()

                    # Ждем появления модального окна
                    # wait.until(EC.presence_of_element_located((By.XPATH, "//xpath_к_модальному_окну")))

                    # Проверяем доступные размеры
                    sizes = self.wait.until(EC.presence_of_element_located(self._NOT_ONE_SIZE))

                    if len(sizes) == 1:  # Если в списке только один размер
                        size_text = sizes[0].text.strip().lower()
                        if "one size" in size_text:
                            print("Товар с One Size найден. Добавляем в корзину")

                    # Нажимаем кнопку "Добавить в корзину"
                        add_to_cart_button = self.driver.find_element(By.XPATH, "//span[text()='Добавить в корзину']")
                        add_to_cart_button.click()
                        add_to_cart_button.click()

                        # Даем время на добавление в корзину
                        time.sleep(2)
                        break  # Выходим из цикла после добавления в корзину

                    # # Закрываем модальное окно, если размеров больше одного
                    # close_button = driver.find_element(By.XPATH, "//xpath_к_кнопке_закрытия_модального_окна")
                    # close_button.click()
                    # time.sleep(1)  # Ждем перед открытием следующего товара

                except Exception as e:
                    print(f"Ошибка: {e}")


