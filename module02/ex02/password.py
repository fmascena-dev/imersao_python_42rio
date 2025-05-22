#!/usr/bin/env python3

password = "Python is awesome"

is_password = input("Enter your password: ")
print(is_password)

if is_password == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
