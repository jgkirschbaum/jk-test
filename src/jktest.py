#!/usr/bin/env python
"""
This is test program
"""

from datetime import datetime
from time import sleep


while True:
    print(datetime.now().strftime("%Y-%m-%dT%T"))
    sleep(1)
