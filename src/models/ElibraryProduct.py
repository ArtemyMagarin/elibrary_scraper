from . import *


class ElibraryProduct(Base):
    __table__ = Table(
        'tElibraryProducts', 
        metadata, 
        autoload=True)
    
    ElibraryProductType = relationship(ElibraryProductType)
    ElibraryJournal     = relationship(ElibraryJournal)
    ElibraryAuthors     = relationship('ElibraryAuthorElibraryProduct')