#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        a = len(sentence)
        b = None
    else:
        a = len(sentence)
        b = sentence[0]

    c = (a, b)
    return c
