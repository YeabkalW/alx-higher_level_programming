#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k, v in a_dictionary.items():
        if value not in a_dictionary.values():
            return a_dictionary
        elif value == v:
            del a_dictionary[k]
        
        return a_dictionary
        