#!/usr/bin/python3

def no_c(my_string):
    new_my_string = ''
    for c in my_string:
        if c != 'c' and c != 'C':
            new_my_string += c
    return (new_my_string)
