# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200826
# @File      : payment.py
# @Desc      : Define functions to pay
import logging

from UI.pages.PaymentPage import PaymentPage


def pay_order(driver, card_id, expired_date, cvc):
    """Pay your order with your card information"""
    logging.info(f"Pay your order with card:[{card_id}, {expired_date}, {cvc}]")
    payment_page = PaymentPage(driver)
    payment_page.switch_to_card_frame()
    payment_page.input_card_number(card_id)
    payment_page.input_card_expired_date(expired_date)
    payment_page.input_card_cvc(cvc)
    payment_page.driver.switch_to.default_content()
    payment_page.click_submit_payment_button()
