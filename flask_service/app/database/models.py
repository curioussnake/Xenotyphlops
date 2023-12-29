# models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    user_lastname = Column(String)
    user_role_id = Column(Integer, ForeignKey('roles.role_id'))
    role = relationship("Role", back_populates="users")


class Role(Base):
    __tablename__ = 'roles'

    role_id = Column(Integer, primary_key=True)
    role_name = Column(String)
    role_description = Column(String)
    users = relationship("User", back_populates="role")
