#!/usr/bin/python3
from datetime import datetime
import uuid

de_ini = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:

    '''def _init_(self, *args, **kwargs):
    
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            #models.storage.new(self)

        else:
            for attr_name, attr in kwargs.items():
                if attr_name == "created_at" or attr_name == "updated_at":
                    attr = datetime.strptime(attr, "%Y-%m-%dT%H:%M:%S.%f")
                if attr_name != "class":
                    setattr(self, attr_name, attr)'''

    def _init_(self, *args, **kwargs):
        
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            #models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, de_ini)
                if key != "class":
                    setattr(self, key, value)


    def _str_(self):
        return "[{}] ({}) {}".format(str(type(self)._name_), self.id,
                                     str(self._dict_))

    '''def _repr_(self):
        return "[{}] ({}) {}".format(str(type(self)._name_), self.id,
                                     str(self._dict_))'''

    def save(self):
        self.updated_at = datetime.now()
        #models.storage.save()

    def to_dict(self):
        d = dict(**self._dict_)
        d['class'] = str(type(self)._name_)
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d
