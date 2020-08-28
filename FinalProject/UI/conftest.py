# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200814
# @File      : conftest.py
# @Desc      : Setup test, e.g. Init driver, take screenshot for failed test case
import logging

import allure
import pytest

from UI.business_flow.login_flow import login
from UI.pages.PageFactory import PageFactory
from start_ui import TEST_RUNNER
from Utils.logger import init_logger


@pytest.fixture(scope="module", autouse=True)
def driver(request):
    """Init drivers and then login fashe website"""
    init_logger(path="UI/reports/UI_log.log")
    logging.info("setup session")
    # driver = PageFactory.init_driver(driver_type="Chrome")
    driver = PageFactory.init_driver(driver_type=TEST_RUNNER[0]['browser'])
    # login(driver, "j_zhou", "123456")
    login(driver, TEST_RUNNER[0]['username'], TEST_RUNNER[0]['password'])

    def fn():
        # pass
        driver.quit()


    request.addfinalizer(fn)
    return driver


@pytest.fixture(scope="function", autouse=True)
def take_screenshot(request, driver):
    """Catch screenshot when test case failed"""
    yield
    if request.session.testsfailed:
        allure.attach(driver.get_screenshot_as_png(),
                      name=request.function.__name__,
                      attachment_type=allure.attachment_type.PNG)
