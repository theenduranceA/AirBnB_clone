#!/usr/bin/python3
"""
Module containing a FileStorage class that serializes instances
to a JSON file and deserializes JSON file to instances.
"""

import os
import json
import models
import datetime


class FileStorage:
    """A File storage class of private attributes."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Public instance method that returns the dictionar."""
        return FileStorage.__objects

    def new(self, obj):
        """Public instance method that sets in objects with the key."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Public instance method that serializes objects to the JSON file."""
        s_obj = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(s_obj, file)

    def reload(self):
        """Public instance method that deserializes
        the JSON file to objects ."""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                for key, value in json.load(file).items():
                    value = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = value
