#!/usr/bin/python3

from datetime import datetime
import uuid
import models
    class BaseModel():
        """ class base model
    """
    def __init__(self, *args, **kwargs):
        """init funtion"""
        m = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None:
            self.created_at
            for key, value in kwargs.items():
                if key != '_class_':
                    setattr(self, key, value)
            self.__class__.__name__ = kwargs['_class_']
            self.created_at = datetime.datetime.strptime(kwargs['created_at'],
                                                         m)
            self.updated_at = datetime.datetime.strptime(kwargs['updated_at'],
                                                         m)
        else:
            models.storage.new(self)

    def __str__(self):
        """str"""
        return ("[{}] ({}) {}".format(type(self).__name__,
                self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

        def to_dict(self):
            """ ____"""
            my_dict['created_at'] = self.created_at.isoformat()
            my_dict['updated_at'] = self.updated_at.isoformat()
            my_dict['_class_'] = self.__class__.__name__
            return(my_dict)
