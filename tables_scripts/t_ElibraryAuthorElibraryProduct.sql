use sciratedb
go

create table tElibraryAuthorElibraryProduct(
    id int identity(1,1) constraint PK_tElibraryAuthorElibraryProduct primary key,
    lnkElibraryAuthor int not null,
    lnkElibraryProduct int not null,
    FOREIGN KEY (lnkElibraryAuthor) REFERENCES tElibraryAuthors(id),
    FOREIGN KEY (lnkElibraryProduct) REFERENCES tElibraryProducts(id)
)

