#!/usr/bin/env python3

first_number = int(input("Enter the first number: \n"))
second_number = int(input("Enter the second number: \n"))

multiplication = first_number * second_number
print(f"{first_number} x {second_number} = {multiplication}")

if multiplication < 0:
    print("The result is negative.")
elif multiplication > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")
