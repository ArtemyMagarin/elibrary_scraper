from . import *
from utils import get_session
from sqlalchemy.sql import text

class SciProduct(Base):
    __table__ = Table(
        'tSciProducts', 
        metadata, 
        autoload=True)

    def get_scirate_authors_id(self):
        s = get_session()
        result = s.query("lnkPersonnel from tAuthorsSciProducts inner join tAuthors on tAuthors.id = tAuthorsSciProducts.lnkAuthor where lnkSciProduct="+str(self.id)).all()
        s.close()
        ids = []
        for r in result:
            if r[0]:
                ids.append(r[0])
        return ids
        
