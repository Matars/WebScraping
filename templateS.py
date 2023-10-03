# Selenium script to auto login to X.com

# Import necessary libraries from selenium and webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set options for Chrome driver
options = Options()
options.add_experimental_option("detach", True)

# Initialize Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

# Navigate to the specified URL
driver.get("http://x.com")

# Define login credentials
username = "ApplekidBurner"
password = "ThisIsBurnerAccount"

# Maximize browser window
driver.maximize_window()

# Locate buttons on the page using xpath and role attribute
buttons = driver.find_elements("xpath", "//div[@role='button']")
