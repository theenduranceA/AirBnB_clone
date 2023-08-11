#!/usr/bin/python3
"""A module for the entry point of the command intepreter"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Nothing is executed with this command."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
