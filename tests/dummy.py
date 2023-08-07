from services.flaskapi.usersapi import UsersApi
from services.flaskapi.rolesapi import RolesApi

tmp_users = UsersApi('http://localhost:8080')
tmp_roles = RolesApi('http://localhost:8080')
print(tmp_users.get_list_of_all_users().status_code)
print(tmp_users.get_list_of_all_users().text)
print(tmp_roles.get_list_of_all_roles().text)
print(tmp_users.create_user("Pablo", "Pueblo", role="MODERATOR"))
print(tmp_users.create_user(name="Pablo", lastname="Pueblo", role="MODERATOR"))
print(tmp_users.get_list_of_all_users().text)

# TODO stworzyc do userapi.py z obsluga rolesapi (opisane w readme)
