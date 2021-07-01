#!/usr/bin/python3
"""Create Class FileStorage"""
import json
from models.base_model import BaseModel


class FileStorage():
    """Private class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        new_dict = {}

        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, mode="w", encoding="utf-8") as json_file:
            json.dump(new_dict, json_file)

    def reload(self):

        try:
            with open(self.__file_path, "r") as file:
                for j, value in (json.load(file)).items():
                    self.__objects[j] = eval(value["__class__"] + "(**value)")
        except FileNotFoundError:
            pass
