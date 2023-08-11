#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
created on Monday Auggust 09 2023 0520HRS

Authors: Jonah Emmanuel and Endurance Aneke
"""

import cmd
import model
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity

class HBNBCommand(cmd.Cmd):
    """aclass that contains the entry point of the command interpreter.
    """
    prompt = '(hbnb) '

    def do_EOF(self, args):
        """EOF command to exit the program.
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
