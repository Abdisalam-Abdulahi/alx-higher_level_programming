#!/usr/bin/python3

"""
Square class that inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    a subclass that inherits from Reactangel
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        method should return [Square] (<id>) <x>/<y> - <size>
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y}\
 - {self.width}")

    @property
    def size(self):
        """
        retreive size
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        sets size
        """
        self.width = size
        self.height = size
