#!/usr/bin/python3
"""
This script defines a class `State` that inherits from `BaseModel`.

A state represents a geographic division within
a country, such as a state or province.
It can contain multiple associated cities.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
   Represents a state or province with its name.

   Attributes:
       name (str): The name of the state.

   Inherits from the BaseModel class which provides common functionality
   for managing objects in the application.
   """

    name = ""
