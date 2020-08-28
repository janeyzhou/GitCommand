# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200814
# @File      : HomePage.py
# @Desc      : Define home page url, title, message and velidation
from selenium.webdriver.common.by import By

from UI.pages.BasePage import BasePage
from config.GetConfig import cfg


class HomePage(BasePage):
    """Define home page url, title, message and velidation"""

    # Read domain from config/cfg.ini according to the specified test environment
    # Combine the domain and home page resource to home page url
    url = cfg.Domain

    slide_locator = (By.CSS_SELECTOR, ".wrap-slick1")

    def go_to_home_page(self):
        """Open home page"""
        self.driver.get(self.url)

    def is_slide_section_displayed(self):
        return self.is_element_displayed(self.slide_locator)

    def verify_home_page_title(self):
        """Verify home page title"""
        current_title = self.driver.title
        expected_title = self.title
        assert current_title == expected_title, f"Current title is {current_title}, it should be {expected_title}"

