#!/usr/bin/python3
"""Defines a City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines a City class that inherits from the BaseModel class"""
    state_id = ""
    name = ""
