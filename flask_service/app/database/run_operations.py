from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Base
from database_operations import populate_testing_user_data, populate_testing_role_data

# Tworzenie silnika
engine = create_engine('sqlite:///my_database.db', echo=True)

# Sprawdzenie, czy baza danych już istnieje
inspector = inspect(engine)
if not inspector.get_table_names():
    # Baza danych jest pusta, tworzymy schematy
    Base.metadata.create_all(engine)

# Tworzenie sesji
Session = sessionmaker(bind=engine)
session = Session()

populate_testing_user_data(session)
populate_testing_role_data(session)

# Zamykanie sesji
session.close()