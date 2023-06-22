#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

args = list(sys.argv[1:])
operators = ['+', '-', '*', '/']

if __name__ == '__main__':
    if len(args) != 3 or len(args) > 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    elif args[1] not in operators:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
    else:
        arg1 = int(args[0])
        arg2 = int(args[2])
        if args[1] == '+':
            print("{} {} {} = {}".format(arg1, args[1], arg2, add(arg1, arg2)))
        elif args[1] == '-':
            print("{} {} {} = {}".format(arg1, args[1], arg2, sub(arg1, arg2)))
        elif args[1] == '*':
            print("{} {} {} = {}".format(arg1, args[1], arg2, mul(arg1, arg2)))
        else:
            print("{} {} {} = {}".format(arg1, args[1], arg2, div(arg1, arg2)))
