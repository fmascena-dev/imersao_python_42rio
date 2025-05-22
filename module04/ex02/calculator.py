#!/usr/bin/env python3

first_number = input("Give me the first number: ")
second_number = input("Give me the second number: ")

first_integer = int(first_number)
second_integer = int(second_number)

print("Thank you!")

soma = first_integer + second_integer
sub = first_integer - second_integer
mult = first_integer * second_integer
div = first_integer / second_integer
div_integer = int(div)

print(f"{first_integer} + {second_integer} = {soma}")
print(f"{first_integer} - {second_integer} = {sub}")
print(f"{first_integer} * {second_integer} = {mult}")
print(f"{first_integer} / {second_integer} = {div_integer}")
