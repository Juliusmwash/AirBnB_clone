#!usr/bin/python3
'''
Module: Class User
'''
from models.base_model import BaseModel


class User(BaseModel):
    ''' The user module inherits the base module
    extends it some user attributes '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
