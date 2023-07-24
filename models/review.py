#!/usr/bin/python3
"""Review module that define a subclass of BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class a subclass of BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
