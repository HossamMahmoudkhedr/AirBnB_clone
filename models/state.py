#!/usr/bin/python3
''' Module defining the State class '''
from models.base_model import BaseModel


class State(BaseModel):
    ''' Class for modeling a State entity '''
    name = ''

    def __init__(self, *args, **kwargs):
        ''' Initialiser of the State class '''
        super().__init__(**kwargs)
