#!/usr/bin/python3

""" class Basemodel"""

from datetime import datetime
import uuid
import models
"""import models"""

de_ini = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:

    """init BaseModel"""

    def __init__(self, *args, **kwargs):
        """init"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, de_ini)
                if key != "class":
                    setattr(self, key, value)

    def __str__(self):
        """str"""
        return "[{}] ({}) {}".format(str(type(self).__name__), self.id,
                                     str(self.__dict__))

    def save(self):
        """save"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """dict"""
        d = dict(**self.__dict__)
        d['class'] = str(type(self).__name__)
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d
