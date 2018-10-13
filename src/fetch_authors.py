
'''
    This script fetchs authors data from elibrary.ru
    into database
'''
from datetime import datetime

from ELibraryScraper import ELibraryAPI
from ELibraryScraper.config import ucode as key

from utils import get_session
from models import ElibraryAuthor

def toCorrectType(value):
    '''
        If value is string, but must be a float ot int,
        this function convert it
    '''
    if value and type(value) == str:
        if value.upper() == value.lower():
            if value.find(',') + 1 or value.find('.') + 1:
                value = float(value.replace(',', '.'))
            else:
                value = int(value)

    return value


def equals(val1, val2):
    if type(val1) == type(val2) == float:
        return ((val1 - val2) ** 2) < (0.001 ** 2)
    else:
        return val1 == val2


el = ELibraryAPI(key=key)
session = get_session()

authors_id = el.get_authors_id()
authors = [ el.get_author_info(a_id) for a_id in authors_id ]

for author in authors:
    # get author from DB
    db_author = session.query(ElibraryAuthor).filter(
        ElibraryAuthor.elibraryAuthorId == author['elibraryAuthorId']).first()

    was_updated = False
    was_created = False

    if not db_author:
        db_author = ElibraryAuthor()
        was_created = True

    for key in author:
        value = toCorrectType(author[key])
        db_value = db_author.__getattribute__(key)

        if not equals(db_value, value):
            was_updated = True
            db_author.__setattr__(key, value)

    nowdate = datetime.now()
    if was_created:
        db_author.createdAt = nowdate

    if was_created or was_updated:
        db_author.updatedAt = nowdate
        session.add(db_author)

session.commit()

