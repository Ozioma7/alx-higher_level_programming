#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    largest_number = Max
    for number in my_list:
        if largest_number is Max or largest_number < number:
            largest_number = number
    print(largest_number)
