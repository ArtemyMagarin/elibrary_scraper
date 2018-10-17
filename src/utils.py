from config import db_login, db_password
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import re

def get_session():
    engine = create_engine('mssql+pyodbc://{db_login}:{db_password}@localhost:1433/sciratedb?driver=SQL+Server+Native+Client+10.0'.format(
        db_login=db_login,
        db_password=db_password))

    Session = sessionmaker(bind=engine)
    session = Session()

    return session


def toCorrectType(value):
    '''
        If value is string, but must be a float or int,
        this function convert it
    '''
    if value and type(value) == str:
        if len(re.findall(r"^\d{1,}[,.]?\d{0,}$", value)): 
            if value.find(',') + 1 or value.find('.') + 1:
                value = float(value.replace(',', '.'))
            else:
                value = int(value)

    return value


def equals(val1, val2):
    if type(val1) == type(val2) == float:
        return ((val1 - val2) ** 2) < (0.001 ** 2)
    else:
        return val1 == val2

