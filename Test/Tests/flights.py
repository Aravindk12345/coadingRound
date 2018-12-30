import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test.Pages.locators import locators
from selenium.webdriver.support.ui import Select
import time


@pytest.mark.usefixtures("setup")
class TestFlightBooking:
    def test_click_flights(self):
        enterloginbtn = self.driver.find_element_by_link_text(locators.click_flights)
        enterloginbtn.click()

    def test_click_oneway(self):
        enterloginbtn = self.driver.find_element_by_id(locators.click_one_way)
        enterloginbtn.click()

    def test_enter_from_address(self):
        self.driver.find_element_by_id(locators.enter_from).clear()
        enterFromAddress = self.driver.find_element_by_id(locators.enter_from)
        enterFromAddress.send_keys("Bangalore")
        originOptions = self.driver.find_element_by_id("ui-id-1").find_element_by_tag_name("li")
        originOptions.click();

    def test_enter_to_address(self):
        self.driver.find_element_by_id(locators.enter_to).clear()
        enterToAddress = self.driver.find_element_by_id(locators.enter_to)
        enterToAddress.send_keys("Delhi")
        originOption = self.driver.find_element_by_id("ui-id-2").find_element_by_tag_name("li")
        originOption.click();
        self.driver.find_element_by_xpath("//*[@id='ui-datepicker-div']//*[@class='monthBlock last']//*[@class='ui-state-default ']").click();

    def test_search_hotels(self):
        clickSearchBtn = self.driver.find_element_by_id(locators.click_search_flights)
        clickSearchBtn.click()