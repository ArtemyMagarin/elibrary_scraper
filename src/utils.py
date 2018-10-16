from config import db_login, db_password
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_session():
    engine = create_engine('mssql+pyodbc://{db_login}:{db_password}@localhost:1433/sciratedb?driver=SQL+Server+Native+Client+10.0'.format(
        db_login=db_login,
        db_password=db_password))

    Session = sessionmaker(bind=engine)
    session = Session()

    return session
