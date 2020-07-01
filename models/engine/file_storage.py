#!/usr/bin/python3
"""FileStorage class"""
from models.base_model import BaseModel
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """FileStorage class"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        new_dict = {}
        for key, val in self.__objects.items():
            new_dict[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exist"""

        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                for key, val in (json.load(f)).items():
                    val = eval(val['__class__'])(**(val))
                    self.__objects[key] = val
        except Exception:
            pass
