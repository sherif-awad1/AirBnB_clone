#!/usr/bin/python3

import os
import unittest
from models.base_model import BaseModel
"""
This script defines a test class to verify
thefunctionality of the BaseModel class,
for other model classes in the
'models' module. The tests cover
instantiation, saving behavior, dictionary
conversion, and string representation.
"""


class TestBasemodel(unittest.TestCase):
    """
    Set up and tear down methods for managing
    a file named 'file.json', possibly
    used for persistence. These methods handle
    renaming and deletion to isolate tests.
    """
    def setUp(self):
        """
        Rename file.json to tmp.json if it exists.
        """
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """
        Remove file.json and restore tmp.json if it exists.
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_init(self):
        """
        Test for successful model instantiation, ensuring the presence of
        required attributes upon creation.
        """
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        Test that saving a model updates its
        'updated_at' timestamp, signifying
        a change in its state.
        """
        my_model = BaseModel()

        initial_updated_at = my_model.updated_at

        current_updated_at = my_model.save()

        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        """
        Test that the 'to_dict' method correctly converts a BaseModel instance
        into a dictionary representation, containing expected keys and values.
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'],
                         my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"][:19],
                         my_model.updated_at.isoformat()[:19])

    def test_str(self):
        """
        Test the string representation of a BaseModel instance, ensuring it
        contains expected information for readability and debugging.
        """
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))

        self.assertIn(my_model.id, str(my_model))

        self.assertIn(str(my_model.__dict__), str(my_model))


"""
Run the tests if the script is executed directly
"""
if __name__ == "__main__":
    unittest.main()
