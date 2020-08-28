# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Ruby Peng <Ruby_Peng@epam.com>
# @Datetime  : 20200818
# @File      : PageDetailPage.py
# @Desc      : create a page factory to init a web drivers

import time

from selenium.webdriver.common.by import By
from UI.pages.BasePage import BasePage
from selenium.webdriver.support.select import Select


class ProductDetailPage(BasePage):
    # "Define Product Detail Page"
    # Sizes locator
    sizes_locator = (By.NAME, 'size')

    # Colors locator
    colors_locator = (By.NAME, 'color')

    # Quantity locator
    quantity_locator = (By.NAME, 'num-product')

    # Add to cart button locator
    addtocart_locator = (By.CSS_SELECTOR, "a[href*='add-to-cart']")

    def select_size(self, size_name):
        # Select size from drop down list
        size_dropdown = self.find_element(self.sizes_locator)
        Select(size_dropdown).select_by_visible_text(size_name)

    def select_color(self, color_name):
        """Select color from drop down list"""
        color_dropdown = self.find_element(self.colors_locator)
        Select(color_dropdown).select_by_visible_text(color_name)

    def input_quantity(self, quantity):
        """Input quantity"""
        self.input_text(self.quantity_locator, quantity)

    def add_to_cart(self):
        self.click(self.addtocart_locator)
        time.sleep(2)
