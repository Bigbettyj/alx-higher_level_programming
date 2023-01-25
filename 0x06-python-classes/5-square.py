#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new square
        Args:
        size (int): the size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """"Retrieves the size of the Square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character # """
        for i in range(0, self.__size):
            [print("#", end="") for n in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
