#!/bin/python3

import sys


S = input().strip()
try:
    num = int(S)
    print(num)
except ValueError:
    print("Bad String")    
