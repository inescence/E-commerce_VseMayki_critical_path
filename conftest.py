import pytest
from selenium import webdriver
import os

@pytest.fixture(autouse=True)
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--incognito")
    # options.add_argument("--ignore-certificate-errors")  # для стейджа
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield
    driver.quit()

# для докера
    # options.add_argument("--disable_cache")
    # options.add_argument("--headless")  # для докера
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--window-size=1920,1080")



# для запуска в разных браузерах: BROWSER=chrome pytest -s -v

# @pytest.fixture(scope="function", autouse=True)
# def get_driver(request):
#
#     if os.environ["BROWSER"] == "chrome":
#         driver = webdriver.Chrome()
#         request.cls.driver = driver
#         yield
#         driver.quit()
#
#     elif os.environ["BROWSER"] == "firefox":
#         driver = webdriver.Firefox()
#         request.cls.driver = driver
#         yield
#         driver.quit()