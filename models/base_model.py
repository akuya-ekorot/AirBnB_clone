#!/usr/bin/env python3
"""
This is our base model
takes in public instances attributes id,created_at 
and updated at.
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel describes public instance attributes id, 
    created_at and updated at
    """

    def __init__(self):
        # declare attributes
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        # update updated_at everytime the object is changed
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        obj_dict = self.__dict__.copy()  # Create a copy of instance attributes
        obj_dict['__class__'] = self.__class__.__name__  # Add class name

        # Convert created_at and updated_at to ISO format strings
        for attr, value in obj_dict.items():
            if isinstance(value, datetime):
                obj_dict[attr] = value.isoformat()

        return obj_dict
