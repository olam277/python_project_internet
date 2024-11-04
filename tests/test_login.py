import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from selenium.webdriver.common.alert import Alert

@pytest.mark.usefixtures("driver")
def test_login(driver):
    base_url = 'https://www.demoblaze.com/'
    driver.get(base_url)
    try:
        login_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "login2"))
        )
        print("הדפיס")
        login_button.click()
    except Exception as e:
        print("לא הדפיס", str(e))
        return

    username_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "loginusername")))
    password_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "loginpassword")))

    lp = LoginPage(driver)
    lp.enter_username("elad123")
    lp.enter_password("elad123")

    login_submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Log in')]"))
    )
    print("well done")
    login_submit_button.click()

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "logout2")))
    print("good job")

@pytest.mark.usefixtures("driver")
def test_login_failure(driver):
    base_url = 'https://www.demoblaze.com/'
    driver.get(base_url)
    login_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "login2"))
    )
    login_button.click()
    username_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "loginusername")))
    password_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "loginpassword")))

    lp = LoginPage(driver)
    lp.enter_username("wrong_username")
    lp.enter_password("wrong_password")
    lp.click_login()

    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        assert "שגיאה" in alert_text
        print("בדיקת כישלון עברה")
    except Exception as e:
        print("שגיאה", str(e))

@pytest.mark.usefixtures("driver")
def test_login_invalid_username_and_password(driver):
    base_url = 'https://www.demoblaze.com/'
    driver.get(base_url)
    login_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "login2"))
    )
    login_button.click()
    username_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "loginusername")))
    password_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "loginpassword")))

    lp = LoginPage(driver)
    lp.enter_username("invalid_user")
    lp.enter_password("invalid_pass")

    login_submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Log in')]"))
    )
    login_submit_button.click()

    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = Alert(driver)
        alert_text = alert.text
        alert.accept()
        assert "Wrong password." in alert_text
    except Exception as e:
        print("שגיאה", str(e))

@pytest.mark.usefixtures("driver")
def test_login_invalid_username(driver):
    base_url = 'https://www.demoblaze.com/'
    driver.get(base_url)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "login2"))).click()

    lp = LoginPage(driver)
    lp.enter_username("invalid@user!")
    lp.enter_password("somepassword")

    login_submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Log in')]"))
    )
    login_submit_button.click()

    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = Alert(driver)
    alert_text = alert.text
    alert.accept()
    assert "User does not exist." in alert_text

@pytest.mark.usefixtures("driver")
def test_login_invalid_password(driver):
    base_url = 'https://www.demoblaze.com/'
    driver.get(base_url)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "login2"))).click()

    lp = LoginPage(driver)
    lp.enter_username("valid_username")
    lp.enter_password("wrongpassword")

    login_submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Log in')]"))
    )
    login_submit_button.click()

    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = Alert(driver)
        alert_text = alert.text
        alert.accept()
        assert "Wrong password" in alert_text
    except Exception as e:
        print("שגיאה", str(e))


