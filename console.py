#!/usr/bin/python3
"""Implementation of the HBnB Command Console."""

import ast
import cmd
import shlex
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
    """HBNBCommand Class.

    The HBNBCommand class is the command-line interface for the
    Airbnb-like application. It provides an interactive shell for
    managing and interacting with various objects and data models
    within the application. Users can create, view, update, and delete
    instances of different classes such as
    BaseModel, Amenity, City, Place, Review, State, and User.

    Args:
        cmd (cmd.Cmd): A subclass of the `cmd` module's `Cmd` class.

    Attributes:
        prompt (str): The prompt displayed to the user in the console.
        classes (dict): A dictionary mapping class names to their
        Python class definitions.

    Methods:
        do_quit(self, arg)
        do_EOF(self, arg)
        emptyline(self)
        evaluate_with_quotes(self, value)
        parse_value_type(self, key, value, instance)
        help_create(self)
        do_create(self, arg)
        do_show(self, arg)
        do_all(self, arg)
        do_update(self, arg)
        do_destroy(self, arg)
        default(self, arg)
        do_count(self, arg)
    """

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

    def help_quit(self):
        """
        Display help information for the quit command.

        Args:
            arg (str): Ignored.
        """
        print("\nUsage: quit\n")
        print("This command allows you to exit the command", end=" ")
        print("interpreter gracefully.\n")

    def do_quit(self, arg):
        """
        Exit the program.

        Args:
            arg (str): Command arguments (ignored).
        """
        return True

    def help_EOF(self):
        """
        Display help information for the EOF command.

        Args:
            arg (str): Ignored.

        """
        print("\nUsage: EOF\n")
        print("This command allows you to exit the command", end=" ")
        print("interpreter gracefully by pressing Ctrl+D (EOF).\n")

    def do_EOF(self, arg):
        """
        Exit the program gracefully using Ctrl+D (EOF).

        Args:
            arg (str): Ignored.

        Returns:
            bool: Returns True
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on an empty line.

        pass
        """
        pass

    def evaluate_with_quotes(self, value):
        """
        Evaluate a value with possible enclosing quotes.

        Args:
            value (str): The input value to be evaluated.

        Returns:
            str: Evaluated value or initial input.
        """
        if len(value) >= 2 and value[0] in '\'"' and value[-1] == value[0]:
            return value[1:-1]
        return value

    def parse_value_type(self, key, value, instance):
        """
        Parse and convert a string value to an appropriate data type.

        Args:
            key (str): The attribute key to which the value corresponds.
            value (str): The input value to be parsed and converted.
            instance: The instance to which the attribute belongs.

        Returns:
            int, float, or str: The parsed value
        """
        if (hasattr(instance, key)):
            attr_type = type(getattr(instance, key))
            try:
                return attr_type(value)
            except ValueError:
                pass
        if re.match(r"^\d+$", value):
            return int(value)
        elif re.match(r"^\d+\.\d+$", value):
            return float(value)
        else:
            return value

    def chunk_array(self, arr, chunk_size=2):
        """
        Chunk an array into sublists of a specified size.

        Args:
            arr (list): The input list to be chunked.
            chunk_size (int): The size of each chunk.

        Returns:
            list: A list of sublists, each containing
                    `chunk_size` elements from the input list.
        """
        chunks = [arr[i:i+chunk_size] for i in range(0, len(arr), chunk_size)]
        return chunks

    def help_create(self):
        """
        Display help information for the create command.

        pass
        """
        print("\nUsage: create <class_name>\n")
        print("This command creates a new instance of", end=" ")
        print("the specified class and assigns it a unique identifier.\n")

    def do_create(self, arg):
        """
        Create a new instance of a specified class.

        Args:
            arg (str): The class name for which an instance is to be created.
        """
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

    def help_show(self):
        """
        Display help information for the show command.

        pass
        """
        print("\nUsage: show <class_name> <id>\n")
        print("This command displays an instance's string representation.\n")

    def do_show(self, arg):
        """
        Display the string representation of an instance.

        Args:
            arg (str): The command argument containing the class name
                       and instance ID.
        """
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

    def help_all(self):
        """
        Display help for the all command.

        pass
        """
        print("\nUsage: help all\n")
        print("All command displays string representations of all instances.")
        print("Optionally, provide a class name to filter instances", end=' ')
        print("of a specific class.\n")

    def do_all(self, arg):
        """
        Display string representations of instances.

        Args:
            arg (str): The optional command argument containing the class name.
        """
        if len(arg) == 0:
            print([str(a) for a in models.storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print(
                [str(a) for b, a in models.storage.all().items() if arg in b]
            )

    def help_update(self):
        """
        Display help for the update command.

        pass
        """
        print(
            """\nUsage: update <class_name> <instance_id>
            <attribute_name> <attribute_value>\n"""
        )
        print(
            """This command updates an instance's attribute based on the
            class name, instance ID, attribute name, and new value."""
        )
        print("The updated instance is then saved to the JSON file.\n")

    def do_update(self, arg):
        """
        Update an instance's attributes.

        Args:
            arg (str): The command argument containing class name,
                        instance ID, attribute name, and attribute value.
        """
        arg_list = shlex.split(arg)
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

    def help_destroy(self):
        """
        Display help for the destroy command.

        pass
        """
        print("\nUsage: help destroy\n")
        print("Destroy command deletes an instance by class", end=' ')
        print("name and instance ID.\n")

    def do_destroy(self, arg):
        """
        Delete an instance based on class name and ID.

        Args:
            arg (str): The command argument containing
                        the class name and instance ID.
        """
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

    def help_count(self):
        """
        Display help for the count command.

        Usage:
            help count
        """
        print("\nUsage: count <class_name>\n")
        print("Retrieve the number of instances of a class.")
        print(
            """Counts and displays the total number of instances
                belonging to the specified class.\n"""
        )

    @staticmethod
    def do_count(arg):
        """
        Retrieve the number of instances of a class.

        Args:
            arg (str): The command argument containing the class name.
        """
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

    def default(self, arg):
        """
        Handle default behavior for unrecognized commands.

        Args:
            arg (str): The command argument containing the unrecognized input.

        Usage:
            The method can handle various syntaxes, such as:
            - <class_name>.all()
            - <class_name>.count()
            - <class_name>.show(<instance_id>)
            - <class_name>.destroy(<instance_id>)
            - <class_name>.update(<instance_id>, <attr_name>, <attr_value>)
            - <class_name>.update(<instance_id>,
                            {<attr_name>: <attr_value>, ...})
        """
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
                class_model = args[0]

                if ', ' not in args[1]:
                    arg1 = args[1].split('(')[1].strip(')')
                    self.do_update(class_model+' '+arg1)

                elif ', ' in args[1] and\
                     '{' in args[1] and ':' in args[1]:
                    arg1 = args[1].split('(')[1].strip(')').split(', ', 1)[0]
                    attr_dict = ast.literal_eval(args[1].split('(')[1]
                                                 .strip(')').split(', ', 1)[1])

                    for key, value in attr_dict.items():
                        self.do_update(f'{class_model} {arg1} {key} "{value}"')

                elif ', ' in args[1] and\
                     len(args[1].split('(')[1].strip(')').split(', ')) == 2:
                    arg1 = args[1].split('(')[1].strip(')').split(', ')[0]
                    arg2 = args[1].split('(')[1].strip(')').split(', ')[1]
                    self.do_update(class_model+' '+arg1+' '+arg2)
                elif ', ' in args[1] and\
                     len(args[1].split('(')[1].strip(')').split(', ')) >= 3:

                    data_arr = args[1].split('(')[1].strip(')').split(', ')
                    data_arr = ' '.join(data_arr)
                    data_arr = shlex.split(data_arr)

                    instance_id = data_arr[0]

                    data_arr.pop(0)
                    data_arr = self.chunk_array(data_arr)

                    for sublist in data_arr:
                        if len(sublist) >= 2:
                            command = f'{class_model} {instance_id}'
                            command = f'{command} {sublist[0]} "{sublist[1]}"'
                            self.do_update(command)
            else:
                print('*** Unknown syntax: {}'.format(arg))
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
