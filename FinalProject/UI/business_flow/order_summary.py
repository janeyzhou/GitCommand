# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200826
# @File      : order_summary.py
# @Desc      : Defined cart management functions
import logging
import operator

from deepdiff import DeepDiff

from UI.business_flow.header import verify_message, verify_cart_menu_product_amount
from UI.pages.OrderSummaryPage import OrderSummaryPage


def is_product_in_cart(driver, name):
    """Check if the product in your cart"""
    order_summary_page = OrderSummaryPage(driver)
    product_names = order_summary_page.get_products_name()
    flag = False
    for item in product_names:
        if item.text == name:
            flag = True
    return flag


def get_product_order_index(driver, product_name):
    """Get a product index via product name"""
    order_summary_page = OrderSummaryPage(driver)
    product_amount = order_summary_page.get_product_amount()
    if product_amount < 1:
        logging.error("You have not added any product to your cart, please check")
    else:
        product_name_elements = order_summary_page.get_products_name()
        if is_product_in_cart(driver, product_name):
            order_index = 0
            for i in range(product_amount):
                if str(product_name_elements[i].text).strip() == product_name:
                    order_index = i
            return order_index
        else:
            logging.error(f"{product_name} has not been added in cart, please check.")


def get_product_name(driver, index):
    """Get a product name via index"""
    order_summary_page = OrderSummaryPage(driver)
    product_amount = order_summary_page.get_product_amount()
    if index > product_amount - 1:
        logging.error("Your given product index is out of cart list, please check")
    else:
        return str(order_summary_page.get_products_name()[index].text)


def get_product_amount_in_cart(driver):
    osp = OrderSummaryPage(driver)
    return osp.get_product_amount()


def get_product_detail_in_cart(driver, name):
    """Return a product information from your cart as a dictionary, composed of name, price, quantity and total price"""
    osp = OrderSummaryPage(driver)
    index = get_product_order_index(driver, name)
    name = osp.get_products_name()[index].text
    price = str(osp.get_products_price()[index].text).strip()
    qty = int(str(osp.get_products_quantity()[index].text).strip())
    total_price = str(osp.get_products_total_price()[index].text).strip()
    product_detail_dict = {"Product Name": name, "Price": price, "Qty": qty, "Total Price": total_price}
    return product_detail_dict


def update_quantity_in_cart(driver, name, added_amount=0, reduced_amount=0):
    """Add or reduct quantity for an product via index"""
    order_summary_page = OrderSummaryPage(driver)
    index = get_product_order_index(driver, name)
    if added_amount > 0:
        logging.info(f"Add [{added_amount}] product quantity to product [{name}] in your cart")
        order_summary_page.add_quantity(index, added_amount)
        verify_message(driver, "Item qty was updated.")
    if reduced_amount > 0:
        logging.info(f"Reduce [{reduced_amount}] product quantity to product [{name}] in your cart")
        order_summary_page.reduce_quantity(index, reduced_amount)
        verify_message(driver, "Item qty was updated.")


def remove_product_from_cart(driver, name):
    """Remove product from your cart"""
    logging.info(f"Remove product [{name}] from your cart")
    order_summary_page = OrderSummaryPage(driver)
    index = get_product_order_index(driver, name)
    order_summary_page.remove_product(index)
    verify_message(driver, "Item was removed from your cart.")
    verify_cart_menu_product_amount(driver)


def checkout_from_order_summary(driver):
    """Checkout from order summary page"""
    logging.info("Checkout from order summary page")
    order_summary_page = OrderSummaryPage(driver)
    order_summary_page.click_check_out_button()


def continue_shopping_from_order_summary(driver):
    logging.info("Continue shopping from order summary page")
    order_summary_page = OrderSummaryPage(driver)
    order_summary_page.click_continue_shopping_button()

def verify_product_in_cart(driver, name):
    flag = is_product_in_cart(driver, name)
    if flag:
        logging.info(f"Product [{name}] is in cart")
    else:
        logging.error(f"Product [{name}] is not in cart")
    return flag
