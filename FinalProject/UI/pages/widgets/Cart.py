# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200214
# @File      : Cart.py
# @Desc      : Define a cart widget and be called by any page which include this section

from selenium.webdriver.common.by import By

from UI.pages.BasePage import BasePage


class Cart(BasePage):
    """Get Products information from cart, e.g. total amount, total price and product details"""

    # Cart locator
    product_amount_locator = (By.CSS_SELECTOR, ".badge.badge-secondary.badge-pill")
    cart_locator = (By.CSS_SELECTOR, ".list-group.mb-3>li")
    product_name_quantity_locator = (By.XPATH, "//ul[@class='list-group mb-3']/li/div")
    product_total_price_locator = (By.XPATH,"//ul[@class='list-group mb-3']/li/span")
    total_price = (By.CSS_SELECTOR, ".list-group.mb-3>li:last-child")

    def get_Your_Cart_product_amount(self):
        """Get your cart amount"""
        amount = self.get_element_text(self.product_amount_locator)
        return int(amount)

    def get_cart_list_product_amount(self):
        """Get product amount in cart list"""
        cart_list = self.find_elements(self.cart_locator)
        return len(cart_list)-2

    def get_products_name_quantity(self):
        return self.find_elements(self.product_name_quantity_locator)

    def get_products_total_price(self):
        return self.find_elements(self.product_total_price_locator)

    # def get_product_name(self, index):
    #     """Get the product name via index"""
    #     name_quantity = str(self.find_elements(self.product_name_quantity_locator)[index].text).splitlines()
    #     name = name_quantity[0]
    #     return name

    # def get_product_quantity(self, index):
    #     """Get the product quantity via index"""
    #     name_quantity = str(self.find_elements(self.product_name_quantity_locator)[index].text).splitlines()
    #     quantity = name_quantity[1].split(":")[1].strip()
    #     return int(quantity)
    #
    # def get_product_total_price(self, index):
    #     """Get one product's total price via index"""
    #     total_price_elements = self.find_elements(self.product_total_price_locator)
    #     return total_price_elements[index].text

    def get_total_price(self):
        """get the order total price"""
        total_price_element = self.find_element(self.total_price)
        total_price = str(total_price_element.text).splitlines()[1]
        return total_price


