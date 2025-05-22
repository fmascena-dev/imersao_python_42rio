#!/usr/bin/env python3

import re

args = __import__('sys').argv[1:]

if len(args) != 2:
    print('none')
else:
    keyword, text = args
    matches = re.findall(r'\b{}\b'.format(re.escape(keyword)), text)
    if matches:
        print(len(matches))
    else:
        print('none')
