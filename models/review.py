#!/usr/bin/python3
"""Module containing a review class that inherits from BaseModel."""

from models.base_model import BaseModel


class Review(BaseModel):
    """A review class of public attributes."""

    place_id = ''

    user_id = ''

    text = ''
