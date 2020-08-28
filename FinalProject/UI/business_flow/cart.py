# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200826
# @File      : cart.py
# @Desc      : xxx
import logging

from UI.pages.widgets.Cart import Cart


def get_product_amount_in_order(driver):
    """Get your cart amount"""
    cart = Cart(driver)
    return cart.get_Your_Cart_product_amount()


def is_product_name_in_order(driver, name):
    """Check if the product name in your cart"""
    cart = Cart(driver)
    product_name_element = cart.get_products_name_quantity()
    flag = False
    for item in product_name_element:
        if str(item.text).find(name) >= 0:
            flag = True
    return flag


def get_product_index(driver, name):
    """Get a product index in cart via product name"""
    cart = Cart(driver)
    flag = is_product_name_in_order(driver, name)
    product_name = cart.get_products_name_quantity()
    if flag:
        for i in range(cart.get_cart_list_product_amount()):
            product_name = str(product_name[i].text).split()[0]
            index = 0
            if product_name == name:
                index = i
            return index
    else:
        logging.error(f"The product name [{name}] can't be find in your cart, please check")


def get_product_detail_in_order(driver, name):
    try:

        cart = Cart(driver)
        index = get_product_index(driver, name)
        name_qty = str(cart.get_products_name_quantity()[index].text).splitlines()
        name = name_qty[0]
        qty = int(name_qty[1].split(":")[1].strip())
        total_price = str(cart.get_products_total_price()[index].text)
        product_detail_dict = {"Product Name": name, "Qty": qty, "Total Price": total_price}
        return product_detail_dict
    except Exception as e:
        logging.error(e)


def verify_product_in_order(driver, name):
    flag = is_product_name_in_order(driver, name)
    if flag:
        logging.info(f"Product [{name}] is in your order")
    else:
        logging.error(f"Product [{name}] is not in your order")
    return flag

