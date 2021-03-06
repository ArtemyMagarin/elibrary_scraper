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

