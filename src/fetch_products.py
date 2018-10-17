import sys

from datetime import datetime

from ELibraryScraper import ELibraryAPI
from ELibraryScraper.config import ucode as key

from utils import get_session, toCorrectType, equals
from models import (ElibraryAuthor, ElibraryProduct, 
    ElibraryAuthorElibraryProduct, ElibraryJournal)

# getting args
# if update is on we update old products, else adding new only
UPDATE = '--update' in sys.argv 
# if debug then print info
DEBUG  = '--debug'  in sys.argv

print('Debug mode: ', 'ON' if DEBUG  else 'OFF')
print('Update mode:', 'ON' if UPDATE else 'OFF')
print()

# init API
el = ELibraryAPI(key=key)

#init DB session
session = get_session()

# getting all authors from db
db_authors = session.query(ElibraryAuthor).all()

for db_author in db_authors:
    # getting list of products ids
    products = el.get_products_list_by_author(str(db_author.elibraryAuthorId))
    
    if DEBUG:
        print('For Elibrary author', db_author.elibraryAuthorId,
            'recived', len(products), 'products')
    
    created_counter = 0
    updated_counter = 0

    for product_id in products:
        # check if product with same id is exists
        db_product = session.query(ElibraryProduct).filter(
            ElibraryProduct.elibraryId==product_id).first()

        # if update mode is off, continue
        if db_product and not UPDATE:

            # check anyway: if old product, but new owner, create new m2m
            ap = session.query(ElibraryAuthorElibraryProduct).filter(
                ElibraryAuthorElibraryProduct.lnkElibraryAuthor==db_author.id).filter(
                ElibraryAuthorElibraryProduct.lnkElibraryProduct==db_product.id).first()

            if not ap:
                ap = ElibraryAuthorElibraryProduct()
                ap.ElibraryAuthor  = db_author
                db_product.ElibraryAuthors.append(ap)
                session.add(db_product)
                session.commit()

            continue 

        product = el.get_product_by_id(product_id)
        

        was_updated = False
        was_created = False

        if not db_product:
            db_product = ElibraryProduct()
            was_created = True

        for key in product:
            if key != 'journal':
                value = toCorrectType(product[key])
                db_value = db_product.__getattribute__(key)

                if not equals(db_value, value):
                    was_updated = True
                    db_product.__setattr__(key, value)
            
            if 'journal' in product:
                db_journal = session.query(ElibraryJournal).filter(
                    ElibraryJournal.eLibraryJournalId==int(product['journal']['id'])).first()

                if db_journal:
                    # if impact factor changed
                    if not equals(db_journal.impactFactor, product['journal']['impactFactor']):
                        db_journal.impactFactor = product['journal']['impactFactor']
                        db_journal.updatedAt = datetime.now()
                        session.add(db_journal)
                        session.commit()

                else:
                    db_journal = ElibraryJournal()
                    journal = product['journal']
                    db_journal.eLibraryJournalId = journal['id']
                    db_journal.fname = journal['name']
                    db_journal.impactFactor = journal['impactFactor']
                    db_journal.isVak = journal['isVak']
                    db_journal.issn = journal['issn']
                    db_journal.updatedAt = db_journal.createdAt = datetime.now()
                    session.add(db_journal)
                    session.commit()


                db_product.ElibraryJournal = db_journal

        # if m2m connection not exists or this is a new product, 
        # add connection
        ap = session.query(ElibraryAuthorElibraryProduct).filter(
            ElibraryAuthorElibraryProduct.lnkElibraryAuthor==db_author.id).filter(
            ElibraryAuthorElibraryProduct.lnkElibraryProduct==db_product.id).first()

        if not ap:
            ap = ElibraryAuthorElibraryProduct()
            ap.ElibraryAuthor  = db_author
            db_product.ElibraryAuthors.append(ap)


        nowdate = datetime.now()
        if was_created:
            created_counter += 1
            db_product.createdAt = nowdate

        if was_updated:
            updated_counter += 1

        if was_created or was_updated:
            db_product.updatedAt = nowdate

        session.add(db_product)
        session.commit()

    if DEBUG:
        print('From', len(products), 'created:', created_counter, 'updated:', updated_counter)
        print()

session.close()



