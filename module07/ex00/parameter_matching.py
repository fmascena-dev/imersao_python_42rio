#!/usr/bin/env python3
args = __import__('sys').argv[1:]

if len(args) != 1:
    print('none')
else:
    expectative = args[0]
    user_input = input("What was the parameter? ")
    if user_input == expectative:
        print("Good job!")
    else:
        print('Nope, sorry...')
