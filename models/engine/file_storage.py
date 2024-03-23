#!/usr/bin/python3
"""
This script defines a class for storing and retrieving objects in JSON format.
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class FileStorage:
    """
    A class that performs serialization and deserialization of objects.

    Attributes:
        __file_path: The path to the file where objects
        are stored (default: "file.json").
        __objects: A dictionary that stores all objects
        (key: object ID, value: object).
    """
    __file_path = "file.json"

    __objects = {}

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
            obj: The object to be added.
        """
        obj_cls_name = obj.__class__.__name__

        key = "{}.{}".format(obj_cls_name, obj.id)

        FileStorage.__objects[key] = obj

    def all(self):
        """
        Returns a dictionary containing all stored objects.

        Returns:
            A dictionary containing all stored objects
            (key: object ID, value: object).
        """
        return FileStorage.__objects

    def save(self):
        """
        Saves all objects in the storage dictionary to a JSON file.
        """
        all_objs = FileStorage.__objects

        obj_dict = {}

        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Loads objects from a JSON file into the storage dictionary.

        If the file doesn't exist, nothing happens.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)

                        instance = cls(**value)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
