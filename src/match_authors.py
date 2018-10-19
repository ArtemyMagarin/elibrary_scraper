
from utils import get_session
from models import ElibraryAuthor, Personnel


#init DB session
session = get_session()

# getting all authors from db
elibrary_authors = session.query(ElibraryAuthor).all()

for el_author in elibrary_authors:
    personnels = session.query(Personnel).\
        filter(Personnel.lastName==el_author.lastName,
               Personnel.firstName==el_author.firstName,
               Personnel.middleName==el_author.secondName).all()

    if len(personnels):
        if len(personnels) == 1:
            el_author.Personnel=personnels[0]
            session.add(el_author)
            session.commit()
        else:
            print('Conflict for elibrary author {el_id}: candidates: [{personnels}]'.format(el_id=str(el_author.id), personnels=', '.join([str(p.id) for p in personnels])))
    else:
        print('Can\'t find personnel for elibrary author {}'.format(' '.join([str(el_author.id), el_author.firstName, el_author.lastName, ])))

session.close()



