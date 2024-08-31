from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (this example uses Chrome)
driver = webdriver.Chrome()

try:
    # Navigate to Facebook's login page
    driver.get("https://www.facebook.com")

    # Maximize the window to ensure all elements are visible
    driver.maximize_window()

    # Find the email input field and enter the email
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("your_email@example.com")

    # Find the password input field and enter the password
    password_field = driver.find_element(By.ID, "pass")
    password_field.send_keys("your_password")

    # Find the login button and click it
    login_button = driver.find_element(By.NAME, "login")
    login_button.click()

    # Wait for a few seconds to ensure the login is processed
    time.sleep(5)

    # Verify if login was successful by checking the URL or a specific element
    if "login" not in driver.current_url:
        print("Login successful!")
    else:
        print("Login failed.")

finally:
    # Close the browser window
    driver.quit()
