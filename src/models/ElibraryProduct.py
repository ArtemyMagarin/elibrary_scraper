from . import *

class ElibraryProduct(Base):
    __table__ = Table('tElibraryProducts', metadata, autoload=True)
