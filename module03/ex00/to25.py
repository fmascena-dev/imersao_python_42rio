#!/usr/bin/env python3

number = int(input("Enter a number less than 25: "))

def check_loop(number):
    if (number > 25):
        print("ERROR")
    while (number <= 25):
        print(f"Inside the loop, my variable is {number}")
    number += 1

check_loop(number)
