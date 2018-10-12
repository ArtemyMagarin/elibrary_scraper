from . import *

class ElibraryAuthorElibraryProduct(Base):
    __table__ = Table('tElibraryAuthorElibraryProduct', metadata, autoload=True)
