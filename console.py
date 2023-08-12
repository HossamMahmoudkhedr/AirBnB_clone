#!/usr/bin/python3
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.review import Review
from models.state import State
from models.user import User
from models.place import Place
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    ''' The HBNB interpreter implementation class '''
    prompt ="(hbnb) "

    def do_EOF(self, arg):
        ''' This function used to quit the cmd '''
        return True

    def do_quit(self, arg):
        ''' This function used to quit the cmd '''
        return True

    def emptyline(self):
        ''' Do nothing on an empty line '''
        pass

    def do_create(self, arg):
        ''' Creates a new instance of BaseModel '''
        if not arg:
            print("** class name missing **")
        elif issubclass(eval(arg), BaseModel):
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        ''' Prints the string representation of an instance based on the class name and id '''
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif issubclass(eval(args[0]), BaseModel):
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")

    def do_destroy(self, arg):
        ''' Deletes an instance based on the class name and id '''

    def do_all(self, arg):
        ''' Prints all string representation of all instances based or not on the class name '''

    def do_update(self, arg):
        ''' Updates an instance based on the class name and id '''

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
