#!/usr/bin/python3


""" Module models/base"""
import json
import os


class Base:
    """ class Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ function __init__ """
        if id is not None or not isinstance(id, int):
            self.id = id
        Base.__nb_objects += 1
        self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ function to_json_string """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ function save_to_file """
        file = cls.__name__ + ".json"
        with open(file, "w") as js_file:
            if list_objs is None:
                js_file.write("[]")
            else:
                dicty = [object.to_dictionary() for object in list_objs]
                js_file.write(Base.to_json_string(dicty))

    @staticmethod
    def from_json_string(json_string):
        """ function from_json_string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    '''
    @classmethod
    def create(cls, **dictionary):
        """ function create """
        if cls.__name__ == "Base":
            return cls(dictionary["id"])
        else:
            ret_cls = cls(1, 1)
        ret_cls.update(**dictionary)
        return ret_cls
    @classmethod
    def load_from_file(cls):
        """ function load_from_file """
        filename = "{}.json".format(cls.__name__)
        if not os.path.exists(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            data = f.read()
        input_li = Base.from_json_string(data)
        ret_li = [cls.create(**obj) for obj in input_li]
        return ret_li
    '''
