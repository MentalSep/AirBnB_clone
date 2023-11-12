#!/usr/bin/env python3
# Class BaseModel that defines all common attributes/methods for other classes
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """BaseModel class"""
    def __init__(self):
        """Constructor"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """retunrs a string representation of BaseModel instance"""
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
