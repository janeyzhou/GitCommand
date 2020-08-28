# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200814
# @File      : BasePage.py
# @Desc      : Overwrite some common functions from WebDriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Overwrite some common functions from WebDriver
    e.g. find_element, find_elements, input_text, click and so on
    """

    def __init__(self, driver):
        """Init BasePage with a WebDriver"""
        self.driver = driver
        self.driver.maximize_window()

    def find_element(self, locator):
        """Overwrite find element"""
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """Overwrite find elements"""
        return self.driver.find_elements(*locator)

    def wait_elements(self, locator):
        """Wait elements to be visible for 10s"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))

    def is_element_displayed(self, locator):
        """Wait elements for 10s and check if element displayed"""
        self.wait_elements(locator)
        elements = self.find_elements(locator)
        if len(elements) > 0:
            return True
        else:
            return False

    def input_text(self, locator, text):
        """Overwrite send_keys"""
        self.wait_elements(locator)
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        """Overwrite click"""
        self.wait_elements(locator)
        self.find_element(locator).click()

    def get_element_text(self, locator):
        """Get the element text"""
        self.wait_elements(locator)
        return self.find_element(locator).text




