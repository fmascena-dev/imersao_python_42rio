#!/usr/bin/env python3

number_base = 0

while number_base <= 10:
    print(f"Table of {number_base}:", end=" ")
    multiply = 0
    while multiply <= 10:
        print(number_base * multiply, end=" ")
        multiply += 1
    print()
    number_base += 1
