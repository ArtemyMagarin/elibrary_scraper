
from utils import get_session
from models import ElibraryProduct, SciProduct

import re

#init DB session
session = get_session()

# getting all products from db
elibrary_products = session.query(ElibraryProduct).all()
sci_products = session.query(SciProduct).all()

for el_product in elibrary_products:

    for sci_product in sci_products:
        el_title_words = re.sub(r'\s', ' ', re.sub(r'\W', ' ', el_product.title.lower())).split(' ')
        sc_title_words = re.sub(r'\s', ' ', re.sub(r'\W', ' ', sci_product.title.lower())).split(' ')
        
        counter = 0
        for w in el_title_words:
            if w in sc_title_words:
                counter += 1

        if counter / len(el_title_words) > 0.7:
            print('match!', el_product.id, sci_product.id)
            print(el_product.title, sci_product.title)
            print()
session.close()



