from pydantic import BaseModel
from typing import List

class Planilha( BaseModel ):

    name: str
    description: str

class User( BaseModel ):

    username: str
    email: str
    password: str

class UserLogin( BaseModel ):

    username: str
    password: str

"""
class UserInfo( BaseModel ):

    username: str
    email: str
    planilhas: List[Planilha] = []

    class Config:
        from_attributes = True
"""