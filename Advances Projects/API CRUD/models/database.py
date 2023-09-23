from configs.db import base
from sqlalchemy import Column, Integer, String

class Login(base):
    __tablename__ = "logins"
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    email = Column(String(100))
    password = Column(String())



