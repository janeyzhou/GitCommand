# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 2020819
# @File      : coreAPI.py
# @Desc      : Define all APIs for Fashe website
import requests

from config.GetConfig import cfg


def login(useraccount):
    """login with valid username and password, and return the key from response as token"""
    login_url = f"{cfg.Domain}/api/v1/rest-auth/login/"
    res = requests.post(url=login_url, json=useraccount)
    return res.json()["key"]


def get_all_items():
    """get all items"""
    get_all_items_url = f"{cfg.Domain}/api/items"
    res = requests.get(url=get_all_items_url)
    return res


def get_specified_item(slug):
    """get an item with the specified slug"""
    get_one_item_url = f"{cfg.Domain}/api/item/{slug}"
    res = requests.get(url=get_one_item_url)
    return res


def get_cart_items(token):
    """get the cart items for the login user account"""
    get_cart_items_url = f"{cfg.Domain}/api/cart_items"
    header = {"Authorization": f"{token}"}
    res = requests.get(url=get_cart_items_url, headers=header)
    return res


def post_cart_items(token, body):
    """update the quantity of the items in cart"""
    post_cart_items_url = f"{cfg.Domain}/api/cart_items"
    header = {"Authorization": f"{token}"}
    res = requests.post(url=post_cart_items_url, headers=header, json=body)
    return res


def get_order_cart(token):
    """Get the order cart items"""
    get_order_cart_url = f"{cfg.Domain}/api/order_cart"
    header = {"Authorization": f"{token}"}
    res = requests.get(url=get_order_cart_url, headers=header)
    return res

def post_order_cart(token, body):
    """Add item to order cart"""
    post_order_cart_url = f"{cfg.Domain}/api/order_cart"
    header = {"Authorization": f"{token}"}
    res = requests.post(url=post_order_cart_url, headers=header, json=body)
    return res

