#!/usr/bin/env python3

args = __import__('sys').argv[1:]

if not args:
    print("none")
else:
    text = args[0]
    z_count = text.count('z')
    if z_count > 0:
        print('z' * z_count)
    else:
        print("none")