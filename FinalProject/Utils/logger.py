# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200817
# @File      : logger.py
# # @Desc      : Init logging to print to console and save to text file
import logging
import os
import sys


def init_logger(path):
    """Init a logger with specified logger level and logger format, add console handler and file handler"""
    logger = logging.getLogger()

    logger_level = logging.INFO
    logger_format = logging.Formatter('[%(levelname)s] [%(asctime)s] : %(message)s', "%Y-%m-%d %H:%M:%S")

    logger.setLevel(logger_level)

    console = logging.StreamHandler(stream=sys.stdout)
    console.setLevel(logger_level)
    console.setFormatter(logger_format)
    logger.addHandler(console)

    log_file = os.path.join(os.path.dirname(__file__), '..', f"{path}")
    file_console = logging.FileHandler(log_file, mode='w')
    file_console.setLevel(logger_level)
    file_console.setFormatter(logger_format)
    logger.addHandler(file_console)

