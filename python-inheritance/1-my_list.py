#!/usr/bin/python3
"""Defines MyList, a list subclass."""


class MyList(list):
    """A list that can print itself sorted."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
