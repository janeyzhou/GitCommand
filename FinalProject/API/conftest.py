# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200821
# @File      : conftest.py
# @Desc      : Setup tet, e.g. get token
import os

import pytest

from API.APIRequsts.coreAPI import login
from Utils.core import parse_json_data
from Utils.logger import init_logger


@pytest.fixture(scope="session", autouse=True)
def token(request):
    """login with valid useraccount and return token"""
    init_logger(path="API/reports/API_log.log")
    test_data_path = os.path.join(os.path.dirname(__file__), "test_data/data.json")
    user_account = parse_json_data(test_data_path)["User Account"]
    token = login(user_account)
    return token

