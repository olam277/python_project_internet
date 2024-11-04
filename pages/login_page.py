from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class LoginPage(BasePage):
    """Class to represent the login page actions."""

    USERNAME_FIELD = (By.ID, "loginusername")  # ID של שדה שם המשתמש
    PASSWORD_FIELD = (By.ID, "loginpassword")  # ID של שדה הסיסמה
    LOGIN_BUTTON = (By.ID, "submit")  # ID של כפתור הכניסה

    def enter_username(self, username):
        """Enters the username in the username field."""
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.USERNAME_FIELD))
        self.enter_text(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        """Enters the password in the password field."""
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.PASSWORD_FIELD))
        self.enter_text(self.PASSWORD_FIELD, password)

    def click_login(self):
        """Clicks the login button."""
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        self.click_element(self.LOGIN_BUTTON)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.LOGIN_BUTTON = (By.XPATH, "//button[text()='Log in']")  # XPath לכפתור

    def enter_username(self, username):
        username_input = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "loginusername"))
        )
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "loginpassword"))
        )
        password_input.send_keys(password)

    def click_login(self):
        login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        login_button.click()



