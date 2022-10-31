#!/usr/bin/python3


""" Module models/square"""
from .rectangle import Rectangle


class Square(Rectangle):
    """ class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ function __init__ """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ function size """
        return self.width

    @size.setter
    def size(self, value):
        """ function size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ function update """
        if len(args):
            key = ["id", "size", "x", "y"]
            idx = 0
            for value in args:
                if idx < 4:
                    setattr(self, key[idx], value)
                    idx += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ function to_dictionary """
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
