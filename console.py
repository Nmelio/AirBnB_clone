#!/usr/bin/python3
""" Entry point of the command interpreter. """


import ast
import cmd
import models
import re

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel,
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'Review': Review,
        'State': State,
        'User': User,
    }

    def do_quit(self, arg):
        """ Exit the program """
        exit()

    def do_EOF(self, arg):
        """ Exit the program """
        print()
        return True

    def emptyline(self):
        """ Empty line + ENTER should not execute anything """
        pass

    def evaluate_with_quotes(self, value):
        if len(value) >= 2 and value[0] in '\'"' and value[-1] == value[0]:
            return value[1:-1]
        return value

    def parse_value_type(self, key, value, instance):
        """
        Convert a string to an integer or a float if possible.

        Args:
            line (str): The input string to be converted.

        Returns:
            int, float, or str: The converted value if the
            input matches the format of an integer or a float;
            otherwise, the original input string.
        """
        if re.match(r"^\d+$", value):
            return int(value)
        elif re.match(r"^\d+\.\d+$", value):
            return float(value)
        else:
            return value

    def help_create(self):
        """
        Display help information for the create command.
        """
        print("\nUsage: create <class_name>\n")
        print("This command creates a new instance of", end=" ")
        print("the specified class and assigns it a unique identifier.\n")

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it
            (to the JSON file) and prints the id """
        if len(arg) == 0:
            print('** class name missing **')
            return
        new_instance = None

        if arg:
            arg_list = arg.split()
            if len(arg_list) == 1:
                if arg in self.classes.keys():
                    new_instance = self.classes[arg]()
                    new_instance.save()
                    print(new_instance.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of
            an instance based on the class name and id """

        arg_list = arg.split()

        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg_list) > 1:
            instance_id = self.evaluate_with_quotes(arg_list[1])
            instance_key = arg_list[0] + '.' + instance_id
            if instance_key in models.storage.all():
                data = models.storage.all()
                print(data[instance_key])
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')

    def do_all(self, arg):
        """ Prints all string representation of
            all instances based or not on the class name """
        if len(arg) == 0:
            print([str(a) for a in models.storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print(
                [str(a) for b, a in models.storage.all().items() if arg in b]
            )

    def do_update(self, arg):
        """ Updates an instance based on the class
        name and id by adding or updating attribute
        (save the change into the JSON file) """
        arg_list = arg.split()
        data_instances = models.storage.all()

        if len(arg_list) == 0:
            print('** class name missing **')
            return
        elif arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg_list) == 1:
            print('** instance id missing **')
            return
        else:
            instance_id = self.evaluate_with_quotes(arg_list[1])
            instance_key = arg_list[0] + '.' + instance_id
            if instance_key in data_instances:
                if len(arg_list) > 2:
                    if len(arg_list) == 3:
                        print('** value missing **')
                    else:
                        arg_list[3] = self.parse_value_type(
                            self.evaluate_with_quotes(
                                arg_list[2]),
                            self.evaluate_with_quotes(
                                arg_list[3]),
                            data_instances[instance_key],
                        )

                        setattr(
                            data_instances[instance_key],
                            arg_list[2],
                            arg_list[3],
                        )
                        data_instances[instance_key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')

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
            instance_id = self.evaluate_with_quotes(arg_list[1])
            instance_key = arg_list[0] + '.' + instance_id
            if instance_key in models.storage.all():
                models.storage.all().pop(instance_key)
                models.storage.save()
            else:
                print('** no instance found **')
                return

    def default(self, arg):
        """ To retrieve all instances of a
            class by using:<class name>.all() """
        args = arg.split('.', 1)

        if args[0] in HBNBCommand.classes.keys():
            if args[1].strip('()') == 'all':
                self.do_all(args[0])
            elif args[1].strip('()') == 'count':
                self.do_count(args[0])
            elif args[1].split('(')[0] == 'show':
                self.do_show(args[0]+' '+args[1].split('(')[1].strip(')'))
            elif args[1].split('(')[0] == 'destroy':
                self.do_destroy(args[0]+' '+args[1].split('(')[1].strip(')'))
            elif args[1].split('(')[0] == 'update':
                arg0 = args[0]
                if ', ' not in args[1]:
                    arg1 = args[1].split('(')[1].strip(')')
                    self.do_update(arg0+' '+arg1)
                elif ', ' in args[1] and\
                     '{' in args[1] and ':' in args[1]:
                    arg1 = args[1].split('(')[1].strip(')').split(', ', 1)[0]
                    attr_dict = ast.literal_eval(args[1].split('(')[1]
                                                 .strip(')').split(', ', 1)[1])

                    for key, value in attr_dict.items():
                        self.do_update(arg0+' '+arg1+' '+key+' '+str(value))
                elif ', ' in args[1] and\
                     len(args[1].split('(')[1].strip(')').split(', ')) == 2:
                    arg1 = args[1].split('(')[1].strip(')').split(', ')[0]
                    arg2 = args[1].split('(')[1].strip(')').split(', ')[1]
                    self.do_update(arg0+' '+arg1+' '+arg2)
                elif ', ' in args[1] and\
                     len(args[1].split('(')[1].strip(')').split(', ')) >= 3:
                    # print(args[1])
                    arg1 = args[1].split('(')[1].strip(')').split(', ')[0]
                    # print(arg1)
                    arg2 = args[1].split('(')[1].strip(')').split(', ')[1]
                    # print(arg2)
                    arg3 = args[1].split('(')[1].strip(')').split(', ')[2]
                    # print(arg3)
                    self.do_update(arg0+' '+arg1+' '+arg2+' '+arg3)
            else:
                print('*** Unknown syntax: {}'.format(arg))
        else:
            print("** class doesn't exist **")

    @staticmethod
    def do_count(arg):
        """ Retrieve the number of instances of
            a class: <class name>.count() """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            counter = 0
            data = models.storage.all()
            for key, value in data.items():
                if arg == key.split('.')[0]:
                    counter += 1
            print(counter)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
