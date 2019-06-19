#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" xargs.py """
# pylint: disable=missing-docstring
# @imports
import csv
import json

ESCAPE: str = "\x1B"


# class csv_dialect(csv.Dialect) -> csv.Dialect:

def conv_csv2json() -> int:  # Open the CSV
    try:
        with open('/path/to/filename.csv', 'rU') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            print(dialect)
            csvfile.seek(0)
            reader = csv.reader(csvfile, dialect)
            # reader = csv.DictReader(f, restkey='overflow')
    except (IOError, FileNotFoundError):
        return 1
    out = json.dumps([row for row in reader])
    try:
        with open('/path/to/parsed.json', 'w') as f:
            f.write(out)
    except (IOError, FileNotFoundError):
        return 1
    return 0


if True:
    import json
    import math
    import inspect
    import os
    import re
    import subprocess
    import sys
    from collections import Counter
    from pathlib import Path  # requires python >= 3.4
    from typing import Dict, List, Any, Tuple

    import numpy as np
    import pandas as pd
    import requests


def test_error(s: str) -> int:
    try:
        message = 'Code location {0.filename}@{0.lineno}:'.format(
            inspect.getframeinfo(inspect.currentframe()))
        # if LOG_ERRORS:
        print(message)
        return 0
    except:
        return 1


def l2s(l: List[str]) -> str:
    return ''.join(l)


def csv2json(csvfile: str) -> str:
    """ csv to json - single section only """
    reader = csv.DictReader(csvfile)
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')


def convert_csv2json(n: str, s: str) -> str:
    reader = csv.DictReader()
    result = '{\n\t"' + n + '": {\n'
    for line in s:
        if line.
        result += '\t\t"'
        line_list = line.split(',')
        for item in line_list:

        result +=


def bash(param_list: List[str]) -> Tuple[int, str]:
    result = subprocess.getstatusoutput(param_list)

    return result


param: List[str] = ['ls', '-lah']
output: Tuple[int, str] = bash(param)
if output[0] == 0:
    xargs_str = ''.join(output[1])
    print(xargs_str)
else:
    test_error("Error: " + output[0])
    message = 'Code location {0.filename}@{0.lineno}:'.format(
        inspect.getframeinfo(inspect.currentframe()))
    print(message)
