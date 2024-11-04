import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.home_page import HomePage
from .base_page import BasePage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def home_page(driver):
    """Fixture to initialize HomePage."""
    home_page = HomePage(driver)
    driver.get('https://www.demoblaze.com/')
    return home_page

def test_verify_product_navigation(home_page):
    home_page.verify_product_navigation()

def test_verify_logo_navigation(home_page):
    home_page.verify_logo_navigation()

def test_verify_image_correctness(home_page):
    expected_image_url = "expected_image_url_here"  # עדכן עם ה-URL הנכון
    home_page.verify_image_correctness(expected_image_url)

def test_verify_price_display(home_page):
    expected_price = "$1000"  # עדכן עם המחיר הנכון
    home_page.verify_price_display(expected_price)

def test_verify_navigation_buttons(home_page):
    home_page.verify_navigation_buttons()

def test_verify_featured_products_display(home_page):
    home_page.verify_featured_products_display()

def test_verify_slideshow_functionality(home_page):
    home_page.verify_slideshow_functionality()


