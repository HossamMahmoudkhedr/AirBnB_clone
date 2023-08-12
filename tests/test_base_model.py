#!/usr/bin/python3
'''Unit testing module for the BaseModel class'''
from models.base_model import BaseModel
from uuid import UUID
from datetime import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    ''' A unittest class for testing the BaseModel class '''

    def setUp(self):
        ''' Set up all the class test units '''
        self.BM1 = BaseModel()
        self.BM1.prop1 = 'val1'
        self.BM1.prop2 = 'val2'
        # args should be ignored
        self.BM2 = BaseModel(
            str(UUID('12345678-1234-5678-1234-567812345678')),
            str(datetime.fromordinal(11111)),
            str(datetime.fromordinal(12345))
        )
        self.BM3 = BaseModel(
            id=str(UUID('12345678-1234-5678-1234-567812345678')),
            created_at=str(datetime.fromordinal(11111)),
            updated_at=str(datetime.fromordinal(12345))
        )

    # too many other tests

    def test_args(self):
        ''' Test that variadic arguments assignment is ignored '''
        self.assertNotEqual(self.BM2.id,
                            str(UUID('12345678-1234-5678-1234-567812345678')))
        self.assertNotEqual(str(self.BM2.created_at),
                            str(datetime.fromordinal(11111)))
        self.assertNotEqual(str(self.BM2.updated_at),
                            str(datetime.fromordinal(12345)))

    def test_kwargs(self):
        ''' Test that key word arguments assignment is correct '''
        self.assertEqual(self.BM3.id,
                         str(UUID('12345678-1234-5678-1234-567812345678')))
        self.assertEqual(str(self.BM3.created_at),
                         str(datetime.fromordinal(11111)))
        self.assertEqual(str(self.BM3.updated_at),
                         str(datetime.fromordinal(12345)))

    def test_dict_recreation(self):
        ''' Test correct to_dict() usage to create identical instances '''
        dict1 = self.BM1.to_dict()
        newcopy = BaseModel(**dict1)
        self.assertDictEqual(newcopy.__dict__, self.BM1.__dict__)
        self.assertDictEqual(newcopy.to_dict(), dict1)

    def test_correct_attribute_types(self):
        ''' Test that the new instance attributes have correct types '''
        self.assertIsInstance(self.BM3.id, str)
        self.assertIsInstance(self.BM3.created_at, datetime)
        self.assertIsInstance(self.BM3.updated_at, datetime)

    def test_correct_dict_assignement(self):
        ''' Test ignoring the '__class__' key in the dict representation '''
        dict1 = self.BM1.to_dict()
        dict1['__class__'] = 'WrongClass'
        newcopy = BaseModel(**dict1)
        self.assertEqual(newcopy.__class__.__name__, 'BaseModel')
        self.assertDictEqual(newcopy.__dict__, self.BM1.__dict__)


if __name__ == '__main__':
    unittest.main()
