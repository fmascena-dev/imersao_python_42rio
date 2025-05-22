#!/usr/bin/env python3

args = __import__('sys').argv
print(args[1].lower() if len(args) == 2 else "none")
