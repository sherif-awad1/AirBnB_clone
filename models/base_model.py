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
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns official string representation"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """This returns a dictionary containing all keys/values of __dict__"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
