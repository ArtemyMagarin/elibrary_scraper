from sqlalchemy     import *
from sqlalchemy.orm import create_session
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from config import db_login, db_password

engine = create_engine('mssql+pyodbc://{db_login}:{db_password}@localhost:1433/sciratedb?driver=SQL+Server+Native+Client+10.0'.format(
    db_login=db_login,
    db_password=db_password))

metadata = MetaData(bind=engine)

Base = declarative_base()

from models.Journal                         import Journal


from models.Personnel                       import Personnel
from models.ElibraryProduct                 import ElibraryProduct
from models.ElibraryProductType             import ElibraryProductType
from models.ElibraryJournal                 import ElibraryJournal
from models.ElibraryAuthor                  import ElibraryAuthor
from models.ElibraryAuthorElibraryProduct   import ElibraryAuthorElibraryProduct
from models.ElibraryAuthorPropertyNames     import ElibraryAuthorPropertyNames

__all__ = [ 'Personnel', ]
