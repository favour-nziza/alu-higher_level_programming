#!/usr/bin/python3
"""Unittests for models/square.py."""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Unittests for instantiation of the Square class."""

    def test_is_base(self):
        """Square is a Base."""
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        """Square is a Rectangle."""
        self.assertIsInstance(Square(10), Rectangle)

    def test_no_args(self):
        """No argument raises a TypeError."""
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        """Two instances get consecutive ids."""
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        """All attributes are set."""
        s = Square(10, 2, 3, 7)
        self.assertEqual((s.size, s.x, s.y, s.id), (10, 2, 3, 7))

    def test_more_than_four_args(self):
        """Too many arguments raise a TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_property(self):
        """size getter and setter."""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual((8, 8, 8), (s.size, s.width, s.height))


class TestSquareValidation(unittest.TestCase):
    """Unittests for size/x/y validation of the Square class."""

    def test_size_types(self):
        """Non-int sizes raise a TypeError."""
        for value in (None, "invalid", 5.5, {"a": 1}, True, [1]):
            with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Square(value)

    def test_size_values(self):
        """Non-positive sizes raise a ValueError."""
        for value in (0, -1):
            with self.assertRaisesRegex(ValueError, "width must be > 0"):
                Square(value)

    def test_x_types(self):
        """Non-int x values raise a TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

    def test_x_values(self):
        """Negative x values raise a ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)

    def test_y_types(self):
        """Non-int y values raise a TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "invalid")

    def test_y_values(self):
        """Negative y values raise a ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)


class TestSquareMethods(unittest.TestCase):
    """Unittests for area, display and __str__ of the Square class."""

    @staticmethod
    def capture(sq, method):
        """Capture and return text printed to stdout."""
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_area(self):
        """Area of a square."""
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_str(self):
        """str() shows all attributes."""
        self.assertEqual("[Square] (53) 2/1 - 7", str(Square(7, 2, 1, 53)))

    def test_print(self):
        """print() uses __str__."""
        capture = TestSquareMethods.capture(Square(4, 0, 0, 3), "print")
        self.assertEqual("[Square] (3) 0/0 - 4\n", capture.getvalue())

    def test_display(self):
        """display with offsets."""
        capture = TestSquareMethods.capture(Square(2, 3, 2, 0), "display")
        self.assertEqual("\n\n   ##\n   ##\n", capture.getvalue())


class TestSquareUpdate(unittest.TestCase):
    """Unittests for the update method of the Square class."""

    def test_args(self):
        """Positional arguments update attributes in order."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_args_None_id(self):
        """A None id generates a new id."""
        s = Square(10, 10, 10, 10)
        s.update(None)
        self.assertEqual("[Square] ({}) 10/10 - 10".format(s.id), str(s))

    def test_kwargs(self):
        """Keyword arguments update attributes."""
        s = Square(10, 10, 10, 10)
        s.update(size=7, id=89, y=1)
        self.assertEqual("[Square] (89) 10/1 - 7", str(s))

    def test_args_and_kwargs(self):
        """Positional arguments take precedence over keywords."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_invalid(self):
        """Invalid values raise errors."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, 0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")


class TestSquareToDictionary(unittest.TestCase):
    """Unittests for the to_dictionary method of the Square class."""

    def test_output(self):
        """to_dictionary returns all attributes."""
        s = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_update_from_dict(self):
        """Using a dictionary to update another square."""
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)
        self.assertEqual(str(s1), str(s2))

    def test_arg(self):
        """to_dictionary takes no argument."""
        with self.assertRaises(TypeError):
            Square(10, 10, 10, 10).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
