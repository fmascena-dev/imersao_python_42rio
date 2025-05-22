#!/usr/bin/env python3

def downcase_it(str):
    return str

args = __import__('sys').argv[1:]

if not args:
    print("none")
else:
    for arg in args:
        print(f"{downcase_it(arg).lower()}")
