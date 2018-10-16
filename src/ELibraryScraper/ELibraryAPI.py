import requests
from bs4 import BeautifulSoup as bs


'''
    TODO:
        - Сохранять данные
            - Возможно стоит сделать связь с mssql
              и запускать скрипт по крону раз в день

            - в таком случае дописать модуль связи с бд
            - и модуль проверки: есть такой продукт в бд или нет
'''


class ELibraryAPI:
    def __init__(self, key):
        self.key = key
        self.org_id = '289'
        self.base_url = 'http://elibrary.ru/projects/API-NEB/API_NEB.aspx?ucode={key}&orgid={org_id}'.format(
            key=self.key,
            org_id=self.org_id)
            
        self.methods = {
            'GetItemId':       '011',
            'GetItem':         '012',
            'GetAuthorId':     '013',
            'GetAuthorIdExt' : '023',
            'GetAuthor2':      '024',           
        }
        
        self.product_types = {
            '1':    'журнал',
            '2':    'книга или сборник статей',
            '3':    'сборник трудов конференции',
            '4':    'статья в журнале',
            '5':    'препринт',
            '6':    'статья в сборнике трудов конференции',
            '7':    'статья в сборнике или глава в книге',
            '8':    'диссертация',
            '9':    'патент',
            '10':   'отчет',
            '11':   'авторское свидетельство',
            '12':   'стандарт',
            '13':   'архивный документ',
            '14':   'рукопись',
            '15':   'интернет сайт',
        }

        self.author_properties_names = {
            'numOfLibraryItems':    'Общее число публикаций на elibrary.ru',
            'numofItemsFull':       'Число публикаций в РИНЦ',
            'libraryCited':         'Суммарное число цитирований из публикаций на elibrary.ru',
            'citedRefs':            'Число цитирований публикаций автора в РИНЦ',
            'citingPubl':           'Число публикаций, процитировавших работы автора',
            'maxItemCited':         'Число ссылок на самую цитируемую публикацию',
            'publCited':            'Число публикаций автора, процитированных хотя бы один раз',
            'publCitedPrc':         'Число публикаций автора, процитированных хотя бы один раз (%)',
            'avgCited':             'Среднее число цитирований в расчете на одну публикацию',
            'numOfCoreItems':       'Число публикаций, входящих в ядро РИНЦ',
            'numOfCoreItemsPrc':    'Число публикаций, входящих в ядро РИНЦ (%)',
            'coreCited':            'Число цитирований из публикаций, входящих в ядро РИНЦ',
            'hirsch':               'Индекс Хирша по публикациям в РИНЦ',
            'hirschs':              'Индекс Хирша без учета самоцитирований',
            'hirscha':              'Индекс Хирша с учетом только статей в журналах',
            'hirschCore':           'Индекс Хирша по ядру РИНЦ',
            'hirschFull':           'Индекс Хирша по всем публикациям на elibrary.ru',
            'firstPublYear':        'Год первой публикации',
            'selfCited':            'Число самоцитирований',
            'selfCitedPrc':         'Число самоцитирований (%)',
            'coauthorCited':        'Число цитирований соавторами',
            'coauthorsNum':         'Число соавторов',
            'publForeign':          'Число публикаций в зарубежных журналах',
            'publRussian':          'Число публикаций в российских журналах',
            'publVAK':              'Число публикаций в российских журналах из перечня ВАК',
            'publTranslated':       'Число публикаций в российских переводных журналах',
            'publIF':               'Число публикаций в журналах с ненулевым импакт-фактором',
            'citForeign':           'Число цитирований из зарубежных журналов',
            'citRussian':           'Число цитирований из российских журналов',
            'citVAK':               'Число цитирований из российских журналов из перечня ВАК',
            'citTranslated':        'Число цитирований из российских переводных журналов',
            'citIF':                'Число цитирований из журналов с ненулевым импакт-фактором',
            'avgPublIF':            'Средневзвешенный импакт-фактор журналов, в которых были опубликованы статьи',
            'avgCitIF':             'Средневзвешенный импакт-фактор журналов, в которых были процитированы статьи',
            'publ5':                'Число публикаций за последние 5 лет',
            'citPubl5':             'Число цитирований статей автора, опубликованных за последние 5 лет',
            'cit5':                 'Число цитирований всех публикаций автора из статей, опубликованных за последние 5 лет',
        }
        
    def get_authors_id(self):
        url = '{base_url}&sid={method_code}'.format(
            base_url=self.base_url,
            method_code=self.methods['GetAuthorIdExt'])
            
        r = requests.get(url)
        soup = bs(r.text, "html.parser")
        authors_id = [author['id'] for author in soup.findAll('author')]
        return authors_id
        
        
    def get_products_list_by_author(self, author_id):
        url = '{base_url}&sid={method_code}&authorid={author_id}'.format(
            base_url=self.base_url,
            method_code=self.methods['GetItemId'],
            author_id=author_id)
            
        r = requests.get(url)
        soup = bs(r.text, "html.parser")
        products = [product['id'] for product in soup.findAll('item')]
        return products
        
    def get_product_by_id(self, product_id):
        url = '{base_url}&sid={method_code}&itemid={product_id}'.format(
            base_url=self.base_url,
            method_code=self.methods['GetItem'],
            product_id=product_id)
            
        r = requests.get(url)
        soup = bs(r.text, "html.parser")
        
        product = {}
        product['elibraryId'] = int(product_id)
        product['title'] = soup.item.title.text
        product['authorsDumbString'] = ', '.join([name.strip() for name in soup.item.authors.text.replace('и др.', '').split(',')])
        product['lnkElibraryProductType'] = int(soup.item['genreid'])
        # product['type'] = self.product_types[str(product['lnkElibraryProductType'])]
        # product['link'] = 'http://elibrary.ru/item.asp?id='+product_id
        product['ref'] =  soup.item.ref.text
        product['year'] =  soup.item.year.text

        if (soup.item.keywords):
            product['keywords'] = ', '.join([ kw.text for kw in soup.item.keywords ])

        if (soup.item.pages):
            product['pages'] = soup.item.pages.text

        # если статья в журнале
        if (product['lnkElibraryProductType'] == 4):
            product['number'] = soup.item.number.text if soup.item.number else ""
            product['volume'] = soup.item.volume.text if soup.item.volume else ""
            product['journal'] = {
                'id': soup.item.journal['id'],
                'name': soup.item.journal.text,
                'issn': soup.item.journal['issn'],
                'impactFactor': float(soup.item.journal['impactfactor'].replace(',', '.')) if len(soup.item.journal['impactfactor']) else None,
                'isVak': (soup.item.journal['vak'] == 1)
            }

        # если патент
        if (product['lnkElibraryProductType'] == 9):
            product['code'] = soup.item.code.text
            product['date'] = soup.item.date.text

        return product
        
    def get_author_info(self, author_id):
        url = '{base_url}&sid={method_code}&authorid={author_id}'.format(
            base_url=self.base_url,
            method_code=self.methods['GetAuthor2'],
            author_id=author_id)
        
        r = requests.get(url)
        soup = bs(r.text, "html.parser")
        
        author_info = {}
        
        for prop in self.author_properties_names:
            author_info[prop] = soup.author[prop.lower()]
        
        author_info['elibraryAuthorId'] = author_id
        author_info['lastName']         = soup.author.lastname.text
        author_info['firstName']        = soup.author.firstname.text
        author_info['secondName']       = soup.author.secondname.text
        author_info['city']             = soup.author.city.text
        
        
        return author_info
        
        
        
        
