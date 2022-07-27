
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from ru import TextConfig

# The webdriver is set by default to use Chrome Browser
# Update the executable path with the location of "chromedriver.exe" on you local machine
# To use other Browsers (i.e Firefox), update webdriver.Firefoxdriver(executable path="")


class TestHudlLoginScenarios(unittest.TestCase):

    def setUp(self):
        self.config = TextConfig()
        self.driver = webdriver.Chrome(executable_path="C:\Selenium\chromedriver.exe")
        self.vars = {}

    def tearDown(self):
        self.driver.quit()

    # Test steps for Positive Login Scenario
    # 1. Open Browser (Default set to Chrome)
    # 2. Navigate to "hudl.com"
    # 3. Click Login button and navigate to login page
    # 4. Enter information for user name and password (Information configured in "Config.txt" file)
    # 5. Click log in button and verify the site updates to main landing page
    # 6. Log out of website and close browser window

    def test_positiveLoginScenario(self):
        self.driver.get("https://www.hudl.com/")
        self.driver.set_window_size(1456, 876)
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        self.driver.find_element(By.ID, "password").send_keys(self.config['PASSWORD'])
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys(self.config['USERNAME'])
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.CSS_SELECTOR, ".styles_pageContainer_31NnIgZuiQzDKnKlPaGLsi").click()
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "logIn").click()
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/logout"]')))
        self.driver.close()

    # Test steps for Negative Login Scenario
    # 1. Open Browser (Default set to Chrome)
    # 2. Navigate to "hudl.com"
    # 3. Click Login button and navigate to login page
    # 4. Enter information for user name (from "Config.txt" file) and password (Automatically set to "Fake_Password")
    # 5. Click log in button, verify the site does NOT update to login page, and returns expected error message
    # 6. Log out of website and close browser window

    def test_negativeLoginScenario(self):
        with self.assertRaises(TimeoutException):
            self.driver.get("https://www.hudl.com/")
            self.driver.set_window_size(1456, 876)
            self.driver.find_element(By.LINK_TEXT, "Log in").click()
            self.driver.find_element(By.ID, "password").send_keys(["Fake_Password"])
            self.driver.find_element(By.ID, "email").click()
            self.driver.find_element(By.ID, "email").send_keys(self.config['USERNAME'])
            self.driver.find_element(By.ID, "password").click()
            self.driver.find_element(By.CSS_SELECTOR, ".styles_pageContainer_31NnIgZuiQzDKnKlPaGLsi").click()
            self.driver.find_element(By.ID, "password").click()
            self.driver.find_element(By.ID, "logIn").click()
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/logout"]')))
        self.driver.close()

    # Test steps for Organizational Login Scenario
    # 1. Open Browser (Default set to Chrome)
    # 2. Navigate to "hudl.com"
    # 3. Click Login button and navigate to login page
    # 4. Click the button for "Log In with an Organization", verify page updates to Organization Login Page
    # 5. Enter the Username from the "config.txt" file
    # 6. If the email domain is not recognized as Organization, return to the standard Login Page

    def test_organizationLoginScenario(self):
        with self.assertRaises(TimeoutException):
            self.driver.get("https://www.hudl.com/")
            self.driver.set_window_size(1456, 868)
            self.driver.find_element(By.LINK_TEXT, "Log in").click()
            self.driver.find_element(By.CSS_SELECTOR, ".uni-button--minimal").click()
            self.driver.find_element(By.ID, "uniId_1").click()
            self.driver.find_element(By.ID, "uniId_1").send_keys(self.config['USERNAME'])
            self.driver.find_element(By.CSS_SELECTOR, ".uni-button--primary").click()
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/logout"]')))
            self.driver.close()


if __name__ == '__main__':
    unittest.main()
