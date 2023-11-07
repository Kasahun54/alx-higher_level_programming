#!/usr/bin/python3

"""Defines the student class"""


class Student:
    """Represent a student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student

        Args:
            attrs (list): (Optional) attributes
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes

        Args:
            json (dict): The key/value  to replace attributes
        """
        for k, v in json.items():
            setattr(self, k, v)

