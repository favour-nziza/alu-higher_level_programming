# Python - Almost a circle

A `Base` class managing ids, a `Rectangle` and a `Square` with validated
attributes, `update`, dictionary and JSON (de)serialization, and unit tests.

## Files

| File | Description |
|------|-------------|
| models/base.py | `Base`: id management, `to_json_string`, `from_json_string`, `save_to_file`, `create`, `load_from_file` |
| models/rectangle.py | `Rectangle(Base)`: width/height/x/y, `area`, `display`, `__str__`, `update`, `to_dictionary` |
| models/square.py | `Square(Rectangle)`: `size`, `__str__`, `update`, `to_dictionary` |
| tests/test_models/ | Unit tests for every class |

## Run the tests

```
python3 -m unittest discover tests
```
