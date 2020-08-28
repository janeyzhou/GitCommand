# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 2020817
# @File      : start_ui.py
# @Desc      : Define the test case execution entrance
import os
import sys

import pytest

from Utils.core import parse_csv_data



def call_pytest():
    """Define test case execution command"""
    root = os.path.join(os.path.dirname(__file__), "")
    exitcode = pytest.main(
        [
            root,
            f"-k test_api.py",
            "--alluredir=API/reports"
        ]
    )
    return exitcode


if __name__ == '__main__':
    running_result = call_pytest()
    sys.exit(running_result)
