# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200826
# @File      : product.py
# @Desc      : Define functions to chose products
import logging

from UI.pages.ProductDetailPage import ProductDetailPage
from UI.pages.ProductListPage import ProductListPage
from UI.pages.widgets.Header import Header

def select_product(driver, page, product_name):
    """Select a product on the website page"""
    logging.info(f"select product [{product_name}] from [{page}] page")
    header = Header(driver)
    if page == "Shop":
        header.click_shop_menu()
    product_list_page = ProductListPage(driver)
    product_list_page.click_one_product(product_name)



def add_product_to_cart(driver, size, color, quantity):
    """Select size, color, quantity and add to cart"""
    logging.info(f"Set product size: [{size}], color: [{color}], quantity: [{quantity}] and add to cart")
    product_detail_page = ProductDetailPage(driver)
    product_detail_page.select_size(size)
    product_detail_page.select_color(color)
    product_detail_page.input_quantity(quantity)
    product_detail_page.add_to_cart()