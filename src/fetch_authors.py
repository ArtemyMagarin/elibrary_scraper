
'''
    This script fetchs authors data from elibrary.ru
    into database
'''

from datetime import datetime

from ELibraryScraper import ELibraryAPI
from ELibraryScraper.config import ucode as key

from utils import get_session, toCorrectType, equals
from models import ElibraryAuthor


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

session.close()

