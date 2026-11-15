#!/usr/bin/python3
"""Unittests for models/rectangle.py."""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Unittests for instantiation of the Rectangle class."""

    def test_is_base(self):
        """Rectangle is a Base."""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        """No argument raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """One argument raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """Two instances get consecutive ids."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        """All attributes are set."""
        r = Rectangle(10, 2, 0, 0, 7)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (10, 2, 0, 0, 7))

    def test_more_than_five_args(self):
        """Too many arguments raise a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        """width is private."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        """height is private."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        """x is private."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        """y is private."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_setters(self):
        """Setters update the attributes."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        r.height = 3
        r.x = 2
        r.y = 9
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 3, 2, 9))


class TestRectangleValidation(unittest.TestCase):
    """Unittests for attribute validation of the Rectangle class."""

    def test_width_types(self):
        """Non-int widths raise a TypeError."""
        for value in (None, "invalid", 5.5, {"a": 1}, True, [1, 2], (1, 2)):
            with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle(value, 2)

    def test_width_values(self):
        """Non-positive widths raise a ValueError."""
        for value in (0, -1):
            with self.assertRaisesRegex(ValueError, "width must be > 0"):
                Rectangle(value, 2)

    def test_height_types(self):
        """Non-int heights raise a TypeError."""
        for value in (None, "invalid", 5.5, {"a": 1}, False, [1, 2]):
            with self.assertRaisesRegex(TypeError,
                                        "height must be an integer"):
                Rectangle(5, value)

    def test_height_values(self):
        """Non-positive heights raise a ValueError."""
        for value in (0, -1):
            with self.assertRaisesRegex(ValueError, "height must be > 0"):
                Rectangle(1, value)

    def test_x_types(self):
        """Non-int x values raise a TypeError."""
        for value in (None, "invalid", 5.5, {"a": 1}, True, [1]):
            with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, value)

    def test_x_values(self):
        """Negative x values raise a ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)

    def test_y_types(self):
        """Non-int y values raise a TypeError."""
        for value in (None, "invalid", 5.5, {"a": 1}, True, [1]):
            with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 3, value)

    def test_y_values(self):
        """Negative y values raise a ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(5, 3, 0, -1)

    def test_order_width_before_height(self):
        """width is validated before height."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_order_height_before_x(self):
        """height is validated before x."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def test_order_x_before_y(self):
        """x is validated before y."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")


class TestRectangleArea(unittest.TestCase):
    """Unittests for the area method."""

    def test_small(self):
        """Area of a small rectangle."""
        self.assertEqual(20, Rectangle(10, 2, 0, 0, 0).area())

    def test_large(self):
        """Area of a large rectangle."""
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

    def test_changed_attributes(self):
        """Area follows attribute changes."""
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

    def test_one_arg(self):
        """area takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(2, 10, 1, 1, 1).area(1)


class TestRectangleStdout(unittest.TestCase):
    """Unittests for the __str__ and display methods."""

    @staticmethod
    def capture(rect, method):
        """Capture and return text printed to stdout."""
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_print(self):
        """print() uses __str__."""
        r = Rectangle(4, 6, 0, 0, 12)
        capture = TestRectangleStdout.capture(r, "print")
        self.assertEqual("[Rectangle] (12) 0/0 - 4/6\n", capture.getvalue())

    def test_str_all(self):
        """str() shows all attributes."""
        r = Rectangle(5, 5, 1, 2, 7)
        self.assertEqual("[Rectangle] (7) 1/2 - 5/5", str(r))

    def test_display_width_height(self):
        """display without offsets."""
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangleStdout.capture(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_x(self):
        """display with an x offset."""
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangleStdout.capture(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_y(self):
        """display with a y offset."""
        r = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangleStdout.capture(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_all(self):
        """display with both offsets."""
        r = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangleStdout.capture(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        """display takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(5, 1, 2, 4, 7).display(1)


class TestRectangleUpdate(unittest.TestCase):
    """Unittests for the update method."""

    def test_args_zero(self):
        """No arguments change nothing."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_args(self):
        """Positional arguments update attributes in order."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_args_None_id(self):
        """A None id generates a new id."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        self.assertEqual("[Rectangle] ({}) 10/10 - 10/10".format(r.id),
                         str(r))

    def test_args_invalid(self):
        """Invalid positional values raise errors."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)

    def test_kwargs(self):
        """Keyword arguments update attributes."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=1, width=2, y=3, x=4, id=89)
        self.assertEqual("[Rectangle] (89) 4/3 - 2/1", str(r))

    def test_args_and_kwargs(self):
        """Positional arguments take precedence over keywords."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_kwargs_wrong_keys(self):
        """Unknown keys are ignored."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))


class TestRectangleToDictionary(unittest.TestCase):
    """Unittests for the to_dictionary method."""

    def test_output(self):
        """to_dictionary returns all attributes."""
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_no_object_changes(self):
        """Using a dictionary to update another rectangle."""
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)
        self.assertEqual(str(r1), str(r2))

    def test_arg(self):
        """to_dictionary takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 4, 1, 2).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
