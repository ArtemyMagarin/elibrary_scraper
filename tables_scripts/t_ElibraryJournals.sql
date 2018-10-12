use sciratedb
go

create table tElibraryJournals (
    id int identity(1,1) constraint PK_tElibraryJournals primary key,
    eLibraryJournalId int NOT NULL,
    fname nvarchar(512) NOT NULL,
    impactFactor float(10),
    isVak int,
    issn nvarchar(255),
    lnkJournal int,
    FOREIGN KEY (lnkJournal) REFERENCES tJournals(id)
)