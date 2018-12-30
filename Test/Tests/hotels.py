import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test.Pages.locators import locators
from selenium.webdriver.support.ui import Select
import time


@pytest.mark.usefixtures("setup")
class TestshouldBeAbleToSearchForHotels:
    def test_click_hotels(self):
        enterloginbtn = self.driver.find_element_by_link_text(locators.click_hotel)
        enterloginbtn.click()

    def test_enter_locality(self):
        enterLocality = self.driver.find_element_by_id(locators.locality_text_box)
        enterLocality.send_keys("Indiranagar, Bangalore")

    def test_click_traveller_selection(self):
        enterloginbtn = Select(self.driver.find_element_by_id(locators.traveller_selection))
        enterloginbtn.select_by_visible_text("1 room, 2 adults")

    def test_click_search_hotels(self):
        enterloginbtn = self.driver.find_element_by_id(locators.click_search_hotels)
        enterloginbtn.click()