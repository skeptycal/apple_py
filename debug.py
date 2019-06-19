#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" py_crust.py - code wrapper, logger, and debugger """
# pylint: disable=missing-docstring
# @imports

import inspect
import json
import math
import os
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path  # requires python >= 3.4
from typing import Any, Dict, List, Tuple  # requires python >= 3.6

import numpy as np
import pandas as pd
import requests


class PyCrust():
    """ py_crust.py - code wrapper, logger, and debugger """


def test_error(s: str) -> int:
    message = 'Code location {0.filename}@{0.lineno}:'.format(
        inspect.getframeinfo(inspect.currentframe()))
    if LOG_ERRORS:
        if


Debug_config: Dict([str], [bool]) = {
    LOG_ERRORS: bool = True
    PRINT_ERRORS: bool = True
    TRAP_ERRORS: bool = True
}
LOG_ERRORS: bool = True
PRINT_ERRORS: bool = True
TRAP_ERRORS: bool = True


def xargs_get(param_list: List[str]) -> Tuple[int, str]:
    result = subprocess.getoutput(param_list)
    result = subprocess.getstatusoutput(param_list)
    # print(output)
    # result = result.stdout.decode('utf-8')
    return result


def print_list(l: List[str]) -> str:
    return "\n".join(l)


param: List[str] = ['ls', '-l']
output: Tuple[int, str] = xargs_get(param)
if not output[0]:
    print(print_list(output))
else:
    test_error("Error: " + output[1])
    message = 'Code location {0.filename}@{0.lineno}:'.format(
        inspect.getframeinfo(inspect.currentframe()))
    print(message)
