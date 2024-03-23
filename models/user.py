#!/usr/bin/python3
"""
This script defines a class `User` that inherits from `BaseModel`.

A user represents a person who interacts with the application, such as
a property owner, guest, or administrator.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user with personal information and authentication credentials.

    Attributes:
        email (str): The user's email address (used for login).
        password (str): The user's password (hashed and stored securely).
        first_name (str): The user's first name.
        last_name (str): The user's last name.

    Inherits from the BaseModel class which provides common functionality
    for managing objects in the application.

    **Note:** It's important to store passwords
    securely using a hashing algorithm
    and never store them in plain text.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
