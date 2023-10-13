#!/usr/bin/python3
"""Defines Base Model Class"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    Base Class from which all other classes inherit from
    """
    def __init__(self, *args, **kwargs):
        """Lets Initialize the public instance attribute"""
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    setattr(self, k, v)
                if k in ('created_at', 'updated_at'):
                    setattr(self, k, datetime.fromisoformat(v))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Returns string representation of the Base Model class when called"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Method returns dictionary representation of an instance"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
