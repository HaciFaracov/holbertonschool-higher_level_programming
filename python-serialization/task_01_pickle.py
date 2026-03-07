#!/usr/bin/python3
"""
This module demonstrates object serialization using the pickle module.
"""
import pickle


class CustomObject:
    """
    A custom class representing an object with name, age, and student status.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a new instance of CustomObject.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the attributes of the object in a specific format.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serializes the current instance and saves it to a file.

        Args:
            filename (str): The name of the file to save the data.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and returns an instance of CustomObject from a file.

        Args:
            filename (str): The name of the file to read from.

        Returns:
            CustomObject: The deserialized instance, or None if it fails.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None
        except Exception:
            return None
