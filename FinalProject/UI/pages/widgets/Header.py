# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200818
# @File      : Header.py
# @Desc      : Define a header widget and be called by any page which include header
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from UI.pages.BasePage import BasePage


class Header(BasePage):
    """Define header element and actions on each menu"""

    # Header menu locator
    home_menu_locator = (By.XPATH, "//div[@class='wrap_menu']//ul//a[contains(text(), 'Home')]")
    shop_menu_locator = (By.CSS_SELECTOR, ".main_menu a[href*='shop']")
    cart_menu_locator = (By.CSS_SELECTOR, ".main_menu a[href*='order-summary']")
    login_menu_locator = (By.CSS_SELECTOR, "//div[@class='wrap_menu']//ul//a[contains(text(), 'Login')]")
    login_sub_menu_locator = (By.CSS_SELECTOR, ".main_menu a[href*='accounts/login']")

    # Message locator
    message_locator = (By.CSS_SELECTOR, ".mt-2>div")

    def click_home_menu(self):
        """Click home menu"""
        self.click(self.home_menu_locator)

    def click_shop_menu(self):
        """Click shop menu"""
        self.click(self.shop_menu_locator)
        time.sleep(2)

    def click_cart_menu(self):
        """Click cart menu"""
        self.click(self.cart_menu_locator)
        time.sleep(2)

    def is_cart_menu_displayed(self):
        """Check if the cart menu displays on menu bar"""
        return self.is_element_displayed(self.cart_menu_locator)

    def click_login_sub_menu(self):
        """Hover on Login menu and then click login sub menu to open login page"""
        login_menu = self.find_element(self.login_menu_locator)
        ActionChains(self.driver).move_to_element(login_menu).perform()
        self.click(self.login_sub_menu_locator)

    def get_message(self):
        """Get the message display on home page and return the message"""
        message = self.get_element_text(self.message_locator)
        return str(message).splitlines()[0].strip()

