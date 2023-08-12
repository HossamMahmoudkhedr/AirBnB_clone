#!/usr/bin/python3
"""Module defining the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for modeling a User entity"""
    def __init__(self, *args, **kwargs):
        """Initialiser of the State class"""
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
        super().__init__(**kwargs)
