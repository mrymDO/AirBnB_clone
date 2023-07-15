#!/usr/bin/python3
"""Entry point of command interpreter"""

import cmd
from models.base_model import BaseModel
import models
import re
import shlex
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """Console class"""

    class_mapping = {
            'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City,
            'Amenity': Amenity, 'Place': Place, 'Review': Review
            }

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when it's called"""
        print()
        return True

    def emptyline(self):
        """Override emptyline method to do nothing"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            if arg in self.class_mapping:
                obj = self.class_mapping[arg]()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] in self.class_mapping:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            class_name = args[0]
            obj_id = args[1]
            if class_name in self.class_mapping:
                key = f"{class_name}.{obj_id}"
                all_objs = models.storage.all()
                if key in all_objs:
                    print(all_objs[key])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] in self.class_mapping:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            class_name = args[0]
            obj_id = args[1]
            all_objs = models.storage.all()
            key = f"{class_name}.{obj_id}"
            if key in all_objs:
                del all_objs[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """ Show All instance """
        model_name = arg
        if arg and model_name not in self.class_mapping:
            print("** class doesn't exist **")
            return

        list_objs = []
        all_objs = models.storage.all().items()
        if arg:
            for key, value in all_objs:
                if type(value) == self.class_mapping[model_name]:
                    list_objs.append(str(value))
            return print(list_objs)

        for key, value in all_objs:
            list_objs.append(str(value))
        print(list_objs)

    def do_update(self, args):
        """update"""
        tokens = shlex.split(args)
        args_len = len(tokens)

        if args_len == 0:
            print("** class name missing **")
            return
        class_name = tokens[0]
        if args_len == 1:
            if class_name not in self.class_mapping:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
            return
        id = tokens[1]
        instance = self.get_by_id(class_name, id)
        if args_len == 2:
            if instance == False:
                print("** no instance found **")
            else:
                print("** attribute name missing **")
            return

        if args_len == 3:
            print("** value missing **")
            return

        attribute_name = tokens[2]
        attribute_value = tokens[3]
        type_attrb_val = self.handle_type(attribute_value)

        if hasattr(instance, attribute_name):
            instance_attr_type = getattr(
                instance, attribute_name).__class__.__name__
            if instance_attr_type == type_attrb_val["type"].__name__:
                setattr(instance, attribute_name,
                        type_attrb_val["type"](attribute_value))
                instance.save()
        else:
            setattr(instance, attribute_name,
                    type_attrb_val["type"](attribute_value))
            instance.save()

    def is_float(self, num):
        try:
            int(num)
            return False
        except ValueError:
            return True

    def get_str(self, string):
        if string[0] == '"':
            return re.search('"[^"]*"', string).group()[1:-1]
        if string[0].isalpha():
            return string.split()[0]

    def handle_type(self, string):
        result = {}
        if string[0].isalpha():
            result["val"] = self.get_str(string)
            result["type"] = str
            return result
        value = string.split()[0]
        result["val"] = value
        if self.is_float(value) == True:
            result["type"] = float
        else:
            result["type"] = int
        return result

    def get_by_id(self, class_name, id):
        """ return obj if exist in storage otherwise return False"""
        key = f"{class_name}.{id}"
        if key in models.storage.all():
            return models.storage.all()[key]
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
