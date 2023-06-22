#!/usr/bin/python3
def uppercase(str):
    for i in str:
        ch = ord(i)
        if ch >= 97 and ch <= 122:
            ch -= 32
        print("{:s}".format(chr(ch)), end='')
    print()
