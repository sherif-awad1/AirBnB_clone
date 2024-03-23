#!/usr/bin/python3
"""
This script defines a class `Place` that inherits from `BaseModel`.

A place represents a location that can be booked for accommodation,
such as an apartment, house, or other lodging.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a place for accommodation with various attributes.

    Attributes:
        city_id (str): The ID of the city where the place is located.
        user_id (str): The ID of the user who owns or manages the place.
        name (str): The name of the place.
        description (str): A description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests allowed in the place.
        price_by_night (int): The price per night for staying at the place.
        latitude (float): The geographical latitude of the place.
        longitude (float): The geographical longitude of the place.
        amenity_ids (list): A list of IDs for
        amenities associated with the place.

    Inherits from the BaseModel class which provides common functionality
    for managing objects in the application.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
