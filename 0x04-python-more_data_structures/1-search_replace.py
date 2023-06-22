#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for element in new_list:
        if element is search:
            new_list[new_list.index(element)] = replace

    return new_list
