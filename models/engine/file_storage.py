#!/usr/bin/python3
''' serializes instances to a JSON file and deserializes JSON file to instances '''
import json


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' returns the dictionary __objects '''
        return self.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        ''' serializes __objects to the JSON file '''
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as myFile:
            json.dump(obj_dict, myFile)

    def reload(self):
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.review import Review
        from models.state import State
        from models.user import User
        from models.place import Place
        ''' deserializes the JSON file to __objects '''
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as myFile:
                obj_dict = json.load(myFile)

            for key, value in obj_dict.items():
                obj = eval(f"{value['__class__']}(**value)")
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
