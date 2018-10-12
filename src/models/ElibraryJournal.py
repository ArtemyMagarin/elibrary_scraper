from . import *

class ElibraryJournal(Base):
    __table__ = Table('tElibraryJournals', metadata, autoload=True)
