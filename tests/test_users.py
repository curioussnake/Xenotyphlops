def test_get_all_users(users_api):
    all_users = users_api.get_list_of_all_users()
    print("all users result: " + all_users.text)


def test_create_user(users_api):
    create_user = users_api.create_user(name="Pablo", lastname="Pueblo", role="MODERATOR")
    print("user created: " + create_user.text)


def test_get_user_by_id_positive(users_api):
    user_id = "tfirsttest"
    get_user_by_id = users_api.get_user_by_id(user_id)
    print("user with id =" + user_id + " is: " + get_user_by_id.content)


def test_update_user(users_api):
    user_id = "tfirsttest"
    get_user_by_id = users_api.get_user_by_id(user_id)
    update_user = users_api.update_user("tfirsttest", "Pablo", "Pueblo", "MODERATOR")
    print("user with id =" + user_id + " and data " + get_user_by_id.content + " updated with: " + update_user.content)
