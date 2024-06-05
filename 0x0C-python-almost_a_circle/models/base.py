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

    @classmethod
    def save_to_file(cls, list_objs):
        """
         writes the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            list_objs = []

        Jison = []
        for i in list_objs:
            Jison.append(i.to_dictionary())

        Jison = cls.to_json_string(Jison)
        clsNmae = cls.__name__ + ".json"
        f = open(clsNmae, "w")
        f.write(Jison)
        f.close()

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation
        """
        if json_string is None:
            return []
        return json.loads(json_string)
