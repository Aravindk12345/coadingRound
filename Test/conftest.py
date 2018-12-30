import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    options = Options()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(dir_path + "/Drivers/chromedriver.exe")
    driver.get("https://www.cleartrip.com/")
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver

    yield driver
    driver.close()