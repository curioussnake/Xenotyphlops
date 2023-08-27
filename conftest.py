import pytest

from services.flaskapi.usersapi import UsersApi
from services.flaskapi.rolesapi import RolesApi

@pytest.fixture(scope="session")
def users_api():
    return UsersApi('http://localhost:8080')

@pytest.fixture(scope="session")
def roles_api():
    return RolesApi('http://localhost:8080')