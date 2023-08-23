import pytest

from services.flaskapi.usersapi import UsersApi


@pytest.fixture(scope="session")
def users_api():
    return UsersApi('http://localhost:8080')
