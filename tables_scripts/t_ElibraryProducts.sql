use sciratedb
go

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
    lnkSciProduct int,

    createdAt datetime,
    updatedAt datetime,
    FOREIGN KEY (lnkElibraryProductType) REFERENCES tElibraryProductTypes(id),
    FOREIGN KEY (lnkElibraryJournal) REFERENCES tElibraryJournals(id)
    FOREIGN KEY (lnkSciProduct) REFERENCES tSciProducts(id)
)

