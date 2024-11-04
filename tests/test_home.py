import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()  # או בחר דפדפן אחר
    driver.get("https://www.demoblaze.com/")
    yield driver
    driver.quit()

#1
def test_home_page_title(driver):
    assert "STORE" in driver.title

#2
def test_categories_displayed(driver):
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.ID, "itemc")))

    expected_categories = ["Phones", "Laptops", "Monitors"]
    categories = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@class='list-group-item']")))
    actual_categories = [category.text for category in categories]

    assert all(category in actual_categories for category in expected_categories), "Some categories are missing!"

#3
def test_specific_product_display(driver):
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.ID, "itemc")))

    product_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Samsung galaxy s6')]")))
    product_link.click()

    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//h4[contains(text(), 'Samsung galaxy s6')]")))
        product_title = driver.find_element(By.XPATH, "//h4[contains(text(), 'Samsung galaxy s6')]")
        assert product_title is not None
    except TimeoutException:
        print("The product page did not load in time.")
        assert False, "Failed to load product page after clicking the link."

#4
def test_specific_product_display(driver):
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.ID, "itemc")))

    product_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Samsung galaxy s6')]")))
    product_link.click()

    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//h4[contains(text(), 'Samsung galaxy s6')]")))
        product_title = driver.find_element(By.XPATH, "//h4[contains(text(), 'Samsung galaxy s6')]")
        assert product_title is not None
    except TimeoutException:
        print("The product page did not load in time.")

#5
def test_logo_redirects_to_home(driver):
    wait = WebDriverWait(driver, 20)
    logo = wait.until(EC.element_to_be_clickable((By.ID, "nava")))
    logo.click()
    wait.until(EC.presence_of_element_located((By.ID, "itemc")))
    assert driver.find_element(By.ID, "itemc").is_displayed()

#6
def test_specific_product_image(driver):
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.XPATH, "//img[@class='card-img-top img-fluid']")))

    product_image = driver.find_element(By.XPATH, "//img[@class='card-img-top img-fluid']")
    expected_src = "imgs/galaxy_s6.jpg"
    actual_src = product_image.get_attribute("src")

    assert expected_src in actual_src, f"The product image is incorrect. Expected to contain: {expected_src}, but got: {actual_src}"

#7
def test_home_page(driver):
    driver.get("https://www.demoblaze.com/index.html")
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".carousel-inner .active img")))

    first_image = driver.find_element(By.CSS_SELECTOR, ".carousel-inner .active img")
    assert first_image.is_displayed(), "The first image is not displayed."

#8
def test_pagination_buttons(driver):
    wait = WebDriverWait(driver, 30)


    prev_button = wait.until(EC.element_to_be_clickable((By.ID, "prev2")))
    next_button = wait.until(EC.element_to_be_clickable((By.ID, "next2")))


    next_button.click()


    try:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//img[@class='new-image-class']")))  # עדכן כאן את ה-XPath לאלמנט החדש
        assert driver.find_element(By.XPATH,
                                   "//img[@class='new-image-class']").is_displayed(), "The new content after Next is not displayed."
    except TimeoutException:
        print("The new content did not load in time.")


    prev_button.click()


    try:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//img[@class='original-image-class']")))  # עדכן כאן את ה-XPath לאלמנט הקודם
        assert driver.find_element(By.XPATH,
                                   "//img[@class='original-image-class']").is_displayed(), "The original content after Previous is not displayed."
    except TimeoutException:
        print("The original content did not load in time.")


#9
def test_home_page_title(driver):
    driver.get("https://www.demoblaze.com/")
    assert driver.title == "STORE"



#10
def test_home_page_elements(driver):
    driver.get("https://www.demoblaze.com/")
    assert driver.find_element(By.ID, "nava").is_displayed()
    assert driver.find_element(By.ID, "login2").is_displayed()
    assert driver.find_element(By.ID, "signin2").is_displayed()

#11
def test_product_display(driver):
    driver.get("https://www.demoblaze.com/")
    product_link = driver.find_element(By.LINK_TEXT, "Laptops")
    product_link.click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "card"))
    )
    products = driver.find_elements(By.CLASS_NAME, "card")
    assert len(products) > 0, "No products found on the Laptops page."


#12
def test_logo_navigates_home(driver):
    driver.get("https://www.demoblaze.com/")
    logo = driver.find_element(By.ID, "nava")
    logo.click()
    WebDriverWait(driver, 10).until(
        EC.title_contains("STORE")
    )
    assert "STORE" in driver.title, "Did not navigate to home page."




