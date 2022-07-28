import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def find_element(driver, locator, by, timeout, condition):
    cls = WebDriverWait(driver, timeout)
    element = cls.until(condition((by, locator)))
    return element


def find_element_by_xpath(driver, xpath, timeout=10, condition=ec.element_to_be_clickable):
    return find_element(driver, xpath, By.XPATH, timeout, condition)


def find_element_by_css(driver, selector, timeout=10, condition=ec.element_to_be_clickable):
    return find_element(driver, selector, By.CSS_SELECTOR, timeout, condition)


def find_element_by_id(driver, selector, timeout=10, condition=ec.element_to_be_clickable):
    return find_element(driver, selector, By.ID, timeout, condition)


def find_element_by_link_text(driver, selector, timeout=10, condition=ec.element_to_be_clickable):
    return find_element(driver, selector, By.LINK_TEXT, timeout, condition)


def enter(driver, xpath, text, *args, **kwargs):
    element = find_element_by_xpath(driver, xpath, *args, **kwargs)
    element.clear()
    element.send_keys(text)


def open_new_tab(driver):
    driver.execute_script("window.open();")


def switch_to(driver, n):
    driver.switch_to.window(driver.window_handles[n])


def open_and_switch_to_tab(driver):
    open_new_tab(driver)
    time.sleep(0.1)
    switch_to(driver, -1)
