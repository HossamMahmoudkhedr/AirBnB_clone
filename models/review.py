#!/usr/bin/python3
"""Module defining the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class for modeling a Review entity"""
    def __init__(self, *args, **kwargs):
        """Initialiser of the Review class"""
        self.place_id = ''
        self.user_id = ''
        self.text = ''
        super().__init__(**kwargs)
