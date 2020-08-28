# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200821
# @File      : test_api.py
# @Desc      : Test the API of items, cart_items and order_cart
import logging
import os

from API.APIRequsts.common import get_quantity
from API.APIRequsts.coreAPI import *
from Utils.core import parse_json_data


def setup_session():
    logging.info("setup session...")


def teardown_session():
    logging.info("teardown session...")


def setup_module(self):
    logging.info("setup module...")


def teardown_module(self):
    logging.info("teardown module...")


class TestAPI:
    """Test the API of items, cart_items and order_cart"""

    def setup_class(cls):
        """Get test data and used in according API"""
        test_data_path = os.path.join(os.path.dirname(__file__), '..', "test_data/data.json")
        cls.test_data = parse_json_data(test_data_path)

    def teardown_class(cls):
        logging.info("teardown class ...")

    def setup_method(self):
        logging.info("setup method...")

    def teardown_method(self):
        logging.info("teardown method...")

    def test_item(self):
        """Get one item with specified slug, verify the status code and slug value"""
        logging.info("Start test case: get item")
        data = self.test_data["Test Items"]
        logging.info(f"Test data: [{data}]")
        get_item = get_specified_item(data["slug"])
        res = get_item.json()
        assert get_item.status_code == 200, f"The status_code is {get_item.status_code}"
        assert res['slug'] == data["slug"], f"Item slug is {res['slug']}, it should be {data['slug']}"


    def test_all_items(self):
        """Test get all items works"""
        logging.info("Start test case: get all items")
        get_items = get_all_items()
        assert get_items.status_code == 200, f"The status_code is {get_items.status_code}"


    def test_get_cart_items(self, token):
        """Test get cart items work"""
        logging.info("Start test case: get cart items")
        get_cart = get_cart_items(token)
        assert get_cart.status_code == 200, f"The status code is {get_cart.status_code}"


    def test_post_cart_items(self, token):
        logging.info("Start test case: post cart items")
        body = self.test_data["Test Card Items"]
        logging.info(f"Test data: [{body}]")
        post_cart = post_cart_items(token, body)
        res = post_cart.json()
        act_qty = get_quantity(token, body["slug"])
        assert post_cart.status_code == 200, f"The status_code is {post_cart.status_code}"
        assert res == "update successfully", f"Return message is [{res}]"
        assert act_qty == body['quantity'], f"The quantity of slug [{body['slug']}] is {act_qty}, it should be {body['quantity']}"


    def test_order_cart(self, token):
        """Add one item to order cart, and then check the item is added to order cart"""

        """Get the order cart items"""
        logging.info("Start test caes: test order cart")
        get_order_items_res1 = get_order_cart(token)
        order = get_order_items_res1.json()

        order_items1 = order[0]["items"]
        number1 = len(order_items1)

        """Post a request to add a item to order cart"""
        body = self.test_data["Test Order Items"]
        logging.info(f"Test data: [{body}]")
        update_order_res = post_order_cart(token, body)
        message = update_order_res.json()
        assert update_order_res.status_code == 200, f"The status_code is {update_order_res.status_code}"
        assert message == "add to cart", f"Return message is [{message}]"

        """Get the order cart items again, and check wheather the new data is added"""
        get_order_items_res2 = get_order_cart(token)
        order = get_order_items_res2.json()
        order_items2 = order[0]["items"]
        number2 = len(order_items2)
        assert number2 == number1 + 1, f"The cart item should be added to {number1 + 1}"

