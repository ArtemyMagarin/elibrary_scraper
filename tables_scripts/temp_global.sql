use sciratedb
go

create table tElibraryAuthorPropertyNames (
    id int identity(1,1) constraint PK_tElibraryAuthorPropertyNames primary key,
    fname nvarchar(512) NOT NULL,
    codename nvarchar(255) NOT NULL
)

insert into tElibraryAuthorPropertyNames (codename, fname) values
    ('numOfLibraryItems', 'Общее число публикаций на elibrary.ru'),
    ('numofItemsFull', 'Число публикаций в РИНЦ'),
    ('libraryCited', 'Суммарное число цитирований из публикаций на elibrary.ru'),
    ('citedRefs', 'Число цитирований публикаций автора в РИНЦ'),
    ('citingPubl', 'Число публикаций, процитировавших работы автора'),
    ('maxItemCited', 'Число ссылок на самую цитируемую публикацию'),
    ('publCited', 'Число публикаций автора, процитированных хотя бы один раз'),
    ('publCitedPrc', 'Число публикаций автора, процитированных хотя бы один раз (%)'),
    ('avgCited', 'Среднее число цитирований в расчете на одну публикацию'),
    ('numOfCoreItems', 'Число публикаций, входящих в ядро РИНЦ'),
    ('numOfCoreItemsPrc', 'Число публикаций, входящих в ядро РИНЦ (%)'),
    ('coreCited', 'Число цитирований из публикаций, входящих в ядро РИНЦ'),
    ('hirsch', 'Индекс Хирша по публикациям в РИНЦ'),
    ('hirschs', 'Индекс Хирша без учета самоцитирований'),
    ('hirscha', 'Индекс Хирша с учетом только статей в журналах'),
    ('hirschCore', 'Индекс Хирша по ядру РИНЦ'),
    ('hirschFull', 'Индекс Хирша по всем публикациям на elibrary.ru'),
    ('firstPublYear', 'Год первой публикации'),
    ('selfCited', 'Число самоцитирований'),
    ('selfCitedPrc', 'Число самоцитирований (%)'),
    ('coauthorCited', 'Число цитирований соавторами'),
    ('coauthorsNum', 'Число соавторов'),
    ('publForeign', 'Число публикаций в зарубежных журналах'),
    ('publRussian', 'Число публикаций в российских журналах'),
    ('publVAK', 'Число публикаций в российских журналах из перечня ВАК'),
    ('publTranslated', 'Число публикаций в российских переводных журналах'),
    ('publIF', 'Число публикаций в журналах с ненулевым импакт-фактором'),
    ('citForeign', 'Число цитирований из зарубежных журналов'),
    ('citRussian', 'Число цитирований из российских журналов'),
    ('citVAK', 'Число цитирований из российских журналов из перечня ВАК'),
    ('citTranslated', 'Число цитирований из российских переводных журналов'),
    ('citIF', 'Число цитирований из журналов с ненулевым импакт-фактором'),
    ('avgPublIF', 'Средневзвешенный импакт-фактор журналов, в которых были опубликованы статьи'),
    ('avgCitIF', 'Средневзвешенный импакт-фактор журналов, в которых были процитированы статьи'),
    ('publ5', 'Число публикаций за последние 5 лет'),
    ('citPubl5', 'Число цитирований статей автора, опубликованных за последние 5 лет'),
    ('cit5', 'Число цитирований всех публикаций автора из статей, опубликованных за последние 5 лет');

create table tElibraryJournals (
    id int identity(1,1) constraint PK_tElibraryJournals primary key,
    eLibraryJournalId int NOT NULL,
    fname nvarchar(512) NOT NULL,
    impactFactor float(10),
    isVak int,
    issn nvarchar(255),
    lnkJournal int,
    createdAt datetime,
    updatedAt datetime,
    FOREIGN KEY (lnkJournal) REFERENCES tJournals(id)
)

create table tElibraryProductTypes (
    id int identity(1,1) constraint PK_tElibraryProductTypes primary key,
    fname nvarchar(512) NOT NULL,
)

insert into tElibraryProductTypes (fname) values
    ('журнал'),
    ('книга или сборник статей'),
    ('сборник трудов конференции'),
    ('статья в журнале'),
    ('препринт'),
    ('статья в сборнике трудов конференции'),
    ('статья в сборнике или глава в книге'),
    ('диссертация'),
    ('патент'),
    ('отчет'),
    ('авторское свидетельство'),
    ('стандарт'),
    ('архивный документ'),
    ('рукопись'),
    ('интернет сайт')

        


create table tElibraryProducts(
    id int identity(1,1) constraint PK_tElibraryProducts primary key,
    elibraryId int not null,
    lnkElibraryProductType int not null,
    lnkElibraryJournal int,
    title nvarchar(2048),
    authorsDumbString nvarchar(2048),
    year int,
    ref nvarchar(2048),
    keywords nvarchar(2048),
    pages nvarchar(255),
    number nvarchar(127),
    volume nvarchar(127),
    code nvarchar(127),
    date nvarchar(127),
    
    createdAt datetime,
    updatedAt datetime,
    FOREIGN KEY (lnkElibraryProductType) REFERENCES tElibraryProductTypes(id),
    FOREIGN KEY (lnkElibraryJournal) REFERENCES tElibraryJournals(id)
)


create table tElibraryAuthors (
    id int identity(1,1) constraint PK_tElibraryAuthors primary key,
    elibraryAuthorId int NOT NULL,
    lnkPersonnel int,
    lastName nvarchar(255),
    firstName nvarchar(255),
    secondName nvarchar(255),
    city nvarchar(255),
    numOfLibraryItems int,
    numofItemsFull int,
    libraryCited int,
    citedRefs int,
    citingPubl int,
    maxItemCited int,
    publCited int,
    publCitedPrc float(5),
    avgCited float(5),
    numOfCoreItems int,
    numOfCoreItemsPrc float(5),
    coreCited int,
    hirsch int,
    hirschs int,
    hirscha int,
    hirschCore int,
    hirschFull int,
    firstPublYear int,
    selfCited int,
    selfCitedPrc float(5),
    coauthorCited  int,
    coauthorsNum int,
    publForeign int,
    publRussian int,
    publVAK int,
    publTranslated int,
    publIF int,
    citForeign int,
    citRussian int,
    citVAK int,
    citTranslated int,
    citIF int,
    avgPublIF float(5),
    avgCitIF float(5),
    publ5 int,
    citPubl5 int,
    cit5 int,
    createdAt datetime,
    updatedAt datetime,
    FOREIGN KEY (lnkPersonnel) REFERENCES tPersonnel(id)
)

create table tElibraryAuthorElibraryProduct(
    id int identity(1,1) constraint PK_tElibraryAuthorElibraryProduct primary key,
    lnkElibraryAuthor int not null,
    lnkElibraryProduct int not null,
    FOREIGN KEY (lnkElibraryAuthor) REFERENCES tElibraryAuthors(id),
    FOREIGN KEY (lnkElibraryProduct) REFERENCES tElibraryProducts(id)
)

-----------------------------------------------------------------