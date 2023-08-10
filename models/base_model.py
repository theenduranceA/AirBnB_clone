#!/usr/bin/python3
<<<<<<< HEAD
"""
Module containing a BaseModel class that defines
all common attributes/methods for other classes.
"""

import uuid
import models
=======

import uuid
>>>>>>> 38a86afa6350ca197938edadbd1927cc9cb850f2
from datetime import datetime


class BaseModel:
<<<<<<< HEAD
    """A base class of public instance attributes."""

    def __init__(self, *args, **kwargs):
        """Instantiating the BaseModel class."""

        if kwargs:
            for key, value in kwargs.items():
                if key in "created_at" or key in "updated_at":
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key is not "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
=======
    def __init__(self, *args, **kwargs)
        if not kwargs:
            self.id = str(uuid.uuid4())  # Get a unique ID
            self.created_at = datetime.now()  # Set creation timestamp
            self.updated_at = self.created_at  # Set initial update timestamp
>>>>>>> 38a86afa6350ca197938edadbd1927cc9cb850f2

    def __str__(self):
        """Print methods in string."""

        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Public instance method that updates public
        instance attribute with the current datetime.
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Public instance method that returns a dictionary
        containing all keys/values of the instance.
        """

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
