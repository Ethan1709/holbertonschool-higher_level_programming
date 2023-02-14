#!/usr/bin/python3
""" Base class """
import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ dict to json string """
        if list_dictionaries is None or list_dictionaries == "":
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file """
        l = []
        if list_objs:
            [l.append(v.to_dictionary()) for v in list_objs]

        with open("%s.json" % (cls.__name__), 'w') as f:
            f.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """  returns an instance with all attributes already set """
        if 'rectangle' in cls.__name__.lower():
            r = cls(3, 3)
        else:
            r = cls(3)

        r.update(**dictionary)

        return r

    @classmethod
    def load_from_file(cls):
        """ meow """
        try:
            with open(cls.__name__ + '.json', 'r') as file:
                text = file.read()
        except:
            text = None
        
        data = cls.from_json_string(text)
        return [cls.create(**v) for v in data]
