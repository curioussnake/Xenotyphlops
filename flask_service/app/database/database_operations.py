from sqlalchemy import create_engine
from models import Base, User, Role
def __init__(self):
    self.engine = create_engine('sqlite:///my_database.db', echo=True)
    self.Session = sessionmaker(bind=self.engine)

def get_session(self):
    return self.Session()

def create_tables():
    engine = create_engine('sqlite:///my_database.db', echo=True)
    Base.metadata.create_all(engine)


def populate_testing_role_data(session):
    admin_role = Role(role_name='ADMIN', role_description='For administration purpose')
    moderator_role = Role(role_name='MODERATOR', role_description='To moderate content')
    viewer_role = Role(role_name='VIEWER', role_description='Can only view content')
    none_role = Role(role_name='NONE', role_description='No role assigned currently')

    session.add_all([admin_role, moderator_role, viewer_role, none_role])
    session.commit()


def populate_testing_user_data(session):
    # Dodawanie użytkowników
    user1 = User(user_name='Test', user_lastname='FirstTest', user_role_id=0)
    user2 = User(user_name='John', user_lastname='Testowy', user_role_id=1)

    session.add_all([user1, user2])
    session.commit()


def add_user(session, user_name, user_lastname, user_role_id):
    new_user = User(user_name=user_name, user_lastname=user_lastname, user_role_id=user_role_id)

    session.add_all(new_user)
    session.commit()

def update_user(session, user_id, user_name, user_lastname, user_role_id):
    if user_name == "":
        pass#Pobierz nazwe uzytkownika z id z bazy danych i przypisz do user_name
    if user_lastname == "":
        pass# Pobierz nazwe uzytkownika z id z bazy danych i przypisz do user_lastname
    if user_role_id == "":
        pass#Pobierz role uzytkownika z id z bazy danych i przypisz do user_role_id

def verify_user(session, user_id):
    pass#Sprawdz czy uzytkownik istnieje i zwroc potwierdzenie jezeli tak

def delete_user(session, user_id):
    pass#usun uzytkownika z bazy danych


