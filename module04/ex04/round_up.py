#!/usr/bin/env python3

number = input("Give me a number: ")
number_float = float(number)

number_integer = number_float.__ceil__()

print(number_integer)