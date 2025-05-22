#!/usr/bin/env python3

def find_the_redheads(hair_color_dict):

    return list(filter(lambda name: hair_color_dict[name] == 'red', hair_color_dict.keys()))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginia": "brunete",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))