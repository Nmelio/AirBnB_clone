#!/usr/bin/python3

import json

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        dict_objects = {}
        for key, value in self.__objects.items():
            dict_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dict_objects, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
            for key, value in data.items():
                class_name, id = key.split('.')

                # Retrieves class object from global
                # scope to recreate instance
                class_obj = globals()[class_name]
                self.__objects[key] = class_obj(**value)

        except FileNotFoundError:
            pass
