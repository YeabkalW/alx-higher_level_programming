#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        if my_list is None:
            my_list = []

        counter = 0

        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end=(""))
                counter += 1
            else:
                continue
        print()
        return counter

    except IndexError as e:
        raise e
