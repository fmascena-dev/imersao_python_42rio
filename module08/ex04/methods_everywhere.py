#!/usr/bin/env python3

import sys

args = sys.argv[1:]

def shrink(str):
    print(str[:8])

def enlarge(str):
    print(str.ljust(8, 'Z'))

if not args:
    print("none")
else:
    for arg in args:
        if len(arg) >= 8:
            shrink(arg)
        else:
            enlarge(arg)
    
