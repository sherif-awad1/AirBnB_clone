#!/usr/bin/python3
"""
This script defines a base class `BaseModel`
for managing objects in the application.

The `BaseModel` class provides common functionality for object creation,
persistence, and serialization. It is intended to be inherited by other
application-specific models.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Represents a base model with common attributes and methods.

    Attributes:
        id (str): A unique identifier for the object (UUID).
        created_at (datetime): The datetime when the object was created.
        updated_at (datetime): The datetime when the object was last updated.

    Methods:
        __init__(self, *args, **kwargs):
            Initializes the object with a unique ID, timestamps, and
            optional keyword arguments.
        save(self):
            Updates the updated_at timestamp and saves the object to storage.
        to_dict(self):
            Returns a dictionary representation of the object with
            formatted timestamps.
        __str__(self):
            Returns a string representation of
            the object including its class name,
            ID, and all attributes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the object with a unique ID, timestamps, and
        optional keyword arguments.

        Args:
            *args: Unused arguments (for future compatibility).
            **kwargs: Keyword arguments used to set object attributes.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def save(self):
        """
        Updates the updated_at timestamp and saves the object to storage.
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the object with
        formatted timestamps.
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict

    def __str__(self):
        """
        Returns a string representation of the object including its class name,
        ID, and all attributes.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


if __name__ == "__main__":
    """
    Example usage of the BaseModel class.
    """
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key,
              type(my_model_json[key]), my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
