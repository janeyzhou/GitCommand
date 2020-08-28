# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200826
# @File      : header.py
# @Desc      : Define functions related with header
import logging
import re

from UI.pages.OrderSummaryPage import OrderSummaryPage
from UI.pages.widgets.Header import Header


def verify_login_message(driver, username):
    """Verify login message and check username display on success message"""
    logging.info("Veirfy login message")
    header = Header(driver)
    current_message = header.get_message()
    expect_message = f"Successfully signed in as {username}."
    assert current_message == expect_message, f"Current login message is {current_message}, it should be {expect_message}"

def verify_message(driver, message):
    """"Verify payment message"""
    logging.info(f"Verify message [{message}]")
    header = Header(driver)
    current_message = header.get_message()
    assert current_message == message, f"Current message is {current_message}, it should be {message}"


def get_cart_menu_product_amount(driver):
    """Return the product amount on cart menu"""
    header = Header(driver)
    cart_menu_product_amount = str(header.get_element_text(header.cart_menu_locator))
    amount = re.sub(r'\D', "", cart_menu_product_amount)
    return int(amount)


def verify_cart_menu_product_amount(driver):
    """Compare the product amount on cart menu with the product amount in order summary page"""
    logging.info("Verify product amount on cart menu")
    cart_menu_product_amount = get_cart_menu_product_amount(driver)
    order_summary_page = OrderSummaryPage(driver)
    order_summary_product_amount = order_summary_page.get_product_amount()
    assert cart_menu_product_amount == order_summary_product_amount, f"The amount in cart menu is {cart_menu_product_amount}, but the amount in order summary page is {order_summary_product_amount}"
