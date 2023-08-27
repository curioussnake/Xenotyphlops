def test_get_list_of_all_roles(roles_api):
    get_list = roles_api.get_list_of_all_roles()
    print("roles list: " + get_list.content)


def test_get_role_by_id(roles_api):
    role_id = 1111
    get_role = roles_api.get_role_by_id(role_id)
    print("role with id: " + role_id + " is " + get_role.text)
