from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

class BasePage:
    """Class to represent the base page that other pages can inherit from."""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator):
        """Finds element based on locator passed."""
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            print(f"Element not found: {locator}")
            return None

    def click_element(self, locator):
        """Clicks on element found by locator."""
        element = self.find_element(locator)
        if element:
            try:
                element.click()
            except ElementClickInterceptedException:
                print(f"Could not click on the element: {locator}")

    def enter_text(self, locator, text):
        """Enters text in a specified field located by the locator."""
        element = self.find_element(locator)
        if element:
            element.clear()  # Clear any existing text
            element.send_keys(text)

    def wait_for_element(self, locator, timeout=10):
        """Waits for an element to be present in the DOM."""
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f"Element not found within {timeout} seconds: {locator}")

