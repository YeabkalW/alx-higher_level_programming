#!/usr/bin/python3

def safe_print_integer(value):
    try:

        if isinstance(value, int):
            print("{:d}".format(value), end=("\n"))
            return True
        else:
            print("{:d}".format(value), end=("\n"))

    except (TypeError, ValueError):
        return False
