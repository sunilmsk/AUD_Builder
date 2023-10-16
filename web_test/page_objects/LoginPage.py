import selenium.webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Login:

    email_text_xpath="//input[@id='i0116']"
    next_button_xpath="//input[@id='idSIButton9']"
    password_text_xpath="//input[@id='i0118']"
    forget_password_xpath="//a[@id='idA_PWD_ForgotPassword']"
    sign_in_with_security_key_xpath="//a[@id='idA_PWD_SwitchToFido']"
    sign_in_button_xpath="//input[@id='idSIButton9']"
    dont_show_checkbox_xpath="//input[@id='KmsiCheckboxField']"
    dont_show_yes_button_xpath="//input[@id='idSIButton9']"


    def __init__(self, driver):
        self.driver = driver


    def set_username(self, username):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.email_text_xpath))).clear()
        self.driver.find_element(By.XPATH, self.email_text_xpath).send_keys(username)

    def click_next_button(self):
        self.driver.find_element(By.XPATH, self.next_button_xpath).click()

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.password_text_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_text_xpath).send_keys(password)


    def click_signin_button(self):
        self.driver.find_element_by_xpath(self.sign_in_button_xpath).click()

    def wait_for_element_visible(self, locator_type, value, timeout=10):
        try:
            by_locator = None

            if locator_type == 'id':
                by_locator = By.ID
            elif locator_type == 'name':
                by_locator = By.NAME
            elif locator_type == 'xpath':
                by_locator = By.XPATH
            elif locator_type == 'class':
                by_locator = By.CLASS_NAME
            elif locator_type == 'linkText':
                by_locator = By.LINK_TEXT
            elif locator_type == 'partialLinkText':
                by_locator = By.PARTIAL_LINK_TEXT
            elif locator_type == 'tagName':
                by_locator = By.TAG_NAME  # Corrected from By.LINK_TEXT to By.TAG_NAME
            # Add more conditions for other locator types if needed.

            if by_locator:
                wait = WebDriverWait(self.driver, timeout)
                element = wait.until(EC.visibility_of_element_located((by_locator, value)))
                return element
        except TimeoutException:
            print(f"Element with {locator_type}: '{value}' did not become visible within {timeout} seconds.")
            return None
