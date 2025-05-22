#!/usr/bin/env python3

args = __import__('sys').argv

if len(args) > 1:
    print(args[1])
else:
    print("none")
