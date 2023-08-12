#!/usr/bin/python3
"""Module defining the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class for modeling a City entity"""
    def __init__(self, *args, **kwargs):
        """Initialiser of the City class"""
        self.name = ''
        self.state_id = ''
        super().__init__(**kwargs)
