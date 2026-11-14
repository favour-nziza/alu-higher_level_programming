#!/usr/bin/python3
"""This module defines a Square class with a size and a position."""


class Square:
    """A class that represents a square with a size and a position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with an optional size and position.

        Args:
            size: The length of one side of the square.
            position: A tuple of 2 positive integers used when printing.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position used when printing the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position after checking it is a tuple of 2 positive ints."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with # at its position, or an empty line."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
