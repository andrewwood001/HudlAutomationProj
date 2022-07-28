import unittest

from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

import test_base
import base
import locators


class TestLogin(test_base.TestBase):

    def test_positiveLoginScenario(self):
        """
        # Test steps for Positive Login Scenario
        # 1. Open Browser (Default set to Chrome)
        # 2. Navigate to "hudl.com"
        # 3. Click Login button and navigate to login page
        # 4. Enter information for username and password (Information configured in "Config.ini" file)
        # 5. Click log in button and verify the site updates to main landing page
        # 6. Log out of website and close browser window
        """
        base.find_element_by_xpath(self.driver, locators.LOGIN_XPATH).click()
        base.enter(self.driver, locators.PASSWORD_XPATH, self.PASSWORD)
        base.find_element_by_xpath(self.driver, locators.EMAIL_XPATH).click()
        base.enter(self.driver, locators.EMAIL_XPATH, self.USERNAME)
        base.find_element_by_xpath(self.driver, locators.PASSWORD_XPATH).click()
        base.find_element_by_id(self.driver, locators.PASSWORD_ID).click()
        base.find_element_by_css(self.driver, ".styles_pageContainer_31NnIgZuiQzDKnKlPaGLsi").click()
        base.find_element_by_id(self.driver, locators.PASSWORD_ID).click()
        base.find_element_by_id(self.driver, locators.LOGIN_ID).click()
        base.find_element_by_css(self.driver, locators.LOGOUT_CSS_SELECTOR, condition=ec.presence_of_element_located)
        self.driver.quit()

    def test_negativeLoginScenario(self):
        """
        # Test steps for Negative Login Scenario
        # 1. Open Browser (Default set to Chrome)
        # 2. Navigate to "hudl.com"
        # 3. Click Login button and navigate to login page
        # 4. Enter information for username (from "Config.ini" file) and password (Automatically set to "Fake_Password")
        # 5. Click log in button, verify the site does NOT update to login page, and returns expected error message
        # 6. Log out of website and close browser window
        """
        with self.assertRaises(TimeoutException):
            base.find_element_by_xpath(self.driver, locators.LOGIN_XPATH).click()
            base.enter(self.driver, locators.PASSWORD_XPATH, 'Fake_Password')
            base.find_element_by_xpath(self.driver, locators.EMAIL_XPATH).click()
            base.enter(self.driver, locators.EMAIL_XPATH, self.USERNAME)
            base.find_element_by_xpath(self.driver, locators.PASSWORD_XPATH).click()
            base.find_element_by_id(self.driver, locators.PASSWORD_ID).click()
            base.find_element_by_css(self.driver, ".styles_pageContainer_31NnIgZuiQzDKnKlPaGLsi").click()
            base.find_element_by_id(self.driver, locators.PASSWORD_ID).click()
            base.find_element_by_id(self.driver, locators.LOGIN_ID).click()
            base.find_element_by_css(self.driver, locators.LOGOUT_CSS_SELECTOR,
                                     condition=ec.presence_of_element_located)
        self.driver.quit()



    def test_organizationLoginScenario(self):
    """
    # Test steps for Organizational Login Scenario
    # 1. Open Browser (Default set to Chrome)
    # 2. Navigate to "hudl.com"
    # 3. Click Login button and navigate to login page
    # 4. Click the button for "Log In with an Organization", verify page updates to Organization Login Page
    # 5. Verify "Log In" button is Inactive
    # 6. Enter the Username from the "config.ini" file
    # 7. Verify the "Log In" button becomes active and Click on it
    # 8. If the email domain is not recognized as Organization (which is expected), return to the standard Login Page
    # 9. Verify the text appears "
    # 	This account can't log in with an organization yet. Please log in using your email and password."
    # 10. Close browser window"""
        base.find_element_by_link_text(self.driver, "Log in").click()
        base.find_element_by_css(self.driver, ".uni-button--minimal").click()
        base.find_element_by_id(self.driver, "uniId_1", condition=ec.presence_of_element_located)
        base.find_element_by_css(self.driver, "button[disabled]", condition=ec.presence_of_element_located)
        base.enter(self.driver, "//input[@name='username']", self.USERNAME)
        base.find_element_by_css(self.driver, 'button[data-qa-id="log-in-with-sso"]').click()
        base.find_element_by_xpath(self.driver,
                                   '//p[contains(text(), "This account can\'t log in with an organization yet. Please log in using your email and password.")]')
        self.driver.close()

    def test_RememberMeScenario(self):
        """
        # Test Steps for Remember Me Scenario
        # 1. Open Browser (Default set to Chrome)
        # 2. Navigate to "hudl.com"
        # 3. Click Login button and navigate to login page
        # 4. Enter information for user name and password (Information configured in "Config.ini" file)
        # 5. Check the box for "Remember Me"
        # 6. Click the Log In button
        # 7. Verify the landing home page
        # 8. Close browser tab (Do NOT log out)
        # 9. Open a new browser tab and navigate to hudl.com
        # 10. Verify the page loads to the "Home" page and not the "Login page"
        """
        base.find_element_by_xpath(self.driver, locators.LOGIN_XPATH).click()
        base.enter(self.driver, locators.PASSWORD_XPATH, self.PASSWORD)
        base.find_element_by_xpath(self.driver, locators.EMAIL_XPATH).click()
        base.enter(self.driver, locators.EMAIL_XPATH, self.USERNAME)
        self.driver.execute_script("arguments[0].click();", base.find_element_by_xpath(self.driver, locators.REMEMBER_ME_XPATH))
        base.find_element_by_id(self.driver, locators.LOGIN_ID).click()
        base.find_element_by_css(self.driver, locators.LOGOUT_CSS_SELECTOR, condition=ec.presence_of_element_located)
        base.open_and_switch_to_tab(self.driver)
        self.driver.get("https://www.hudl.com/")
        base.find_element_by_css(self.driver, locators.LOGOUT_CSS_SELECTOR, condition=ec.presence_of_element_located)

    def test_ResetPasswordScenario(self):
        """
        # Test steps for Reset Password Scenario
        # 1. Open Browser (Default set to Chrome)
        # 2. Navigate to "hudl.com"
        # 3. Verify page loads
        # 4. Press Login Button
        # 5. Verify Login page loads (https://www.hudl.com/login)
        # 6. Press the "Need help" hyperlink
        # 7. Verify the "Login Help" page loads
        # 8. Verify "Send Password Reset" button is Inactive
        # 9. Enter the Username from "config" file into the "Email" field
        # 10. Verify the "Send Password Reset" button becomes Active, but do NOT click on it
        """
        base.find_element_by_xpath(self.driver, locators.LOGIN_XPATH).click()
        self.assertEqual(self.driver.current_url, 'https://www.hudl.com/login')
        base.find_element_by_xpath(self.driver, locators.NEED_HELP_XPATH).click()
        base.find_element_by_xpath(self.driver, locators.LOGIN_HELP_HEADLINE_XPATH)
        base.find_element_by_xpath(self.driver, locators.DISABLED_PASSWORD_RESET_SUBMIT_BUTTON, condition=ec.presence_of_element_located)
        base.enter(self.driver, locators.PASSWORD_RESET_INPUT_XPATH, self.USERNAME)
        base.find_element_by_xpath(self.driver, locators.ACTIVE_PASSWORD_RESET_SUBMIT_BUTTON)


if __name__ == '__main__':
    unittest.main()
