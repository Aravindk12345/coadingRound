import pytest
from Test.Pages.locators import locators
from Test.TestData.UserData import Userdata


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
        enterFromAddress.send_keys(Userdata.FlightDetails.get('from_address'))
        originOptions = self.driver.find_element_by_id(locators.select_from_drop_down).find_element_by_tag_name(locators.tag_id)
        originOptions.click()

    def test_enter_to_address(self):
        self.driver.find_element_by_id(locators.enter_to).clear()
        enterToAddress = self.driver.find_element_by_id(locators.enter_to)
        enterToAddress.send_keys(Userdata.FlightDetails.get('to_address'))
        originOption = self.driver.find_element_by_id(locators.select_to_drop_down).find_element_by_tag_name(locators.tag_id)
        originOption.click()
        self.driver.find_element_by_xpath(locators.date_picker).click()

    def test_search_hotels(self):
        clickSearchBtn = self.driver.find_element_by_id(locators.click_search_flights)
        clickSearchBtn.click()
