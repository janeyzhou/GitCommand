# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200827
# @File      : home.py
# @Desc      : Define functions on home page
import logging

from UI.pages.HomePage import HomePage


def verify_current_page_is_home(driver):
    home_page = HomePage(driver)
    flag = home_page.is_slide_section_displayed()
    assert flag
    if flag:
        logging.info("Current page is home page")
    else:
        logging.error("Current page is not home page")
    return flag
