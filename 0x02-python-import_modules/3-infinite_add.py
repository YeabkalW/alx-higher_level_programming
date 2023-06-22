#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print("{}".format(0))
    else:
        args = list(map(int, sys.argv[1:]))
        sum_arg = sum(args)
        print("{}".format(sum_arg))
