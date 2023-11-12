#!/usr/bin/env python3
"""entry point of the command interpreter using cmd module"""
import cmd
from typing import Any


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand"""

    prompt = '(hbnb) '

    def emptyline(self):
        """"overrides the default emptyline"""
        pass

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Ctrl+D - EOF command to exit the program"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
