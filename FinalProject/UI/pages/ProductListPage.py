# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Ruby Peng <Ruby_Peng@epam.com>
# @Datetime  : 20200818
# @File      : PageDetailPage.py
# @Desc      : create a page factory to init a web drivers

import logging
from selenium.webdriver.common.by import By
from UI.pages.BasePage import BasePage


class ProductListPage(BasePage):
    # Define Product List Page and locator for product Aaa
    # Product Aaa locator
    Aaa_locator = (By.LINK_TEXT, "Aaa")

    product_name_locator = (By.CSS_SELECTOR, "a[href*='product']")

    # Title locator
    Aaa_title_locator = (By.CSS_SELECTOR, "h4[class='product-detail-name m-text16 p-b-13']")

    def verify_PDP(self):
        Title = self.find_element(self.Aaa_title_locator).text
        print(Title)
        logging.info(Title)
        assert Title == 'Aaa'

    def click_one_product(self, product_name):
        product_name_elements = self.find_elements(self.product_name_locator)
        for item in product_name_elements:
            if str(item.text).strip() == product_name:
                item.click()
                break
