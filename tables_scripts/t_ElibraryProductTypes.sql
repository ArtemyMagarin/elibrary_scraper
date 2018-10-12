use sciratedb
go

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
