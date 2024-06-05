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

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        lis = []
        for i in args:
            lis.append(i)

        if len(lis) >= 1:
            self.id = lis[0]
        if len(lis) == 2:
            self.size = lis[1]
        if len(lis) == 3:
            self.x = lis[2]
        if len(lis) == 4:
            self.y = lis[3]

        for k, v in kwargs.items():
            if 'id' == k:
                self.id = v
            if 'size' == k:
                self.size = v
            if 'x' == k:
                self.x = v
            if 'y' == k:
                self.y = v
