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
        st = {}
        for i in FileStorage.__objects.keys():
            st[i] = FileStorage.__objects[i].to_json()

        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as fd:
            fd.write(json.dumps(st))

    def reload(self):
        try:
            with open(FileStorage.__file_path, mode="r") as file:
                new_dict = (json.load(file))
                for key, value in new_dict.items():
                    class_name = value.get('__class__')
                    obj = eval(class_name + '(**value)')
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
