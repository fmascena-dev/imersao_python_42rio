#!/usr/bin/env python3

origin_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = [numero + 2 for numero in origin_array if numero > 5]
array_not_duplicate = set(new_array)

print(f"Original array: {origin_array}")
print(f"New array: {array_not_duplicate}")
