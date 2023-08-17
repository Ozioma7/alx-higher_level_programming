#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dictionary = {key: value * 2 for key, value i  a_dictionary.items()}
    print(new_dictionary)
