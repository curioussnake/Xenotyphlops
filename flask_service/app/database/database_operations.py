from sqlalchemy import create_engine
from models import Base, User, Role


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
