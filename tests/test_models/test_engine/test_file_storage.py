#!/usr/bin/python3

import os
import json
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """
    This class defines unit tests for the instantiation
    of the FileStorage class.
    """

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)
        """
        Tests if creating a FileStorage instance without
        arguments works correctly.

        Expected behavior:
            - The created instance should be of type FileStorage.
        """

    def test_FileStorage_instantiation_with_arg(self):
        """
        Tests if creating a FileStorage instance
        with arguments raises a TypeError.

        Expected behavior:
            - Creating an instance with arguments should raise a TypeError.
        """
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        """
        Tests if the `_FileStorage__file_path` attribute
        is private and of type string.

        Expected behavior:
            - The attribute should be private
            (starting with double underscores).
            - The attribute's type should be string.
        """
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        """
        Tests if the `_FileStorage__objects
        `attribute is private and of type dictionary.

        Expected behavior:
            - The attribute should be private
            (starting with double underscores).
            - The attribute's type should be dictionary.
        """
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        """
        Tests if the `models.storage` variable
        is initialized as a FileStorage instance.

        Expected behavior:
            - The `models.storage` variable should be of type FileStorage.
        """
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """
    This class defines unit tests for the methods of the FileStorage class.
    """

    def setUp(self):
        """
        Sets up the test environment by renaming the storage file
        and resetting the storage object's internal dictionary.
        """
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """
        Tears down the test environment by removing the temporary storage file
        and renaming the original storage file back (if it existed).
        Also resets the storage object's internal dictionary.
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """
        Tests if the `all` method returns a dictionary of all stored objects.

        Expected behavior:
            - The `all` method should return a dictionary.
            - The dictionary keys should be in the formati
            "<class_name>.<object_id>"
            - The dictionary values should be the corresponding
            object instances.
        """
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        """
        Tests if the `all` method with arguments raises a TypeError.

        Expected behavior:
            - Calling `all` with arguments should raise a TypeError.
        """
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        """
        Tests if the `new` method correctly adds new objects to the storage.

        Expected behavior:
           - Adding objects with `new` should store them
           in the internal dictionary.
           - Objects should be retrievable with the correct keys in `all()`.
        """
        my_base_model = BaseModel()
        my_user = User()
        my_state = State()
        my_place = Place()
        my_city = City()
        my_amenity = Amenity()
        my_review = Review()
        models.storage.new(my_base_model)
        models.storage.new(my_user)
        models.storage.new(my_state)
        models.storage.new(my_place)
        models.storage.new(my_city)
        models.storage.new(my_amenity)
        models.storage.new(my_review)
        self.assertIn("BaseModel." + my_base_model.id,
                      models.storage.all().keys())
        self.assertIn(my_base_model, models.storage.all().values())
        self.assertIn("User." + my_user.id, models.storage.all().keys())
        self.assertIn(my_user, models.storage.all().values())
        self.assertIn("State." + my_state.id, models.storage.all().keys())
        self.assertIn(my_state, models.storage.all().values())
        self.assertIn("Place." + my_place.id, models.storage.all().keys())
        self.assertIn(my_place, models.storage.all().values())
        self.assertIn("City." + my_city.id, models.storage.all().keys())
        self.assertIn(my_city, models.storage.all().values())
        self.assertIn("Amenity." + my_amenity.id, models.storage.all().keys())
        self.assertIn(my_amenity, models.storage.all().values())
        self.assertIn("Review." + my_review.id, models.storage.all().keys())
        self.assertIn(my_review, models.storage.all().values())

    def test_new_with_args(self):
        """
        Tests if calling `new` with additional arguments raises a TypeError.
        """
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        """
        Tests if calling `new` with None raises an AttributeError.
        """
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        """
        Tests if the `save` method correctly saves objects to the storage file.

        Expected behavior:
            - Calling `save` should write serialized representations of objects
              to the storage file (`file.json`).
            - The serialized data should contain the object attributes.
        """
        my_base_model = BaseModel()
        my_user = User()
        my_state = State()
        my_place = Place()
        my_city = City()
        my_amenity = Amenity()
        my_review = Review()
        models.storage.new(my_base_model)
        models.storage.new(my_user)
        models.storage.new(my_state)
        models.storage.new(my_place)
        models.storage.new(my_city)
        models.storage.new(my_amenity)
        models.storage.new(my_review)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + my_base_model.id, save_text)
            self.assertIn("User." + my_user.id, save_text)
            self.assertIn("State." + my_state.id, save_text)
            self.assertIn("Place." + my_place.id, save_text)
            self.assertIn("City." + my_city.id, save_text)
            self.assertIn("Amenity." + my_amenity.id, save_text)
            self.assertIn("Review." + my_review.id, save_text)

    def test_save_with_arg(self):
        """
        Tests if calling `save` with an argument raises a TypeError.
        """
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        """
        Tests if the `reload` method correctly
        loads objects from the storage file.

        Expected behavior:
            - Calling `reload` should read serialized
            data from the storage file
              and create corresponding object instances.
            - The loaded objects should be stored in the internal dictionary.
        """
        my_base_model = BaseModel()
        my_user = User()
        my_state = State()
        my_place = Place()
        my_city = City()
        my_amenity = Amenity()
        my_review = Review()
        models.storage.new(my_base_model)
        models.storage.new(my_user)
        models.storage.new(my_state)
        models.storage.new(my_place)
        models.storage.new(my_city)
        models.storage.new(my_amenity)
        models.storage.new(my_review)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + my_base_model.id, objs)
        self.assertIn("User." + my_user.id, objs)
        self.assertIn("State." + my_state.id, objs)
        self.assertIn("Place." + my_place.id, objs)
        self.assertIn("City." + my_city.id, objs)
        self.assertIn("Amenity." + my_amenity.id, objs)
        self.assertIn("Review." + my_review.id, objs)

    def test_reload_with_arg(self):
        """
        Tests if calling `reload` with an argument raises a TypeError.
        """
        with self.assertRaises(TypeError):
            models.storage.reload(None)


"""
Run the tests if the script is executed directly
"""
if __name__ == "__main__":
    unittest.main()
