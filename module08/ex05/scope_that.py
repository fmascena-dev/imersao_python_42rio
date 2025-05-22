#!/usr/bin/env python3

def add_one(x):
    x += 1
    return x

number = 25
print("Before:", number)

number = add_one(number)

print("After:", number)
