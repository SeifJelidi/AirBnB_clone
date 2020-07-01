#!/usr/bin/python3
"""
____
"""

import models
import uuid
import datetime
import sys


class BaseModel:
    """
    base model class
    """

    def __init__(self, *args, **kwargs):
        """constructor"""
        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    datefmt = '%Y-%m-%dT%H:%M:%S.%f'
                    value = datetime.datetime.strptime(value, datefmt)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(
                   type(self).__name__, self.id, self.__dict__)

    def save(self):
        """the public instance attribute updated_at"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary contains all keys/values"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        new_cr_at = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        new_up_at = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        my_dict['created_at'] = new_cr_at
        my_dict['updated_at'] = new_up_at
        return my_dict
