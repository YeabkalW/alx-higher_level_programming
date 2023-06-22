#!/usr/bin/python3
"""Defines a student class"""


class Student:
    """Student class that is a template
    for a student and holds relevant info
    a that defines a student, as well a function
    that help to convert class instances attribute
    to a serializable dictionary."""

    def __init__(self, first_name, last_name, age):
        """creates class instance upon creation and
            assigns its properties to a public attribute
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """converts the instance properties to a
        dictionary an returns it"""
        obj_dict = {}
        for k, v in self.__dict__.items():
            if isinstance(v, (list, bool, int, dict, str)):
                obj_dict[k] = v
        return obj_dict
