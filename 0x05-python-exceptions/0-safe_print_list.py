#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if my_list is None:
        my_list = []

    counter = 0
    try:
        for i in range(x):
            print(my_list[i], end=(""))
            counter += 1
        print()
        return counter
    except IndexError:
        print()
        return counter
