from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def book_demo_ticket():
    # Start browser
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        driver.maximize_window()

        wait = WebDriverWait(driver, 10)

        # Fill name
        name_input = wait.until(EC.presence_of_element_located((By.NAME, "my-text")))
        name_input.send_keys("John Doe")

        # Fill email
        email_input = driver.find_element(By.NAME, "my-password")
        email_input.send_keys("johndoe@example.com")

        # Choose a date
        date_input = driver.find_element(By.NAME, "my-date")
        date_input.send_keys("2025-12-25")

        # Select dropdown option
        select_option = driver.find_element(By.NAME, "my-select")
        select_option.send_keys("Two")

        # Click submit
        submit_btn = driver.find_element(By.TAG_NAME, "button")
        submit_btn.click()

        # Wait for confirmation
        time.sleep(3)
        print("Demo ticket form submitted successfully!")

    finally:
        driver.quit()

if __name__ == "__main__":
    book_demo_ticket()
