<<<<<<< HEAD
#!/usr/bin/env python3
"""Console module for HBNB project"""
import cmd
import shlex
from models.engine.file_storage import FileStorage
=======
#!/usr/bin/python3
"""it Defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
>>>>>>> 423cf54316a17e27e6aa53f51231d6cec948740b
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
<<<<<<< HEAD
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Console or command interpreter for the HBNB project"""

    prompt = "(hbnb) "
    cls_list = {'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City,
               'Amenity': Amenity, 'Place': Place, 'Review': Review}

    def do_quit(self, arg):
        """Command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Command to exit program using Ctrl+D shortcut"""
        print()
        return True

    def emptyline(self):
        """Nothing is executed with an empty line + ENTER"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of a class so long as it is in cls_list
        It then saves this instance to a JSON file and prints the id
        """
        if arg == '':
            print("** class name missing **")
        elif arg not in HBNBCommand.cls_list:
            print("** class doesn't exist **")
        else:
            obj_dict = eval(arg)()
            obj_dict.save()
            print(obj_dict.id)

    def do_show(self, args):
        """
            Command prints the string representation of an instance
            based on the class name and id
        """
        args_list = args.split()
        if len(args_list) == 0:
            print("** class name missing **")
            return
        if len(args_list) == 1:
            print("** instance id missing **")
            return

        storage = FileStorage()
        storage.reload()
        instance_dict = storage.all()

        cls_name = args_list[0]
        obj_id = args_list[1]

        try:
            cls = globals()[cls_name]
        except KeyError:
            print("** class doesn't exist **")
            return

        k = "{}.{}".format(cls_name, obj_id)

        if k in instance_dict:
            instance = instance_dict[k]
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args_list = args.split()
        if len(args_list) == 0:
            print("** class name missing **")
            return

        elif len(args_list) == 1:
            print("** instance id missing **")
            return

        cls_name = args_list[0]
        cls_id = args_list[1]
        storage = FileStorage()
        storage.reload()
        instance_dict = storage.all()
        try:
            eval(cls_name)
        except NameError:
            print("** class doesn't exist **")
            return

        k = "{}.{}".format(cls_name, cls_id)
        try:
            del instance_dict[k]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """
            Prints all string representation of all instances based
            or not on the class name
        """
        obj_list = []
        storage = FileStorage()
        storage.reload()
        obj = storage.all()
        args_list = args.split()

        if len(args_list) > 0:
            try:
                cls_to_filter = eval(args_list[0])
            except NameError:
                print("** class doesn't exist **")
        else:
            cls_to_filter = None

        for key, val in obj.items():
            if cls_to_filter is None or isinstance(val, cls_to_filter):
                obj_list.append(str(val))

        print(obj_list)

    def do_update(self, args):
        """
            Update an instance based on the class name and id
            sent as args
        """
        storage = FileStorage()
        storage.reload()
        args_list = shlex.split(args)
        if len(args_list) == 0:
            print("** class name missing **")
            return
        elif len(args_list) == 1:
            print("** instance id missing **")
            return
        elif len(args_list) == 2:
            print("** attribute name missing **")
            return
        elif len(args_list) == 3:
            print("** value missing **")
            return
        try:
            eval(args_list[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args_list[0] + "." + args_list[1]
        instance_dict = storage.all()
        try:
            obj_val = instance_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type = type(getattr(obj_val, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(obj_val, args_list[2], args_list[3])
        obj_val.save()


if __name__ == '__main__':
=======
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """it Defines HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing when receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
>>>>>>> 423cf54316a17e27e6aa53f51231d6cec948740b
    HBNBCommand().cmdloop()
