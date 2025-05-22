#!/usr/bin/env python3

is_number = int(input("Digite um número e verifique se e positivo ou negativo: "))
print(is_number)

if is_number > 0:
    print("Esse número é positivo.")
elif is_number < 0:
    print("Esse número é negativo.")
else:
    print("Esse numero e neutro!")
