import datetime

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Utils:
    def __init__(self, driver):
        self.driver = driver

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

    def take_screenshot(self):
        # Get the current date and time with milliseconds
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")

        # Define the filename with a ".png" extension
        filename = fr"C:\Users\sunil.mekala\PycharmProjects\Audience_Builder\web\screen_shots/screenshot_{current_time}.png"

        # Take a screenshot and save it
        self.driver.save_screenshot(filename)
