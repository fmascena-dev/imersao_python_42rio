#!/usr/bin/env python3

args = __import__('sys').argv[1:]

def shrink(s):
    print(s[:8])

def enlarge(s):
    print(s.ljust(8, 'Z'))

if not args:
    print("none")
else:
    for arg in args:
        if len(arg) >= 8:
            shrink(arg)
        else:
            enlarge(arg)
    
