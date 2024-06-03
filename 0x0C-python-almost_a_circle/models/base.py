#!/usr/bin/python3

"""
A base class that has methods
and attributes
"""


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
