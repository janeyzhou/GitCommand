# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200814
# @File      : LoginPage.py
# @Desc      : Define login form locator and login action
import time

from selenium.webdriver.common.by import By

from UI.pages.BasePage import BasePage
from config.GetConfig import cfg


class LoginPage(BasePage):
    """Login form and login action"""

    # Read domain from config/cfg.ini according to the specified test environment
    # Combine the domain and login page resource to login page url
    url = f'{cfg.Domain}/accounts/login/'

    # Login form locator
    username_locator = (By.NAME, 'login')
    password_locator = (By.NAME, 'password')
    sign_in_locator = (By.CSS_SELECTOR, "button[class= 'btn btn-primary']")

    def go_to_login_page(self):
        """Open login page"""
        self.driver.get(self.url)

    def input_username(self, username):
        """Set username"""
        self.input_text(self.username_locator, username)

    def input_password(self, password):
        """Set password"""
        self.input_text(self.password_locator, password)

    def click_login_button(self):
        """Click login button"""
        self.click(self.sign_in_locator)
        time.sleep(2)

