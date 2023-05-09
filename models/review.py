#!/usr/bin/python3
"""
Module:  Class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """  model to create reviews on the website
    Attributes:
        text
        user_id
        place_id
    """
    place_id = ""
    user_id = ""
    text = ""
