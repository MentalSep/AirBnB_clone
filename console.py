#!/usr/bin/python3
"""entry point of the command interpreter using cmd module"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand"""
    prompt = '(hbnb) '
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place",
               "Review"]

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

    def do_create(self, arg):
        """create command to create a new instance of BaseModel"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg + "()")
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """show command to print the string representation of an instance"""
        if len(arg) == 0:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """destroy command to delete an instance based on the class name"""
        if len(arg) == 0:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        """all command to print all string representation of all instances"""
        if len(arg) == 0:
            print([str(value) for value in storage.all().values()])
        else:
            args = arg.split()
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                print([str(value) for key, value in storage.all().items()
                       if args[0] in key])

    def do_update(self, arg):
        """update command to update an instance based on the class name"""
        if len(arg) == 0:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all().keys():
                    print("** no instance found **")
                elif len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(storage.all()[key], args[2], args[3])
                    storage.save()

    def default(self, arg):
        """ overwrites the defalut 'default' method"""
        args = arg.split(".")
        if len(args) >= 2:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                print(len([str(value) for key, value in storage.all().items()
                           if args[0] in key]))
            elif args[1][:5] == "show(" and args[1][-1] == ")":
                self.do_show(args[0] + " " + args[1][6:-2])
            elif args[1][:8] == "destroy(" and args[1][-1] == ")":
                self.do_destroy(args[0] + " " + args[1][9:-2])
            elif args[1][:7] == "update(" and args[1][-1] == ")":
                args2 = args[1][7:-1].split(", ")
                if len(args2) == 4:
                    self.do_update(args[0] + " " + args2[0][1:-1] + " " +
                                   args2[1][1:-1] + " " + args2[2][1:-1] +
                                   " " + args2[3][1:-1])
                elif len(args2) == 3:
                    self.do_update(args[0] + " " + args2[0][1:-1] + " " +
                                   args2[1][1:-1] + " " + args2[2][1:-1])
                elif len(args2) == 2:
                    self.do_update(args[0] + " " + args2[0][1:-1] + " " +
                                   args2[1][1:-1])
                elif len(args2) == 1:
                    self.do_update(args[0] + " " + args2[0][1:-1])
            else:
                cmd.Cmd.default(self, arg)
        else:
            cmd.Cmd.default(self, arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
