#!/usr/bin/python3
"""Defines a user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines a User class that inherits from the BaseModel class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
