#!/usr/bin/python3

"""a function that prints a text with 2 new lines 
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """prints a text with 2
    new lines after each of these
    characters: (., ?, :)
    
    Args:
        text: a block of text to be 
            parsed
    Prints:
        a modified text with blank lines
    """
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        for c in text:
            if c == '.' or c == '?' or c == ':':
                print(c, end=(''))
                print('\n', end=(''))
                print('\n', end=(''))
            else:
                print(c, end=(''))               
