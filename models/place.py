#!/usr/bin/python3
"""Module defining the Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class for modeling a Place entity"""
    def __init__(self, *args, **kwargs):
        """Initialiser of the Place class"""
        self.name = ''
        self.city_id = ''
        self.user_id = ''
        self.description = ''
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        super().__init__(**kwargs)
