# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 20200214
# @File      : GetConfig.py
# @Desc      : Get each config information
import os

from start_ui import TEST_RUNNER
from Utils.ParseConfig import ParseConfig


class GetConfig(ParseConfig):
    """Get config content"""
    def __init__(self):
        config_path = os.path.join(os.path.dirname(__file__), 'cfg.ini')
        super().__init__(config_path)

        # self.Domain = self.get("PPE", "DOMAIN") if TEST_RUNNER[0]["env"] == "PPE" else self.get("DEV", "DOMAIN")


        self.Domain = self.get("PPE", "DOMAIN") if self.get("Default", "PPE") else self.get("DEV", "DOMAIN")


cfg = GetConfig()