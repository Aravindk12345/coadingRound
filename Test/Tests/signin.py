import pytest
from Test.Pages.locators import locators
import time


@pytest.mark.usefixtures("setup")
class TestSignIn:
    def test_click_your_trips(self):
        enterloginbtn = self.driver.find_element_by_link_text(locators.your_trips)
        enterloginbtn.click()

    def test_click_signin(self):
        enterloginbtn = self.driver.find_element_by_id(locators.signin)
        enterloginbtn.click()
        time.sleep(5)
        fram = self.driver.find_element_by_id(locators.frame)
        self.driver.switch_to_frame(fram)
        time.sleep(5)

    def test_click_signinbtn(self):
        signinbtn = self.driver.find_element_by_id(locators.signinBtn)
        signinbtn.click()
        time.sleep(10)
        centerText = self.driver.find_element_by_id(locators.error1).text
        print(centerText)