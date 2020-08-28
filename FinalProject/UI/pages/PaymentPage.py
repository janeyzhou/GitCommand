# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200818
# @File      : PaymentPae.py
# @Desc      : Define card locator, input card information and payment action
import time

from selenium.webdriver.common.by import By

from UI.pages.BasePage import BasePage


class PaymentPage(BasePage):
    """Define card information and payment action"""

    # Payment form locator
    card_frame_locator = (By.CSS_SELECTOR, "#card-element>div>iframe")
    card_number_locator = (By.CSS_SELECTOR, ".CardNumberField-input-wrapper>span>input")
    card_expired_date_locator = (By.CSS_SELECTOR, ".CardField-expiry.CardField-child span>input")
    card_cvc_locator = (By.CSS_SELECTOR, ".CardField-cvc.CardField-child span>input")
    submit_payment_locator = (By.CSS_SELECTOR, ".new-card-form div>button[id='stripeBtn']")

    def switch_to_card_frame(self):
        """Switch to card information frame"""
        card_element = self.find_element(self.card_frame_locator)
        self.driver.switch_to.frame(card_element)

    def input_card_number(self, card_number):
        """Input card number"""
        self.input_text(self.card_number_locator, card_number)

    def input_card_expired_date(self, expired_date):
        """Input card expired date"""
        self.input_text(self.card_expired_date_locator, expired_date)

    def input_card_cvc(self, cvc):
        """Input card CVC value"""
        self.input_text(self.card_cvc_locator, cvc)

    def click_submit_payment_button(self):
        """Click submit button to complete payment"""
        self.click(self.submit_payment_locator)
        time.sleep(2)









