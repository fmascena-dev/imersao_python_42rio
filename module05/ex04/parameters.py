#!/usr/bin/env python3

print(len(__builtins__.__import__('sys').argv) - 1)