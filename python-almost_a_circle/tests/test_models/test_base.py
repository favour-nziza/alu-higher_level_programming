#!/usr/bin/python3
"""Unittests for models/base.py."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """Unittests for instantiation of the Base class."""

    def test_no_arg(self):
        """Two instances without id get consecutive ids."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        """Three instances without id get consecutive ids."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        """None ids are auto-generated."""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        """A given id is used as is."""
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        """A given id does not change the counter."""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)
        self.assertEqual(b2.id, 12)

    def test_id_public(self):
        """The id attribute is public."""
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        """__nb_objects is private."""
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_objects)

    def test_str_id(self):
        """A string id is kept."""
        self.assertEqual("hello", Base("hello").id)

    def test_list_id(self):
        """A list id is kept."""
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_two_args(self):
        """Too many arguments raise a TypeError."""
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBaseToJsonString(unittest.TestCase):
    """Unittests for the to_json_string method."""

    def test_type(self):
        """to_json_string returns a string."""
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_rectangle_one_dict(self):
        """One rectangle dictionary is serialized."""
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_square_two_dicts(self):
        """Two square dictionaries are serialized."""
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_empty_list(self):
        """An empty list gives []."""
        self.assertEqual("[]", Base.to_json_string([]))

    def test_none(self):
        """None gives []."""
        self.assertEqual("[]", Base.to_json_string(None))

    def test_no_args(self):
        """No argument raises a TypeError."""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_more_than_one_arg(self):
        """Too many arguments raise a TypeError."""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBaseFromJsonString(unittest.TestCase):
    """Unittests for the from_json_string method."""

    def test_type(self):
        """from_json_string returns a list."""
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        self.assertEqual(list, type(Rectangle.from_json_string(
            json_list_input)))

    def test_one_rectangle(self):
        """One rectangle dictionary is deserialized."""
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        self.assertEqual(list_input,
                         Rectangle.from_json_string(json_list_input))

    def test_two_squares(self):
        """Two square dictionaries are deserialized."""
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        self.assertEqual(list_input, Square.from_json_string(json_list_input))

    def test_None(self):
        """None gives an empty list."""
        self.assertEqual([], Base.from_json_string(None))

    def test_empty_list(self):
        """'[]' gives an empty list."""
        self.assertEqual([], Base.from_json_string("[]"))

    def test_no_args(self):
        """No argument raises a TypeError."""
        with self.assertRaises(TypeError):
            Base.from_json_string()


class TestBaseSaveToFile(unittest.TestCase):
    """Unittests for the save_to_file method."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        for f in ("Rectangle.json", "Square.json", "Base.json"):
            try:
                os.remove(f)
            except IOError:
                pass

    def test_one_rectangle(self):
        """One rectangle is saved."""
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_two_squares(self):
        """Two squares are saved."""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_overwrite(self):
        """Saving again overwrites the file."""
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_None(self):
        """None writes []."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_empty_list(self):
        """An empty list writes []."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_no_args(self):
        """No argument raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()


class TestBaseCreate(unittest.TestCase):
    """Unittests for the create method."""

    def test_rectangle(self):
        """create builds a new, equal Rectangle."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_square(self):
        """create builds a new, equal Square."""
        s1 = Square(3, 5, 1, 7)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))
        self.assertIsNot(s1, s2)


class TestBaseLoadFromFile(unittest.TestCase):
    """Unittests for the load_from_file method."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        for f in ("Rectangle.json", "Square.json"):
            try:
                os.remove(f)
            except IOError:
                pass

    def test_rectangles(self):
        """Rectangles are loaded back."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(output[0]))
        self.assertEqual(str(r2), str(output[1]))
        self.assertTrue(all(type(o) is Rectangle for o in output))

    def test_squares(self):
        """Squares are loaded back."""
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertEqual(str(s2), str(output[1]))
        self.assertTrue(all(type(o) is Square for o in output))

    def test_no_file(self):
        """A missing file gives an empty list."""
        self.assertEqual([], Square.load_from_file())

    def test_more_than_one_arg(self):
        """Too many arguments raise a TypeError."""
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


if __name__ == "__main__":
    unittest.main()
