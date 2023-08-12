#!/usr/bin/python3
""" This module defines the entry point of the command interpreter """
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    ''' The HBNB interpreter implementation class '''
    prompt ="(hbnb) "

    classes = ['BaseModel', 'City', 'Amenity', 'Place', 'Review', 'State', 'User']
    def do_help(self, arg):
        """To get help on a command, type help <topic>.
        """
        return super().do_help(arg)

    def do_EOF(self, arg):
        ''' This function used to quit the cmd '''
        print("")
        return True

    def do_quit(self, arg):
        '''Quit command to exit the program
        '''
        return True

    def emptyline(self):
        ''' Do nothing on an empty line '''
        pass

    def do_create(self, arg):
        ''' Creates a new instance of BaseModel '''
        args = arg.split()
        if not args[0] in self.classes:
            print("** class name missing **")
        elif args[0] in self.classes:
            new_instance = eval(args[0])()

            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        ''' Prints the string representation of an instance based on the class name and id '''
        args = arg.split()
        object = storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in object:
            print("** instance id missing **")
        else:
            selectedInstance = object["{}.{}".format(args[0], args[1])]
            print("{}".format(selectedInstance))

    def do_destroy(self, arg):
        ''' Deletes an instance based on the class name and id '''
        args = arg.split()
        object = storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in object:
            print("** no instance found **")
        else:
            selectedInstance = "{}.{}".format(args[0], args[1])
            object.pop(selectedInstance)
            storage.save()

    def do_all(self, arg):
        ''' Prints all string representation of all instances based or not on the class name '''
        args = arg.split()
        object = storage.all()
        if len(args) == 0:
            for key, value in object.items():
                print(key, value)
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) != 0:
            for key, value in object.items():
                if value.__class__.__name__ ==  args[0]:
                    print(key, value)

    def do_update(self, arg):
        ''' Updates an instance based on the class name and id '''
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        object = storage.all()
        instance_key = f"{class_name}.{instance_id}"

        if instance_key not in object:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]

        instance = object[instance_key]
        if attribute_name in ["id", "created_at", "updated_at"]:
            return
        elif hasattr(instance, attribute_name):
            attribute_type = type(getattr(instance, attribute_name))
            if attribute_type is str:
                attribute_value = attribute_value.strip('"')
            elif attribute_type is int:
                attribute_value = int(attribute_value)
            elif attribute_type is float:
                attribute_value = float(attribute_value)
            setattr(instance, attribute_name, attribute_value)
            storage.save()
        else:
            print("** attribute doesn't exist **")

    def default(self, line):
        ''' Handles all the method call syntax and non-command cases'''
        cls_name = line[:line.find('.')]
        try:
            if not issubclass(eval(cls_name), BaseModel):
                print("** class doesn't exist **")
                return
        except NameError:
            print("** class doesn't exist **")
            return

        mthd_name = line[line.find('.') + 1:line.find('(')]
        args = line[line.find('(') + 1:line.find(')')]
        if mthd_name == 'all' or mthd_name == 'count':
            all_found = []
            for key, value in storage.all().items():
                if key[:key.find('.')] == cls_name:
                    all_found.append(str(value))
            
            if mthd_name == 'all':
                print(all_found)
            else:
                print(len(all_found))
        elif mthd_name == 'show' or mthd_name == 'destroy':
            eval(f'self.do_{mthd_name}("{cls_name} {args}")')
        elif mthd_name == 'update':
            args = [ string.strip() for string in args.split(',')]
            if args[1][0] == '{':
                dict_repr = dict(eval(args[1]))
                for key, value in dict_repr.items():
                    self.do_update(f"{cls_name} {args[0]} {key} {value}")
            else:
                self.do_update(f"{cls_name} {args[0]} {args[1]} {args[2]}")
        else:
            print("** unknown method  **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
