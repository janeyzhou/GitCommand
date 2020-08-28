# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200817
# @File      : login_flow.py
# @Desc      : login work flow
import logging

from UI.pages.LoginPage import LoginPage


def login(driver, username, password):
    """Login with username and password and verify login success"""
    logging.info(f"Login Fashe website with valid account [{username, password}]")
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.input_username(username)
    login_page.input_password(password)
    login_page.click_login_button()


