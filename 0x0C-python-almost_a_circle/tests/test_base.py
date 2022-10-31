#!/usr/bin/python3


""" Module test_base"""
import os
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ class TestBase """

    def test_normal(self):
        """ function test_normal """
        self.base = Base(6)
        self.assertEqual(self.base.id, 6)
        self.base = Base()
        self.assertEqual(self.base._Base__nb_objects, 7)
        self.base = Base()
        self.assertEqual(self.base.id, 8)


    def test_arg_count(self):
        """ function test_arg_count """
        with self.assertRaises(TypeError):
            self.base = Base(2, 2)

    def test_json(self):
        """ function test_json """
        self.base = Base()
        dic = {"test": 1, "test2": 2, "test3": 3}
        lidi = [dic]
        json_dict = self.base.to_json_string(lidi)
        self.assertTrue(isinstance(json_dict, str))
        dic1 = {"test": 1, "test2": 2, "test3": 3}
        lidi = [dic, dic1]
        json_dict = self.base.to_json_string(lidi)
        self.assertTrue(isinstance(json_dict, str))
        json_dict = self.base.to_json_string([])
        self.assertEqual(json_dict, "[]")
        json_dict = self.base.to_json_string(None)
        self.assertEqual(json_dict, "[]")

    def test_json_to_file(self):
        """ function test_json_to_file """
        self.r1 = Rectangle(1, 2)
        Rectangle.save_to_file([self.r1])
        with open("Rectangle.json", "r") as f:
            data = f.read()
            self.assertEqual(len(data), 52)
        self.r2 = Rectangle(3, 4)
        Rectangle.save_to_file([self.r1, self.r2])
        with open("Rectangle.json", "r") as f:
            data = f.read()
            self.assertEqual(len(data), 104)
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            data = f.read()
            self.assertEqual(len(data), 2)

    def test_from_json(self):
        """ function test_from_json """
        self.rec = Rectangle(1, 2)
        li = [self.rec.to_dictionary()]
        json_list_input = Rectangle.to_json_string(li)
        from_json = Rectangle.from_json_string(json_list_input)
        self.assertTrue(isinstance(from_json, list))
        self.assertTrue(isinstance(from_json[0], dict))
        self.assertEqual(Rectangle.from_json_string(None), [])
        self.assertEqual(Rectangle.from_json_string("[]"), [])

    def test_create_cls(self):
        """ function test_create_cls """
        self.r1 = Rectangle(10, 10, 10)
        self.r1_dict = self.r1.to_dictionary()
        
