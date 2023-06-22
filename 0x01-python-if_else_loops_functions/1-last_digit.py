#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst_digi = abs(number) % 10
if number < 0:
    lst_digi = -lst_digi
print(f'Last digit of {number:d} is {lst_digi:d} and is ', end='')
if lst_digi > 5:
    print(f'greater than 5')
elif lst_digi == 0:
    print(f'0')
else:
    print(f'less than 6 and not 0')
