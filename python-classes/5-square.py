#!/usr/bin/python3
"""This module defines a Square class that can print itself."""


class Square:
    """A class that represents a square and prints it with #."""

    def __init__(self, size=0):
        """Initialize the square with an optional size.

        Args:
            size: The length of one side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the length of one side of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the length of one side of the square after checking it."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character, or an empty line."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
