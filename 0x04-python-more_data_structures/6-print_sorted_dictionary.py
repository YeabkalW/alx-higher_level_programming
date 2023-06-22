#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_key = sorted(a_dictionary.keys())
    new_dict = {}
    for i in dict_key:
        new_dict[i] = a_dictionary[i]
        print("{}: {}".format(i, new_dict[i]))
