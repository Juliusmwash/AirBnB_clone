#!/usr/bin/python3
"""
Module: class city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines a city model.

    Attributes:
        name and 
        state_id
    """
    state_id = ""
    name = ""
