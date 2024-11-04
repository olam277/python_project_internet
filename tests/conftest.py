import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Set webdriver_manager to use the local cache
os.environ['WDM_LOCAL'] = '1'

@pytest.fixture(scope="session")
def driver():
     """Fixture for setting up WebDriver instance."""
     chrome_options = webdriver.ChromeOptions()
     chrome_service = Service(ChromeDriverManager().install())  # use the path directly

     # Initialize Chrome driver with the specified service and options
     driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
     driver.maximize_window()
     yield driver
     driver.quit()
