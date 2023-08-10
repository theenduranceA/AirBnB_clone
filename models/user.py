#!/usr/bin/python3
"""Module containing a user class that inherits from BaseModel."""

from models.base_model import BaseModel


class User(BaseModel):
    """A user class of public attributes."""

    email = ''

    password = ''

    first_name = ''

    last_name = ''
