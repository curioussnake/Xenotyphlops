def test_get_all_users(users_api):
    all_users = users_api.get_list_of_all_users()
    print("all users result: " + all_users.text)
    assert len(all_users.json()) == 2


def test_create_user(users_api):
    all_users = users_api.get_list_of_all_users()
    create_user = users_api.create_user("Pedro", "Sanchez", role="MODERATOR")
    assert create_user.status_code == 201
    new_user = users_api.get_user_by_id(create_user.json()["id"])
    # print(new_user.json()["name"])
    assert new_user.status_code == 200
    new_user_json = new_user.json()
    assert new_user_json["name"] == "Pablo", "Incorrect name!"
    assert new_user_json["surname"] == "Pueblo", "Incorrect surname!"
    assert new_user_json["role"] == "MODERATOR", "Incorrect role!" #To beda miekkie asercje
    all_users_after_creation = users_api.get_list_of_all_users()
    assert all_users_after_creation.status_code == 200
    assert len(all_users.json()) < len(all_users_after_creation.json()) #To bedzie miekka asercja



def test_get_user_by_id_positive(users_api):
    user_id = "tfirsttest"
    get_user_by_id = users_api.get_user_by_id(user_id)
    assert get_user_by_id.status_code == 200
    get_user_by_id_json = get_user_by_id.json()
    assert get_user_by_id_json["name"] == "Test"
    assert get_user_by_id_json["lastname"] == "FirstTest"
    assert get_user_by_id_json["role"] == "NONE"


def test_update_user(users_api):
    user_id = "tfirsttest"
    get_user_by_id = users_api.get_user_by_id(user_id)
    update_user = users_api.update_user("tfirsttest", "Pablo", "Pueblo", "MODERATOR")
    print("user with id =" + user_id + " and data " + get_user_by_id.content + " updated with: " + update_user.content)

    #Delete assert (miekka asercja)
    #Zweryfikowac w asercji: 1.Kod odpowiedzi, 2.Dane, 3.Jezeli jest
    # POST lub UPDATE to zweryfikowac czy dane sa poprawnie zaaktualizowane

    #Przekazywanie headerow na poziomie testow, jezeli jest to potrzebne - mozna testowac poprawne zachowanie dla roznych naglowkow.
    #Metoda Except - zamiast asercji - assert expectations - zamiast zwyklych asercji w ktorych niepowodzenie dowolnej z nich powoduje przerwanie sprawdzania kolejnych
    # W przypadku assert expectation - punkt przerwania - jezeli ktoras z metod expect nie zostanie spelniona.

    #TODO: 2. test_users, test_roles - dodac asercje
    #TODO: 3. Ogarnac Expect assert (Biblioteka sie nazywa Delayed Assert
    #TODO: 4. Sprawdzic Runtime environment, zeby byl ustawiony w rootcie (A nie w katalogu /tests/ poniewaz w /tests/ nie ma fixtureow wiec nie moze z nich skorzystac!
