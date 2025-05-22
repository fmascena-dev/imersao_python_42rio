#!/usr/bin/env python3

import sys

args = sys.argv[1:]

if len(args) != 2:
    print("none")
else:
    try:
        start = int(args[0])
        end = int(args[1])
        if start < end:
            array = list(range(start + 1, end))
        else:
            array = list(range(end + 1, start))
        print(array)
    except ValueError:
        print("none")
