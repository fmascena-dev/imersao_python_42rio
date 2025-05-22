#!/usr/bin/env python3

def greetings(name="noble stranger"):
    if isinstance (name, str):
        print(f"Hello, {name}")
    else:
        print("Error! name must be a string")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
