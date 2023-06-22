#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    counter = len(sys.argv) - 1
    if counter == 0:
        print("{:d} arguments.".format(counter))
    elif counter == 1:
        print("{:d} argument:".format(counter))
    else:
        print("{:d} arguments:".format(counter))

    for i in range(counter):
        print("{:d}: {}".format(i+1, sys.argv[i+1]))
