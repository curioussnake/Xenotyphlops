def test_get_list_of_all_roles(roles_api):
    get_list = roles_api.get_list_of_all_roles()
    assert get_list.status_code == 200
    assert len(get_list.json()) == 4


def test_get_role_by_id(roles_api):
    role_id = "Admin"
    get_role = roles_api.get_role_by_id(role_id, accept="application/json")
    assert get_role.status_code == 200
    get_role_by_id_json = get_role.json()
    assert get_role_by_id_json["name"] == "Admin", "Incorrect id!"
    assert get_role_by_id_json["description"] == "For admit content and service.", "Incorrect description"
    print("role with id: " + role_id + " is " + get_role.text)

