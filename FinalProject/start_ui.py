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



# TEST_RUNER is defined as a global variable and get value from test case runner matrix, this matrix defines
# environment, browser, login account, and executed test case

global TEST_RUNNER
TEST_RUNNER = parse_csv_data(os.path.join(os.path.dirname(__file__), 'UI/test_case_runner.csv'))


def call_pytest():
    """Define test case execution command"""
    root = os.path.join(os.path.dirname(__file__), "")
    exitcode = pytest.main(
        [
            root,
            f"-k {TEST_RUNNER[0]['test_suite_name']}",
            "--alluredir=UI/reports"
        ]
    )
    return exitcode


if __name__ == '__main__':
    running_result = call_pytest()
    sys.exit(running_result)
