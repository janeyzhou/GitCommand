# !/usr/bin/env python
# encoding   : utf-8
# @Product   : Fashe
# @Project   : Team 1 Final Project
# @Author    : Janey Zhou <janey_zhou@epam.com>
# @Datetime  : 2020817
# @File      : core.py
# @Desc      : Define core functions, e.g. parse data, compare data
import csv
import json
import logging
import operator


def parse_json_data(path):
    """parse json data to python dictionary"""
    try:
        with open(path, 'r') as f:
            data = json.load(f)
            f.close()
        return data
    except Exception as e:
        logging.error(e)


def parse_csv_data(path):
    """parse csv data to python dictionary"""
    try:
        data_list = []
        with open(path, 'r') as f:
            data = csv.DictReader(f)
            for row in data:
                data_list.append(row)
            f.close()
        return data_list
    except Exception as e:
        logging.error(e)

