#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()

    # check if idx negative
    if idx < 0:
        return my_list
    # checks if idx is out of bounds
    elif idx >= len(my_list):
        return new_list
    else:
        new_list[idx] = element
        return new_list
