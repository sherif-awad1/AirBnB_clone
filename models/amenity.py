#!/usr/bin/python3
"""
This script defines a class to model amenities for a hospitality service.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity with a descriptive name.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
