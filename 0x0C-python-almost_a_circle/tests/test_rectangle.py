#!/usr/bin/python3


""" Module test_rectangle"""
import sys
import io
import unittest

from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """ class TestRectangle """

    def test_parent(self):
        """ function test_parent """
        self.rec = Rectangle(1, 2)
        self.assertTrue(isinstance(self.rec, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertEqual(self.rec.id, 17)
        self.rec = Rectangle(1, 2)
        self.rec = Rectangle(1, 2)
        self.rec = Rectangle(1, 2)
        self.assertEqual(self.rec.id, 20)

    def test_init(self):
        """ function test_init """
        self.rec = Rectangle(1, 2, 3, 4, 10)
        self.assertEqual(self.rec.width, 1)
        self.assertEqual(self.rec.height, 2)
        self.assertEqual(self.rec.x, 3)
        self.assertEqual(self.rec.y, 4)
        self.assertEqual(self.rec.id, 15)

        self.rec = Rectangle(1, 2)
        self.assertEqual(self.rec.x, 0)
        self.assertEqual(self.rec.y, 0)
        self.assertEqual(self.rec.id, 16)


    def test_etc(self):
        """ function test_etc """
        with self.assertRaises(TypeError):
            self.rec = Rectangle(1)
        with self.assertRaises(TypeError):
            self.rec = Rectangle()
        with self.assertRaises(TypeError):
            self.rec = Rectangle(1, 2, 3, 4, 5, 6)

    def test_area(self):
        """ function test_area """
        self.rec = Rectangle(4, 2)
        self.assertEqual(self.rec.area(), 8)
        self.rec1 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(self.rec1.area(), 56)

    def test_display(self):
        """ function test_display """
        self.rec = Rectangle(3, 3)
        cap_out = io.StringIO()
        sys.stdout = cap_out
        self.rec.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(cap_out.getvalue(), "###\n###\n###\n")
        self.rec = Rectangle(2, 3, 1, 2)
        cap_out = io.StringIO()
        sys.stdout = cap_out
        self.rec.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(cap_out.getvalue(), "\n\n ##\n ##\n ##\n")

    def test_str(self):
        """ function test_str """
        self.rec = Rectangle(4, 5)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (23) 0/0 - 4/5")
        self.rec = Rectangle(4, 5, 12, 1, 24)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (24) 12/1 - 4/5")

    def test_update(self):
        """ function test_update """
        self.rec = Rectangle(10, 10, 10, 10)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (26) 10/10 - 10/10")
        self.rec.update(98)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (98) 10/10 - 10/10")
        self.rec.update(98, 2)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (98) 10/10 - 2/10")
        self.rec.update(98, 2, 3)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (98) 10/10 - 2/3")
        self.rec.update(98, 2, 3, 4)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (98) 4/10 - 2/3")
        self.rec.update(98, 2, 3, 4, 5)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (98) 4/5 - 2/3")
        self.rec = Rectangle(10, 10, 10, 10)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (27) 10/10 - 10/10")
        self.rec.update(id=98)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (98) 10/10 - 10/10")
        self.rec.update(id=98, width=2)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (98) 10/10 - 2/10")
        self.rec.update(id=98, width=2, height=3)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (98) 10/10 - 2/3")
        self.rec.update(id=98, width=2, height=3, x=4)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (98) 4/10 - 2/3")
        self.rec.update(id=98, width=2, height=3, x=4, y=5)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (98) 4/5 - 2/3")

        with self.assertRaises(TypeError):
            self.rec.update(width="f")
        self.rec1 = Rectangle(1, 2)
        self.rec1.update(3, 3, id=9)
        self.assertEqual(self.rec1.__str__(), "[Rectangle] (3) 0/0 - 3/2")


    def test_to_json(self):
        """ function test_to_json """
        self.rec = Rectangle(10, 10, 10, 10, 10)
        rec_dict = self.rec.to_dictionary()
        json_dict = Base.to_json_string([rec_dict])
        self.assertTrue(isinstance(json_dict, str))

    def test_save_json(self):
        """ function test_save_json """
        self.r1 = Rectangle(1, 2)
        Rectangle.save_to_file([self.r1])
        with open("Rectangle.json", "r") as f:
            data = f.read()
            self.assertEqual(len(data), 53)
        self.r2 = Rectangle(3, 4)
        Rectangle.save_to_file([self.r1, self.r2])
        with open("Rectangle.json", "r") as f:
            data = f.read()
            self.assertEqual(len(data), 106)
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
       
if __name__ == "__name__":
    unittest.main()
