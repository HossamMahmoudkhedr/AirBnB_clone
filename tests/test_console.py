#!/usr/bin/python3
''' Unit testing module for the  class '''
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
from models.base_model import BaseModel
from models.place import Place


class TestHBNBCommand_help_quit(unittest.TestCase):
    '''Unittest to test the console'''

    def test_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand().prompt)

    def test_enter(self):
        message = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(message, f.getvalue().strip())

    def test_quit(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommand_create(unittest.TestCase):
    ''' unittest for the create command '''
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp.json")
        except IOError:
            pass
        FileStorage.__objects = {}
        self.hbnb = HBNBCommand()

    def tearDown(self):
        try:
            os.remove("file.json")
            os.rename("temp.json", "file.json")
        except Exception:
            pass

    def test_create_missing_class(self):
        errMessage = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.hbnb.onecmd("create")
            self.assertEqual(errMessage, f.getvalue().strip())

    def test_create_exist_class(self):
        errMessage = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.hbnb.onecmd("create MyModal")
            self.assertEqual(errMessage, f.getvalue().strip())

    def test_create_instance(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.hbnb.onecmd("create BaseModel")
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("BaseModel.{}".format(f.getvalue().strip()),
                          storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            self.hbnb.onecmd("create Amenity")
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Amenity.{}".format(f.getvalue().strip()),
                          storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            self.hbnb.onecmd("create City")
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("City.{}".format(f.getvalue().strip()),
                          storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            self.hbnb.onecmd("create Place")
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Place.{}".format(f.getvalue().strip()),
                          storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            self.hbnb.onecmd("create Review")
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Review.{}".format(f.getvalue().strip()),
                          storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            self.hbnb.onecmd("create State")
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("State.{}".format(f.getvalue().strip()),
                          storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            self.hbnb.onecmd("create User")
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("User.{}".format(f.getvalue().strip()),
                          storage.all().keys())
