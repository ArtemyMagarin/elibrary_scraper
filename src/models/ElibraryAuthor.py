from . import *

class ElibraryAuthor(Base):
    __table__ = Table(
        'tElibraryAuthors',
        metadata, 
        autoload=True)

    Personnel = relationship('Personnel')
