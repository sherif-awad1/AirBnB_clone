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
            """
        def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
