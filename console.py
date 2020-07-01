#!/usr/bin/python3
"""Console 0.0.1"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import datetime
classList = ["BaseModel", "User", "State", "City",
             "Amenity", "Place", "Review"]


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = '(hbnb) '

    def do_EOF(self, my_input):
        """Handles EOF to exit the program"""
        print('')
        return True

    def do_quit(self, my_input):
        """Handles quit to exit the program"""
        return True

    def emptyline(self):
        """Handles empty line + ENTER"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""

        if not args:
            print("** class name missing **")
            return

        if args == classList[0]:
            my_base_model = BaseModel()
            print(my_base_model.id)
            my_base_model.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation
        of an instance based on the class name and id"""

        if not args:
            print("** class name missing **")
            return

        largs = args.split(" ")

        if largs[0] in classList:
            if len(largs) == 1:
                print("** instance id missing **")
                return

            objs = storage.all()
            idObj = largs[0] + '.' + largs[1]
            if idObj not in objs.keys():
                print("** no instance found **")
                return
            print(objs[idObj])
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and
        id and saving the change in json file)"""

        if not args:
            print("** class name missing **")
            return

        largs = args.split(" ")

        if largs[0] in classList:
            if len(largs) == 1:
                print("** instance id missing **")
                return

            objs = storage.all()
            idObj = largs[0] + '.' + largs[1]
            if not objs[idObj]:
                print("** no instance found **")
                return
            del objs[idObj]
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not
        on the class name"""

        objs = storage.all()

        if not args:
            val_l = []
            for val in objs.values():
                val_l.append(str(val))
            if val_l:
                print(val_l)
        else:
            largs = args.split(" ")
            if largs[0] not in classList:
                print("** class doesn't exist **")
                return
            val_l = []
            for val in objs.values():
                if(val.__class__.__name__ == largs[0]):
                    val_l.append(str(val))
            if val_l:
                print(val_l)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)"""

        if not args:
            print("** class name missing **")
            return

        objs = storage.all()
        largs = args.split(" ")

        if len(largs) == 0 or largs[0] not in classList:
            print("** class doesn't exist **")
            return
        if len(largs) == 1:
            print("** instance id missing **")
            return

        c_key = largs[0] + '.' + largs[1]
        obj = objs[c_key]
        if not obj:
            print("** no instance found **")
            return

        if len(largs) == 2:
            print("** attribute name missing **")
            return
        if len(largs) == 3:
            print("** value missing **")
            return

        setattr(obj, largs[2], largs[3])
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
