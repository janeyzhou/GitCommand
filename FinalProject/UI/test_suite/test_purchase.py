# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200814
# @File      : test_purchase.py
# @Desc      : Define purchase scenario, e.g. view product detail, add to cart and payment
import os

from UI.business_flow.cart import *
from UI.business_flow.checkout import set_address, checkout_order_to_pay
from UI.business_flow.home import verify_current_page_is_home
from UI.business_flow.order_summary import *
from UI.business_flow.payment import pay_order
from UI.business_flow.product import select_product, add_product_to_cart
from UI.pages.widgets.Header import Header

from Utils.core import parse_json_data


def setup_session():
    logging.info("setup session...")


def teardown_session():
    logging.info("teardown session...")


def setup_module(self):
    logging.info("setup module...")


def teardown_module(self):
    logging.info("teardown module...")


class TestPurchase:
    """Test purchase products work flow"""

    def setup_class(cls):
        logging.info("setup class...")
        logging.info("Get test data from csv file")
        test_data_file = os.path.join(os.path.dirname(__file__), '..', 'test_data/purchase_products.json')
        cls.test_data = parse_json_data(test_data_file)

    def teardown_class(cls):
        logging.info("teardown class....")

    def setup_method(self):
        logging.info("setup method...")

    def teardown_method(self):
        logging.info("teardown method...")

    def test_purchase_products(self, driver):
        """Add product to cart, checkout and then payment"""
        logging.info("Start test case: checkout product successfully")
        products = self.test_data["Purchase Products"]["Products"]
        address = self.test_data["Purchase Products"]["Address"]
        payment_info = self.test_data["Purchase Products"]["Payment Info"]
        logging.info(f"Test Data: {self.test_data['Purchase Products']}")

        select_product(driver, products[0]["Page"], products[0]["Product Name"])
        add_product_to_cart(driver, products[0]["Size"], products[0]["Color"], products[0]["Quantity"])
        checkout_from_order_summary(driver)
        set_address(driver, address["Billing Address"], address["Country"], address["City"], address["Zip"])
        checkout_order_to_pay(driver, payment_info["Payment Type"])
        pay_order(driver, payment_info["Card ID"], payment_info["Expired Date"], payment_info["CVC"])
        verify_message(driver, "Order was successful")

    def test_add_product_to_cart(self, driver):
        """Add product to cart and continue shopping"""
        logging.info("Start test case: Continue Shop")
        data = self.test_data["Continue Shop"]["Products"][0]
        logging.info(f"Test data: [{data}]")
        product_name = data["Product Name"]

        select_product(driver, data["Page"], product_name)
        add_product_to_cart(driver, data["Size"], data["Color"], data["Quantity"])
        assert is_product_in_cart(driver, product_name)
        continue_shopping_from_order_summary(driver)
        assert verify_current_page_is_home(driver)


    def test_update_cart(self, driver):
        """Test Add quantity, remove product and continue shop function on order summary page
        Precondition: already have two product in order summary"""

        logging.info("Start test case: Edit product in orderSummary")
        data = self.test_data["Edit product in orderSummary"]
        products = data["Products"]
        logging.info("Test data: {}".format(products))

        for i in range(len(products)):
            select_product(driver, products[i]["Page"], products[i]["Product Name"])
            add_product_to_cart(driver, products[i]["Size"], products[i]["Color"], products[i]["Quantity"])

        added_name = get_product_name(driver, index=data["Added Index"] - 1)
        update_quantity_in_cart(driver, name=added_name, added_amount=data["Added Amount"])
        expected_qty = get_product_detail_in_cart(driver, added_name)["Qty"]

        removed_name = get_product_name(driver, index=data["Removed Index"] - 1)
        remove_product_from_cart(driver, name=removed_name)
        expected_amt = get_product_amount_in_cart(driver)

        checkout_from_order_summary(driver)
        actual_amt = get_product_amount_in_order(driver)
        actual_qty = get_product_detail_in_order(driver, added_name)["Qty"]
        logging.info("Verify product amount and product quantity on checkout page")
        assert actual_amt == expected_amt, f"your cart product amount is {actual_amt}, it should be {expected_amt}"
        assert actual_qty == expected_qty, f"The quantity of added product {added_name} is {actual_qty}, it should be {expected_qty}"
        assert not verify_product_in_order(driver, removed_name)

    def test_order_summary_display(self, driver):
        """Verify the cart table header on ordere summary page"""
        header = Header(driver)
        header.click_cart_menu()
        order_summary_page = OrderSummaryPage(driver)
        assert order_summary_page.order_head == order_summary_page.get_order_head(), "order summary table header is wrong, please check"



