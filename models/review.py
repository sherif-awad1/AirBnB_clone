#!/usr/bin/python3
"""
This script defines a class `Review` that inherits from `BaseModel`.

A review represents a user's feedback about a particular place.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review of a place written by a user.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The text content of the review.

    Inherits from the BaseModel class which provides common functionality
    for managing objects in the application.
    """

    place_id = ""
    user_id = ""
    text = ""
