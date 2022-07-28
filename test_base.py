import unittest
import configparser

from selenium import webdriver


class TestBase(unittest.TestCase):
    CONFIG = configparser.ConfigParser()
    CONFIG.read('config.ini')
    USERNAME = CONFIG['USER CREDENTIALS']['USERNAME']
    PASSWORD = CONFIG['USER CREDENTIALS']['PASSWORD']

    # The webdriver is set by default to use Chrome Browser
    # Update the executable path with the location of "chromedriver.exe" on you local machine
    # To use other Browsers (i.e Firefox), update webdriver.Firefoxdriver(executable path="")

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Selenium\chromedriver.exe")
        self.driver.get("https://www.hudl.com/")
        self.driver.set_window_size(1456, 876)
        self.vars = {}

    def tearDown(self):
        self.driver.quit()
