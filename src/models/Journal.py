from . import *

class Journal(Base):
    __table__ = Table(
        'tJournals', 
        metadata, 
        autoload=True)
