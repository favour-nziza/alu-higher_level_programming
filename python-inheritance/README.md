# Python - Inheritance

Superclasses, subclasses, `isinstance`/`issubclass`, overriding and `super()`.

| File | Description |
|------|-------------|
| 0-lookup.py | `lookup(obj)` returns `dir(obj)` |
| 1-my_list.py | `MyList(list)` with `print_sorted()` (tests in `tests/1-my_list.txt`) |
| 2-is_same_class.py | True if obj is exactly an instance of a class |
| 3-is_kind_of_class.py | True if obj is an instance of a class or a subclass |
| 4-inherits_from.py | True if obj's class inherits from a class (not the class itself) |
| 5-base_geometry.py | Empty `BaseGeometry` |
| 6-base_geometry.py | `BaseGeometry.area()` raises an Exception |
| 7-base_geometry.py | Adds `integer_validator()` (tests in `tests/7-base_geometry.txt`) |
| 8-rectangle.py | `Rectangle(BaseGeometry)` with validated private width/height |
| 9-rectangle.py | Adds `area()` and `__str__` -> `[Rectangle] w/h` |
| 10-square.py | `Square(Rectangle)` with `area()` |
| 11-square.py | Adds `__str__` -> `[Square] w/h` |
