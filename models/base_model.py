#!/usr/bin/python3
''' Module defining the BaseModel class for other classes '''
import sys
import os
from datetime import datetime
from uuid import uuid4
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import storage

class BaseModel:
    ''' The base model class with functionality for other entity classes '''

    def __init__(self, *args, **kwargs):
        ''' Initialise the base model object id '''
        if len(kwargs) == 0:
            self.created_at = datetime.now()
            self.id = str(uuid4())
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in zip(kwargs.keys(), kwargs.values()):
                if key != '__class__':
                    setattr(self, key, value)
            if hasattr(self, 'created_at'):
                self.created_at = datetime.fromisoformat(self.created_at)
            if hasattr(self, 'updated_at'):
                self.updated_at = datetime.fromisoformat(self.updated_at)

    def save(self):
        ''' Saves the timestamp of updating the instance '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        ''' Converts the instance into a dict representation '''
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict['__class__'] = type(self).__name__
        return obj_dict

    def __str__(self):
        ''' String representation of the instance '''
        return '[{}] ({}) {}'.format(
            type(self).__name__, self.id, self.__dict__
        )

if __name__ == '__main__':
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    # print("--------\n{}\n--------".format(type(my_model).__name__))
    print(my_model)
    print()
    my_model.save()
    print()
    print(my_model)
    print()
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print()
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(
            key, type(my_model_json[key]), my_model_json[key])
        )
