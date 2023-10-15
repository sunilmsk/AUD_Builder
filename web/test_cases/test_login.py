import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web.page_objects.LoginPage import Login
from web.utils.utilities import Utils


class TestLogin:
    URL = "https://admin.qa.console.sharecare.com/"
    username = "Sunil.Mekala@sharecare.com"
    password = "MSK123GoodTimes@123"

    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    def test_login_account(self):
        self.driver.get(self.URL)
        time.sleep(15)
        self.LP = Login(self.driver)
        self.LP.set_username(self.username)
        # self.LP.wait_for_element_visible("XPATH", self.LP.click_next_button(), 10)
        self.util = Utils(self.driver)
        self.util.wait_for_element_visible("XPATH", self.LP.click_next_button(), 10)
        time.sleep(10)
        self.LP.set_password(self.password)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.LP.sign_in_button_xpath).click()
        # self.LP.wait_for_element_visible("XPATH", self.LP.sign_in_button_xpath, 20).click()
        self.driver.find_element(By.XPATH, self.LP.dont_show_checkbox_xpath).click()
        self.driver.find_element(By.XPATH, self.LP.dont_show_yes_button_xpath).click()
        current_title = self.driver.title
        print("Current page title: ", current_title)
        time.sleep(3)
        assert current_title == "Sharecare Admin Console", "Login Failed"
        self.util.take_screenshot()
