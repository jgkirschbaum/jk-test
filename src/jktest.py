#!/usr/bin/env python3
"""
This is test program
"""

from datetime import datetime
from time import sleep


while True:
    print(datetime.now().strftime("%Y-%m-%dT%T"))
    sleep(1)
