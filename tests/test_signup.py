import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from pages.signup_page import SignUpPage
from selenium.common.exceptions import TimeoutException

@pytest.mark.usefixtures("driver")
def test_signup_valid_credentials(driver):
    base_url = 'https://www.demoblaze.com/'
    driver.get(base_url)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "signin2"))).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "sign-username")))
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "sign-password")))
    sp = SignUpPage(driver)
    sp.enter_username("your_username")
    sp.enter_password("your_password")
    sp.click_signup()
    assert sp.is_signup_successful()

@pytest.mark.usefixtures("driver")
def test_signup_empty_fields(driver):
    base_url = 'https://www.demoblaze.com/'
    driver.get(base_url)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "signin2"))).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "sign-username")))
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "sign-password")))

    driver.find_element(By.ID, "sign-username").clear()
    driver.find_element(By.ID, "sign-password").clear()
    driver.find_element(By.CSS_SELECTOR, "button[onclick='register()']").click()

    alert = Alert(driver)
    alert_text = alert.text
    assert "Please fill out Username and Password." == alert_text
    alert.accept()

    driver.find_element(By.ID, "sign-username").send_keys("elad123")
    driver.find_element(By.ID, "sign-password").clear()
    driver.find_element(By.CSS_SELECTOR, "button[onclick='register()']").click()

    alert = Alert(driver)
    alert_text = alert.text
    assert "Please fill out Username and Password." == alert_text


@pytest.mark.usefixtures("driver")
def test_signup_password_only(driver):
    base_url = 'https://www.demoblaze.com/'
    driver.get(base_url)
    try:
        WebDriverWait(driver, 2).until(EC.alert_is_present())
        alert = Alert(driver)
        alert.accept()
    except TimeoutException:
        pass
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "signin2"))).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "sign-username")))
    driver.find_element(By.ID, "sign-password").send_keys("elad123")
    driver.find_element(By.ID, "sign-username").clear()
    driver.find_element(By.CSS_SELECTOR, "button[onclick='register()']").click()
    alert = Alert(driver)
    alert_text = alert.text
    assert "Please fill out Username and Password." == alert_text


@pytest.mark.usefixtures("driver")
def test_signup_no_password(driver):
    base_url = 'https://www.demoblaze.com/'
    driver.get(base_url)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "signin2"))).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "sign-username")))

    driver.find_element(By.ID, "sign-username").send_keys("new_username")
    driver.find_element(By.ID, "sign-password").clear()
    driver.find_element(By.CSS_SELECTOR, "button[onclick='register()']").click()

    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = Alert(driver)
    alert_text = alert.text
    alert.accept()
    assert "Please fill out Username and Password." in alert_text

@pytest.mark.usefixtures("driver")
def test_signup_username_only(driver):
    base_url = 'https://www.demoblaze.com/'
    driver.get(base_url)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "signin2"))).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "sign-username")))

    driver.find_element(By.ID, "sign-username").send_keys("my_username")
    driver.find_element(By.ID, "sign-password").clear()
    driver.find_element(By.CSS_SELECTOR, "button[onclick='register()']").click()

    alert = Alert(driver)
    alert_text = alert.text
    assert "Please fill out Username and Password." in alert_text
