from delayed_assert import expect


def test_get_all_users(users_api):
    all_users = users_api.get_list_of_all_users()
    print("all users result: " + all_users.text)
    assert all_users.status_code == 200
    expect(len(all_users.json()) == 2, "Number of accounts is incorrect!")


def test_create_user(users_api):
    all_users = users_api.get_list_of_all_users()
    create_user = users_api.create_user("Pedro", "Sanchez", role="MODERATOR")
    assert create_user.status_code == 201
    new_user = users_api.get_user_by_id(create_user.json()["id"], accept="application/json")
    # print(new_user.json()["name"])
    assert new_user.status_code == 200
    new_user_json = new_user.json()
    expect(new_user_json["name"] == "Pedro", "Incorrect name!")
    expect(new_user_json["surname"] == "Sanchez", "Incorrect surname!")
    expect(new_user_json["role"] == "MODERATOR", "Incorrect role!") #To beda miekkie asercje
    all_users_after_creation = users_api.get_list_of_all_users()
    assert all_users_after_creation.status_code == 200
    assert len(all_users.json()) < len(all_users_after_creation.json()) #To bedzie miekka asercja


def test_get_user_by_id_positive(users_api):
    user_id = "tfirsttest"
    get_user_by_id = users_api.get_user_by_id(user_id, accept="application/json")
    assert get_user_by_id.status_code == 200
    get_user_by_id_json = get_user_by_id.json()
    # print("here is my printed stuff")
    # print(get_user_by_id_json)
    expect(get_user_by_id_json["name"] == "Test")
    expect(get_user_by_id_json["lastname"] == "FirstTest")
    expect(get_user_by_id_json["role"] == "NONE")


def test_update_user(users_api):
    user_id = "tfirsttest"
    get_user_by_id = users_api.get_user_by_id(user_id)
    assert get_user_by_id.status_code == 200
    update_user = users_api.update_user("tfirsttest", "Pablo", "Pueblo", "MODERATOR")
    assert update_user.status_code == 200
    get_user_by_id_json = get_user_by_id.json()
    expect(get_user_by_id_json["names"] == "Pablo")
    expect(get_user_by_id_json["surname"] == "Pueblo")
    expect(get_user_by_id_json["role"] == "MODERATOR")
    print("user with id =" + user_id + " and data " + get_user_by_id.content + " updated with: " + update_user.content)

def test_delete_user(users_api):
    user_id = "tfirsttest"
    get_user_by_id = users_api.get_user_by_id(user_id)
    assert get_user_by_id.status_code == 200
    delete_user = users_api.delete_user(user_id)
    assert delete_user.status_code == 200
    get_deleted_user_by_id = users_api.get_user_by_id(user_id)
    assert get_deleted_user_by_id.status_code == 404



    #Delayed assert (miekka asercja)
    #Zweryfikowac w asercji: 1.Kod odpowiedzi, 2.Dane, 3.Jezeli jest
    # POST lub UPDATE to zweryfikowac czy dane sa poprawnie zaaktualizowane

    #Przekazywanie headerow na poziomie testow, jezeli jest to potrzebne - mozna testowac poprawne zachowanie dla roznych naglowkow.
    #Metoda Except - zamiast asercji - assert expectations - zamiast zwyklych asercji w ktorych niepowodzenie dowolnej z nich powoduje przerwanie sprawdzania kolejnych
    # W przypadku assert expectation - punkt przerwania - jezeli ktoras z metod expect nie zostanie spelniona.

    #TODO: 4. Sprawdzic Runtime environment, zeby byl ustawiony w rootcie (A nie w katalogu /tests/ poniewaz w /tests/ nie ma fixtureow wiec nie moze z nich skorzystac!
