import pytest
from selenium import webdriver
import os

@pytest.fixture(autouse=True) #params=["chrome", "firefox"],
def driver(request):
    options = webdriver.ChromeOptions()
    # options = webdriver.FirefoxOptions()
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Firefox(options=options)
    request.cls.driver = driver
    yield
    driver.quit()


# запуск BROWSER=chrome pytest -s -v
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