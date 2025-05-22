#!/usr/bin/env python3

number = input("Give me a number: ")
number_float = float(number)

if number_float.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")
