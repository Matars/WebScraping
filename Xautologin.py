# Import necessary libraries from selenium and webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set options for Chrome driver
options = Options()
options.add_experimental_option("detach", True)

# Initialize Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to the specified URL
driver.get("http://x.com")

# Define login credentials
username = "ApplekidBurner"
password = "ThisIsBurnerAccount"

# Maximize browser window
driver.maximize_window()

# Locate and click the 'refuse' button to dismiss cookies popup
buttons = driver.find_elements("xpath", "//div[@role='button']")
for button in buttons:
    if "refuse" in button.get_attribute('innerHTML').lower():
        button.click()
        break

# Navigate to login page
url = "https://www.x.com/login"
driver.get(url)

# Allow the page to load
driver.implicitly_wait(30)

# Enter username
input_element = driver.find_element("xpath", "//input[@type='text']")
input_element.send_keys(username)

# Click 'next' button
buttons = driver.find_elements("xpath", "//div[@role='button']")
for button in buttons:
    if "next" in button.get_attribute('innerHTML').lower():
        button.click()
        break

# Allow the page to load
driver.implicitly_wait(30)

# Enter password
input_element = driver.find_element("xpath", "//input[@type='password']")
input_element.send_keys(password)

# Click 'log in' button
buttons = driver.find_elements("xpath", "//div[@role='button']")
for button in buttons:
    if "log in" in button.get_attribute('innerHTML').lower():
        button.click()
        break

import time

# Initialize scroll position and increment value
scroll_position = 0
scroll_increment = 500  # Adjust to control scroll amount

# Infinite loop for scrolling and clicking 'like' button
while True:
    try:
        # Incrementally scroll down
        scroll_position += scroll_increment
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(1.5)  # Adjust to control scroll speed
        
        # Locate and click the 'like' button
        button = driver.find_element("xpath", "//div[@data-testid='like']")
        button.click()
        driver.execute_script("arguments[0].scrollIntoView();", button)
        
    except Exception as e:
        # Break loop if an error occurs (e.g., button not found)
        print(f"An error occurred: {e}")
        break
