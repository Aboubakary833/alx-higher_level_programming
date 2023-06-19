#!/usr/bin/python3

"""Base class module"""
import json
import csv
import os.path


class Base:
    """Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize new Base instance

            Args:
                    id (int, None): Instance id. Defaults to None.
            """
        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Stringify a list of dictionnaries

                Args:
                        list_dictionaries (list): List of dictionnary

                Returns:
                        _type_: _description_
                """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

                Args:
                        list_objs (list): List of object
                """
        filename = "{}.json".format(cls.__name__)
        _list = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                _list.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(_list)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string

                Args:
                        json_string (str): JSON representation

                Returns:
                        list: List of JSON representation
                """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an return instance
        of Base class

                Returns:
                        Base: Base class instance
                """
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Return list of instance

                Returns:
                        list: List of instance
                """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            _list = f.read()

        _cls_list = cls.from_json_string(_list)
        instances_list = []

        for index in range(len(_cls_list)):
            instances_list.append(cls.create(**_cls_list[index]))

        return instances_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save list_objs to csv

                Args:
                        list_objs (list): List of object
                """
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            _dict_list = [0, 0, 0, 0, 0]
            _key_list = ['id', 'width', 'height', 'x', 'y']
        else:
            _dict_list = ['0', '0', '0', '0']
            _key_list = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(_key_list)):
                    _dict_list[kv] = obj.to_dictionary()[_key_list[kv]]
                matrix.append(_dict_list[:])

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """Get and return list of objs from a csv

                Returns:
                        list: Instance list
                """
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            _keys_list = ['id', 'width', 'height', 'x', 'y']
        else:
            _keys_list = ['id', 'size', 'x', 'y']

        matrix = []

        for csv_elem in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[_keys_list[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)

        _instance_list = []

        for index in range(len(matrix)):
            _instance_list.append(cls.create(**matrix[index]))

        return _instance_list
