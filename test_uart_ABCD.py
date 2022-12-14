#!/usr/bin/env python3

from serial import Serial
from pyubx2 import UBXReader
import time

stream = Serial('/dev/ttyS0', 9600, timeout=3)
ubr = UBXReader(stream)
while True:
    (raw_data, parsed_data) = ubr.read()
    print(parsed_data)
    time.sleep(2)
