#!/usr/bin/python3
""" Rectangle module."""
from models.base import Base


class Rectangle(Base):
    """Represents rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """setter or getter for with of rectangel"""
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) != int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """ setter or getter for height of rectangle"""
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) != int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """setter or getter for x coordinate of rectangle"""
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) != int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """ gets the y"""
        return self.__y

    @y.setter
    def y(self, val):
        """ y setter function"""
        if type(val) != int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """Area of the rectangle"""
        return (self.height * self.width)

    def display(self):
        """Displays the rectange by #"""
        for i in range(self.y):
            print('\n', end="")
        for i in range(self.height):
            for i in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end='')
            print('')

    def __str__(self):
        """Overrides the __str__ methond"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """for updating the arguments in athe rectangle class"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """ Dictionary represetnation of rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
