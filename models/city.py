#!/user/bin/python3
"""City class that inherit from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class subclass of BaseModel"""

    state_id = ""
    name = ""
