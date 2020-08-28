# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200826
# @File      : checkout.py
# @Desc      : Define functions to set address and payment type
import logging

from UI.pages.CheckoutPage import CheckoutPage


def set_address(driver, billing_address, country, city, zip):
    """Set address for your order"""
    logging.info(f"Set address as [{billing_address}, {country}, {city}, {zip}]")
    checkout_page = CheckoutPage(driver)
    checkout_page.input_address(billing_address)
    checkout_page.select_country(country)
    checkout_page.select_city(city)
    checkout_page.input_zip(zip)


def checkout_order_to_pay(driver, payment_type):
    """Select payment type and checkout to pay"""
    logging.info(f"Select [{payment_type}] and pay")
    checkout_page = CheckoutPage(driver)
    checkout_page.chose_payment_type(payment_type)
    checkout_page.click_continue_checkout_button()

