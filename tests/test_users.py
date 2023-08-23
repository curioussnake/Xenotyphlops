def test_get_all_users(users_api):
    all_users = users_api.get_list_of_all_users()
    print("all users result: " + all_users.text)
