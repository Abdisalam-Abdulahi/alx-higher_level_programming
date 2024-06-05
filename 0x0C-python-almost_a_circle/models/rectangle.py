#!/usr/bin/python3

"""
this module defines a rectangle class
which is subclass of base
"""
from models.base import Base


class Rectangle(Base):
    """
    this module defines a rectangle class
    which is subclass of base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        retreives width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        sets width
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        retreives height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        sets height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        """
        retreives x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        sets x
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        retreives y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        sets y
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        calculates the arae of the reactangle
        """
        return self.width * self.height

    def display(self):
        """
        dispaly reactangle using "#"
        """
        for i in range(self.y):
            print("")

        for h in range(self.height):

            for i in range(self.x):
                print(" ", end="")

            for w in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
        method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y}\
 - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        lis = []
        for i in args:
            lis.append(i)

        if len(lis) == 1:
            self.id = lis[0]
        if len(lis) == 2:
            self.width = lis[1]
        if len(lis) == 3:
            self.height = lis[2]
        if len(lis) == 4:
            self.x = lis[3]
        if len(lis) == 5:
            self.y = lis[4]

        for k, v in kwargs.items():
            if 'id' == k:
                self.id = v
            if 'width' == k:
                self.width = v
            if 'height' == k:
                self.height = v
            if 'x' == k:
                self.x = v
            if 'y' == k:
                self.y = v

    def to_dictionary(self):
        """
        Returns dictionary representation of Reactangle class
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
