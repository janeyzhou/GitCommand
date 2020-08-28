# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200821
# @File      : common.py
# @Desc      : Define some common functions to operate the response data
import logging

from API.APIRequsts.coreAPI import get_specified_item, post_cart_items, get_cart_items


def get_item_id(slug):
    res = get_specified_item(slug).json()
    return res["id"]


def get_quantity(token, slug):
    cart_items = get_cart_items(token).json()
    updated_slug_id = get_item_id(slug)
    qty = ''
    flag = False
    for item in cart_items:
        if item["item"] == updated_slug_id:
            qty = item["quantity"]
            flag = True
            return qty
    if flag == False:
        logging.error(f"The slug [{slug}] does not exist in your cart")





