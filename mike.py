""" Mike's python utilities
    because importing 1000 things every time sucks
    and these files are small anyway """

import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, List

import requests

from bs4 import BeautifulSoup

#  use lxml parser for speed: BeautifulSoup(markup,"lxml")
#  use html5lib parser for accuracy: BeautifulSoup(markup,"html5lib")
