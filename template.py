#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" apple.py """
# pylint: disable=missing-docstring
# @imports

import json
import math
import os
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path  # requires python >= 3.4
from typing import Any, Dict, List, Tuple

import requests

import numpy as np
import pandas as pd

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

# @info
name = "apple.py"

# @functions


def create_usage(data: Dict) -> str:
    """ Create program usage info from json file. """
    usage = data["name"]
    return usage


def create_version(data: Dict) -> str:
    """ Create program version info from json file. """
    usage = data
    print(data)
    return 'test'


class Project:
    """ setup and track projects """

    def __init__(self,
                 init_name: str = 'test',
                 init_description: str = 'test project'):
        self.version = '0.0.1'
        self.name = init_name
        self.py_file_name = self.name + '.py'
        self.json_file_name = self.name + '.json'
        self.description = init_description
        self.json_data: Dict = {}
        self.cli: bool = True
        self.path: Path = Path()
        self.here: str = self.path.resolve()
        self.here: str = ''

    def get_json(self) -> Dict:
        """ Read program info from json file. """
        with open(self.json_file_name, "r") as read_file:
            data = json.load(read_file)
        return data

    def put_json(self, data: Dict) -> int:
        """ Write program info to json file. """
        with open(self.json_file_name, "w") as write_file:
            json.dump(data, write_file)
        return 0

    def print_version(self) -> str:
        """ Print version if CLI else #TODO dialog """
        if self.cli:
            print(self.name, " version: ", self.version)
        else:
            pass
        return 'test'

    def help(self) -> str:
        """ Print usage and help if CLI else #TODO dialog? """
        pass


p1 = Project('test',
             'Test project to see if my automation script is working ...')
