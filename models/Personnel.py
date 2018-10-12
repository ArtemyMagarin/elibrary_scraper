from . import *

class Personnel(Base):
    __table__ = Table('tPersonnel', metadata, autoload=True)