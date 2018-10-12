from . import *

class ElibraryProductType(Base):
    __table__ = Table('tElibraryProductTypes', metadata, autoload=True)
