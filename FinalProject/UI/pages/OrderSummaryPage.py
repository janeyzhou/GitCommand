# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200821
# @File      : OrderSummaryPage.py
# @Desc      : Define locator, elements, cart management actions on order summary page
import time

from selenium.webdriver.common.by import By

from UI.pages.BasePage import BasePage


class OrderSummaryPage(BasePage):
    order_head = ["#", "Product Image", "Product Name", "Product Price", "Qty", "Total Price"]

    # Order list locator
    order_head_locator = (By.CSS_SELECTOR, ".table>thead th")
    product_order_index_locator = (By.XPATH, "//tbody//th")
    product_name_locator = (By.XPATH, "//tbody//td[2]")
    price_locator = (By.XPATH, "//tbody//td[3]")
    qty_locator = (By.XPATH, "//tbody//td[4]")
    total_price_locator = (By.XPATH, "//tbody//td[5]")

    # Buttons locator on order summary page
    remove_quantity_button_locator = (By.CSS_SELECTOR, ".table a[href*='remove-item-from-cart']")
    add_quantity_button_locator = (By.CSS_SELECTOR, ".table a[href*='add-to-cart']")
    delete_button_locator = (By.CSS_SELECTOR, "tbody td>a[href*='remove-from-cart']>i")
    order_total_locator = (By.CSS_SELECTOR, ".table>tbody>tr:nth-last-child(2)")
    check_out_button_locator = (By.CSS_SELECTOR, ".table a[href*='checkout']")
    continue_shopping_button_locator = (By.XPATH, "//tbody//a[text()='Continue Shopping']")

    def get_order_head(self):
        """Return order head as a list"""
        head_elements = self.find_elements(self.order_head_locator)
        head_list = []
        for item in head_elements:
            head_list.append(item.text)
        return head_list

    # Buttons operations
    def reduce_quantity(self, index, reduced_amount):
        """Reduce order's quantity, and verify the latest quantity
        index: the product index will be reduced
        reduced_amount: the quantity will be reduced
        """
        reduce_quantity_buttons = self.find_elements(self.remove_quantity_button_locator)
        origin_quantity = self.get_product_quantity(index)
        for i in range(reduced_amount):
            reduce_quantity_buttons[index].click()
        latest_quantity = self.get_product_quantity(index)
        expected_quantity = origin_quantity - reduced_amount
        assert latest_quantity == expected_quantity, f"The latest quantity is {latest_quantity}, it should be {expected_quantity} "

    def add_quantity(self, index, added_amount):
        """Add order's quantity, and verify the latest quantity
        index: the product index will be added
        added_amount: the quantity will be added
        """
        origin_quantity = self.get_product_quantity(index)
        add_quantity_buttons = self.find_elements(self.add_quantity_button_locator)
        for i in range(added_amount):
            add_quantity_buttons[index].click()
            time.sleep(2)
        latest_quantity = self.get_product_quantity(index)
        expected_quantity = origin_quantity + added_amount
        assert latest_quantity == expected_quantity, f"The latest quantity is {latest_quantity}, it should be {expected_quantity} "

    def remove_product(self, index):
        """Remove one product from cart, and verify the product amount, and the deleted product does not display any more
        index: the product index will be removed
        """
        origin_product_amount = self.get_product_amount()
        remove_product_buttons = self.find_elements(self.delete_button_locator)
        remove_product_buttons[index].click()
        latest_product_amount = self.get_product_amount()
        assert latest_product_amount == origin_product_amount - 1, f"The latest product amount is {latest_product_amount}, it should be reduced 1"

    def click_check_out_button(self):
        """Click checkout button"""
        self.click(self.check_out_button_locator)

    def click_continue_shopping_button(self):
        """Click continue shoppping button"""
        self.click(self.continue_shopping_button_locator)
        time.sleep(2)

    # Order list operations
    def get_products_name(self):
        return self.find_elements(self.product_name_locator)

    def get_products_price(self):
        return self.find_elements(self.price_locator)

    def get_products_quantity(self):
        return self.find_elements(self.qty_locator)

    def get_products_total_price(self):
        return self.find_elements(self.total_price_locator)

    def get_product_name(self, index):
        """Get a product name via index"""
        product_name_elements = self.find_elements(self.product_name_locator)
        return product_name_elements[index].text

    def get_product_price(self, index):
        """Get a product price via index"""
        product_price_elements = self.find_elements(self.price_locator)
        product_price = str(product_price_elements[index].text).strip()
        return product_price

    def get_product_quantity(self, index):
        """Get a product quantity via index"""
        product_quantity_elements = self.find_elements(self.qty_locator)
        quantity = str(product_quantity_elements[index].text).strip()
        return int(quantity)

    def get_product_total_price(self, index):
        """Get a product total price via index"""
        product_total_price_elements = self.find_elements(self.total_price_locator)
        total_price = str(product_total_price_elements[index].text).strip()
        return total_price

    def get_order_total_price(self):
        """Return the order total price"""
        order_total = str(self.find_element(self.order_total_locator).text).split(":")
        return order_total[1].strip()

    def get_product_amount(self):
        """Return the total product amount in your cart"""
        order_elements = self.find_elements(self.product_order_index_locator)
        return len(order_elements)


