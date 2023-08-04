from services.flaskapi.usersapi import UsersApi


tmp = UsersApi('http://localhost:8080')
print(tmp.get_list_of_all_users().status_code)
print(tmp.get_list_of_all_users().text)

# TODO stworzyc do userapi.py z obsluga rolesapi (opisane w readme)