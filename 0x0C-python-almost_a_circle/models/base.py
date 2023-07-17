#!/usr/bin/python3
"""
    Defines the Base class
"""
import json
import csv


class Base:
    """Represents Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor."""
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json string representation"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json represetnation of list-objs to a file"""
        with open(cls.__name__ + ".json", "w") as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Deserializes the JSON string"""
        if json_string == "[]" or json_string is None:
            return[]
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """gets instance with all attributs"""
        if dictionary != {} and dictionary:
            if cls.__name__ == "Rectangle":
                n = cls(1, 1)
            else:
                n = cls(1)
            n.update(**dictionary)
            return n

    @classmethod
    def load_from_file(cls):
        """Gets the list of instances"""
        f = str(cls.__name__) + ".json"
        try:
            with open(f, "r") as jfile:
                dict_list = Base.from_json_string(jfile.read())
                return [cls.create(**a) for a in dict_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves file to csv"""
        csvfile = cls.__name__ + ".csv"
        with open(csvfile, "w", newline="") as csv_file:
            if list_objs == [] or list_objs is None:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_name = ["id", "width", "height", "x", "y"]
                else:
                    field_name = ["id", "size", "x", "y"]
                twrite = csv.DictWriter(csv_file, fieldnames=field_name)
                for j in list_objs:
                    twrite.writerow(j.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """loads file form a csv"""
        csvfile = cls.__name__ + ".csv"
        try:
            with open(csvfile, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    field_name = ['id', 'width', 'height', 'x', 'y']
                else:
                    field_name = ['id', 'size', 'x', 'y']
                listdicts = csv.DictReader(csv_file, fieldnames=field_name)
                listdicts = [dict([n, int(m)] for n, m in j.items())
                             for j in listdicts]
                return [cls.create(**k) for k in listdicts]
        except IOError:
            return []
