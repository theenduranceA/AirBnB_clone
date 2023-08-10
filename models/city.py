#!/usr/bin/python3
"""Module containing a city class that inherits from BaseModel."""

from models.base_model import BaseModel


class City(BaseModel):
    """A city class of public attributes."""

    state_id = ''

    name = ''
