#!/usr/bin/python3
"""
This script defines a class `City` that inherits from `BaseModel`.

A city is a location within a state and can have many associated places.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city within a state.

    Attributes:
        state_id (str): The ID of the state the city belongs to.
        name (str): The name of the city.

    Inherits from the BaseModel class which provides common functionality
    for managing objects in the application.
    """

    state_id = ""
    name = ""
