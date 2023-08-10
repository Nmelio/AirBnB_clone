#!/usr/bin/python3
""" Entry point of the command interpreter """
import cmd
import sys
import json
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Entry point of the command interpreter """
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State}

    def do_quit(self, arg):
        """ Exit the program """
        exit()

    def do_EOF(self, arg):
        """ Exit the program """
        print('')
        return True

    def emptyline(self):
        """ Empty line + ENTER should not execute anything """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it
            (to the JSON file) and prints the id """
        if len(arg) == 0:
            print('** class name missing **')
            return
        new_class = None
        if arg:
            listss = arg.split()
            if len(listss) == 1:
                if arg in self.classes.keys():
                    new_class = self.classes[arg]()
                    new_class.save()
                    print(new_class.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of
            an instance based on the class name and id """
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg.split()) > 1:
            x = arg.split()[0] + '.' + arg.split()[1]
            if x in storage.all():
                y = storage.all()
                print(y[x])
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name
            and id (save the change into the JSON file) """
        if len(arg) == 0:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            obj = eval(arg_list[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print('** instance id missing **')
            return
        if len(arg_list) > 1:
            key = arg_list[0] + '.' + arg_list[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')
                return

    def do_all(self, arg):
        """ Prints all string representation of
            all instances based or not on the class name """
        if len(arg) == 0:
            print([str(a) for a in storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(a) for b, a in storage.all().items() if arg in b])

    def do_update(self, arg):
        """ Updates an instance based on the class
        name and id by adding or updating attribute
        (save the change into the JSON file) """
        arg = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print('** instance id missing **')
            return
        else:
            key = arg[0] + '.' + arg[1]
            if key in storage.all():
                if len(arg) > 2:
                    if len(arg) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                            storage.all()[key],
                            arg[2],
                            arg[3][1:-1])
                        storage.all()[key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
