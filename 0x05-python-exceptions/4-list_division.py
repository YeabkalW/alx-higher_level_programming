#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    try:

        result = []

        for i in range(list_length):
            try:
                result.append(my_list_1[i] / my_list_2[i])

            except (IndexError, ZeroDivisionError, TypeError) as e:
                if isinstance(e, ZeroDivisionError):
                    result.append(0)
                    print("division by 0")
                elif isinstance(e, IndexError):
                    result.append(0)
                    print("out of range")
                elif isinstance(e, TypeError):
                    result.append(0)
                    print("wrong type")

    finally:
        return result
