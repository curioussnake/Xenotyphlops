from delayed_assert import expect, assert_expectations


def test_get_all_users(users_api):
    all_users = users_api.get_list_of_all_users()
    print("all users result: " + all_users.text)
    assert all_users.status_code == 200
    amount_of_users: int = len(all_users.json())
    expect(amount_of_users == 2, "Number of accounts is incorrect!")
    assert_expectations()


def test_create_user(users_api):
    all_users = users_api.get_list_of_all_users()
    create_user = users_api.create_user("Rodriguez", "Gonzalez", role="MODERATOR")
    assert create_user.status_code == 201
    new_user = users_api.get_user_by_id(create_user.json()["id"], accept="application/json")
    assert new_user.status_code == 200
    new_user_json = new_user.json()
    expect(new_user_json["name"] == "Rodriguez", "Incorrect name!")
    expect(new_user_json["lastname"] == "Gonzalez", "Incorrect surname!")
    expect(new_user_json["role"] == "MODERATOR", "Incorrect role!")  # To beda miekkie asercje
    all_users_after_creation = users_api.get_list_of_all_users()
    assert all_users_after_creation.status_code == 200
    expect(len(all_users.json()) < len(all_users_after_creation.json()))  # To bedzie miekka asercja
    assert_expectations()


def test_get_user_by_id_positive(users_api):
    user_id = "rgonzalez"
    get_user_by_id = users_api.get_user_by_id(user_id, accept="application/json")
    assert get_user_by_id.status_code == 200
    get_user_by_id_json = get_user_by_id.json()
    expect(get_user_by_id_json["name"] == "Rodriguez")
    expect(get_user_by_id_json["lastname"] == "Gonzalez")
    expect(get_user_by_id_json["role"] == "MODERATOR")
    assert_expectations()


def test_update_user(users_api):
    user_id = "tfirsttest"
    get_user_by_id_before_update = users_api.get_user_by_id(user_id)
    assert get_user_by_id_before_update.status_code == 200
    update_user = users_api.update_user("tfirsttest", "Pablo", "Pueblo", "MODERATOR")
    assert update_user.status_code == 200
    get_user_by_id_after_update = update_user.json()
    print(get_user_by_id_after_update)
    expect(get_user_by_id_after_update["name"] == "Pablo")
    expect(get_user_by_id_after_update["lastname"] == "Pueblo")
    expect(get_user_by_id_after_update["role"] == "MODERATOR")
    assert_expectations()


def test_delete_user(users_api):
    user_id = "tfirsttest"
    get_user_by_id = users_api.get_user_by_id(user_id)
    assert get_user_by_id.status_code == 200
    delete_user = users_api.delete_user(user_id)
    assert delete_user.status_code == 200
    get_deleted_user_by_id = users_api.get_user_by_id(user_id)
    assert get_deleted_user_by_id.status_code == 404
    assert_expectations()

    # Delayed assert (miekka asercja)
    # Zweryfikowac w asercji: 1.Kod odpowiedzi, 2.Dane, 3.Jezeli jest
    # POST lub UPDATE to zweryfikowac czy dane sa poprawnie zaaktualizowane

    # Przekazywanie headerow na poziomie testow, jezeli jest to potrzebne - mozna testowac poprawne zachowanie dla roznych naglowkow.
    # Metoda Except - zamiast asercji - assert expectations - zamiast zwyklych asercji w ktorych niepowodzenie dowolnej z nich powoduje przerwanie sprawdzania kolejnych
    # W przypadku assert expectation - punkt przerwania - jezeli ktoras z metod expect nie zostanie spelniona.

    # TODO: 4. Sprawdzic Runtime environment, zeby byl ustawiony w rootcie (A nie w katalogu /tests/ poniewaz w /tests/ nie ma fixtureow wiec nie moze z nich skorzystac!
