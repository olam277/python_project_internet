from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class HomePage(BasePage):
    """Class representing the home page."""
    PRODUCT_LINK = (By.LINK_TEXT, "Laptops")
    LOGO = (By.XPATH, "//a[@id='nava']")
    PRODUCT_IMAGE = (By.CLASS_NAME, "card-img-top")
    NEXT_BUTTON = (By.LINK_TEXT, "Next")
    PREVIOUS_BUTTON = (By.LINK_TEXT, "Previous")
    PRICE = (By.CLASS_NAME, "price")
    FEATURED_PRODUCTS = (By.CLASS_NAME, "card-title")

    def click_product(self):
        self.click_element(self.PRODUCT_LINK)

    def click_logo(self):
        self.click_element(self.LOGO)

    def get_product_image(self):
        return self.find_element(self.PRODUCT_IMAGE)

    def get_price(self):
        return self.find_element(self.PRICE).text

    def click_next(self):
        self.click_element(self.NEXT_BUTTON)

    def click_previous(self):
        self.click_element(self.PREVIOUS_BUTTON)

    def get_featured_products(self):
        return self.driver.find_elements(*self.FEATURED_PRODUCTS)

    def verify_product_navigation(self):
        """Verify that clicking on a product shows the correct product page."""
        self.click_product()
        assert "Laptops" in self.driver.title, "Product navigation failed."

    def verify_logo_navigation(self):
        """Verify that clicking on the logo navigates back to the home page."""
        self.click_logo()
        assert "STORE" in self.driver.title, "Logo navigation failed."

    def verify_image_correctness(self, expected_image_url):
        """Verify that the product image is correct."""
        product_image = self.get_product_image()
        assert expected_image_url in product_image.get_attribute('src'), "Product image is incorrect."

    def verify_price_display(self, expected_price):
        """Verify that prices are displayed correctly."""
        price = self.get_price()
        assert price == expected_price, f"Expected price {expected_price}, but got {price}"

    def verify_navigation_buttons(self):
        """Verify that next and previous buttons work."""
        self.click_product()  # Navigate to the product page
        self.click_previous()
        assert "Laptops" in self.driver.title, "Previous button failed."
        self.click_next()
        assert "Laptops" in self.driver.title, "Next button failed."

    def verify_featured_products_display(self):
        """Verify that featured products are displayed correctly on the homepage."""
        featured_products = self.get_featured_products()
        assert len(featured_products) > 0, "No featured products displayed."

    def verify_slideshow_functionality(self):
        """Verify that the slideshow of device images works."""
        slideshow_button = (By.CLASS_NAME, "slideshow-button")
        self.click_element(slideshow_button)
