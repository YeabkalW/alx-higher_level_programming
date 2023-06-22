#!/usr/bin/python3
def print_last_digit(number):
    digit = abs(number) % 10
    if number < 0:
        digit = -digit
    print(digit)
    return digit
