#!/usr/bin/env python3

import sys

args = sys.argv[1:] # [1:] => Ignora o nome do arquivo

if not args:
    print("none")
else:
    for arg in args:
        if not arg.endswith("ism"):
            print(arg + "ism")
            