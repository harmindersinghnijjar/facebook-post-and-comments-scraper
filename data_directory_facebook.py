# Description: This script automates the process of accessing the Facebook website using an existing data directory.
# Author: harmindesinghnijjar
# Date: 2023-12-07
# Version: 1.0.0
# Usage: python data_directory_facebook.py


import time
import os
import getpass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class SeleniumAutomator:
    # Constructor method
    def __init__(self, driver):
        self.driver = driver

    # Method to open Facebook in a Chrome instance
    def open_facebook(self):
        try:
            # Open Facebook
            self.driver.get("https://www.facebook.com")
        except Exception as e:
            print(f"An error occurred while opening Facebook: {e}")
        else:
            print("Opened Facebook successfully!")

    # Method to close the Chrome instance
    def close_browser(self):
        self.driver.quit()
        print("Closed the browser successfully!")


if __name__ == "__main__":
    # Kill any existing Chrome instances to avoid conflicts
    os.system("taskkill /im chrome.exe /f")

    # Fetch current user's name
    user = getpass.getuser()

    # Set up ChromeDriver service
    service = Service()

    # Define Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument(
        f"--user-data-dir=C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data"
    )
    options.add_argument("--profile-directory=Default")

    # Create a WebDriver instance
    chrome_driver = webdriver.Chrome(service=service, options=options)

    # Create an instance of SeleniumAutomator
    selenium_automator = SeleniumAutomator(driver=chrome_driver)

    # Use the SeleniumAutomator methods
    selenium_automator.open_facebook()
    # ... perform other actions ...
    time.sleep(60)

    # Close the browser when done
    selenium_automator.close_browser()
