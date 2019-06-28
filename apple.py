#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" apple.py """
# pylint: disable=missing-docstring
# @imports
import json  # requires python >= 2.6
import os
import sys
from pathlib import Path  # requires python >= 3.4
from typing import Dict

import requests

# @info
# __name__ = "apple.py"

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
                 init_description: str = 'test project',
                 init_version: str = '0.0.1',
                 init_filename: str = '',
                 init_type: str = 'python_cli',):
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
            # if gui, show dialog
            pass
        return 'test'

    def help(self) -> str:
        """ Print usage and help if CLI else #TODO dialog? """
        if self.cli:
            print(self.help_text)
        else:
            # if gui, show dialog
            pass
        return 'test'


p1 = Project('test',
             'Test project to see if my automation script is working ...')

print(__name__)
__
