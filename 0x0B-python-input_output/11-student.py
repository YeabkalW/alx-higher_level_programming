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

    def to_json(self, attr=None):
        """converts the instance properties to a
        dictionary an returns it"""

        if isinstance(attr, list) and all(isinstance(elm, str)
                                          for elm in attr):
            obj_dict = {}
            for elm in attr:
                for k, v in self.__dict__.items():
                    if isinstance(v, (list, bool, int, dict, str)) and k \
                         == elm:
                        obj_dict[k] = v
            return obj_dict

        obj_dict = {}
        for k, v in self.__dict__.items():
            if isinstance(v, (list, bool, int, dict, str)):
                obj_dict[k] = v
        return obj_dict

    def reload_from_json(self, json):
        """replaces the classes instances
        with the value provied in the arg passes

        Args:
            json : a dict containg update attribute value"""

        for k, v in json.items():
            setattr(self, k, v)
