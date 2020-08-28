# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200814
# @File      : PageFactory.py
# @Desc      : create a page factory to init a web driver
import logging
import os
from venv import logger

from selenium import webdriver


class PageFactory:
    @staticmethod
    def init_driver(driver_type='Chrome'):
        """init drivers from a given drivers type
        :param driver_type: browser type with default value as Chrome
        :return: web drivers
        """
        logging.info("init drivers...")

        if driver_type == 'Chrome':
            return webdriver.Chrome(os.path.join(os.path.dirname(__file__), '..', 'drivers/chromedriver.exe'))
        else:
            logger.info(f"Do not support {driver_type} currently")
