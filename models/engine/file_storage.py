#!/usr/bin/python3
""" class FileStorage serializes instances to a JSON
    file and deserializes JSON file to instances """
import json
import uuid
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ serializes instances to a JSON file and 
        deserializes JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """ Serializes __objects to the JSON file 
            (path: __file_path) """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file_name:
            create_dic = {key: obj.to_dict() for key, obj in
                        FileStorage.__objects.items()}
            json.dump(create_dic, file_name)

    def reload(self):
        """ Deserializes the JSON file to __objects 
            (only if the JSON file (__file_path) exists """
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file_name:
                json_file = json.load(file_name)
                for key, value in json_file.items():
                    FileStorage.__objects[key] = eval(value['__class__'])(**value)
