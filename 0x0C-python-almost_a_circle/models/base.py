#!/usr/bin/python3

"""
A base class that has methods
and attributes
"""
import json


class Base:
    """
    Base class which has a lot of subclasses
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializeir, and class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
