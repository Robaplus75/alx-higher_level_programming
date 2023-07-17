#!/usr/bin/python3
"""Square class module"""
from rectangle import Rectangle


class Square(Rectangle):
    """represents square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """square class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overrides the __str__ method"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        """gets the size of square"""
        return self.width

    @size.setter
    def size(self, val):
        """set the size of square"""
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """updates the square"""
        if len(args):
            for j, argg in enumerate(args):
                if j == 0:
                    self.id = argg
                elif j == 1:
                    self.size = argg
                elif j == 2:
                    self.x = argg
                elif j == 3:
                    self.y = argg
        else:
            for keyy, val in kwargs.items():
                if hasattr(self, keyy) is True:
                    setattr(self, keyy, val)

    def to_dictionary(self):
        """Dictionary represention of a square"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
