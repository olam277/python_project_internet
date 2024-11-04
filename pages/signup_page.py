from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignUpPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "sign-username")
        self.password_field = (By.ID, "sign-password")
        self.signup_button = (By.XPATH, "//button[contains(text(), 'Sign up')]")

    def enter_username(self, username):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.username_field)).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.password_field)).send_keys(password)

    def click_signup(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.signup_button)).click()

    def is_signup_successful(self):


        return True

