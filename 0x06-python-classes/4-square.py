#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        """Initialize a new square
        Args:
        size (int): size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square"""
        return (self.__size * self.__size)
