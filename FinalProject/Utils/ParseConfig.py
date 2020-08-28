# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 2020817
# @File      : ParseConfig.py
# @Desc      : Parse config information
from configparser import ConfigParser, ExtendedInterpolation


class ParseConfig:
    """Define a new class to parse config content"""
    def __init__(self, file_path):
        self.config_content = ConfigParser(allow_no_value=True, interpolation=ExtendedInterpolation())
        self.config_content.read(file_path)

    def get(self, section, key):
        """Get config value by section and key"""
        return self.config_content.get(section, key)
