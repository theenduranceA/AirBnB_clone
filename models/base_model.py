#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs)
        if not kwargs:
            self.id = str(uuid.uuid4())  # Get a unique ID
            self.created_at = datetime.now()  # Set creation timestamp
            self.updated_at = self.created_at  # Set initial update timestamp

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()  # Update the update timestamp

    def to_dict(self):
        obj_dict = self.__dict__.copy()  # Copy instance attributes
        obj_dict['__class__'] = self.__class__.__name__  # Add class name
        obj_dict['created_at'] = self.created_at.isoformat()  # Convert to ISO format
        obj_dict['updated_at'] = self.updated_at.isoformat()  # Convert to ISO format
        return obj_dict

