# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200818
# @File      : CheckoutPage.py
# @Desc      : Define billing address and payment locator, payment action
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from UI.pages.BasePage import BasePage


class CheckoutPage(BasePage):

    """Define billing address and payment locator, payment action"""

    # Billing address locator
    address_locator = (By.NAME, "street_address")
    country_locator = (By.NAME, "country")
    city_locator = (By.ID, "state")
    zip_locator = (By.NAME, "zip")

    # Payment locator
    paypal_locator = (By.CSS_SELECTOR, "#PayPal~label")
    stripe_locator = (By.ID, "#Stripe~label")
    continue_checkout_locator = (By.CSS_SELECTOR, "form>button")

    def input_address(self, address):
        """Input address"""
        self.input_text(self.address_locator, address)

    def select_country(self, country_name):
        """Select country from drop down list"""
        country_dropdown = self.find_element(self.country_locator)
        Select(country_dropdown).select_by_visible_text(country_name)

    def select_city(self, city_name):
        """Select city from drop down list according to the selected country"""
        city_dropdown = self.find_element(self.city_locator)
        Select(city_dropdown).select_by_visible_text(city_name)

    def input_zip(self, zip):
        """Input zip"""
        self.input_text(self.zip_locator, zip)

    def chose_payment_type(self, payment_type):
        """Chose a payment type by radio button"""
        if payment_type == 'PayPal':
            self.click(self.paypal_locator)
        elif payment_type == 'Stripe':
            self.click(self.stripe_locator)
        else:
            logging.error("Only support PayPal and Stripe...")

    def click_continue_checkout_button(self):
        """click continue checkout button"""
        self.click(self.continue_checkout_locator)

    def verify_current_page_is_checkout_page(self):
        url = self.driver.current_url
        assert str(url).find("checkout") >= 0, "Current url does not contain checkout, this is not checkout page"

