drop table if exists skill;
create table skill
(
    id       int primary key,
    name     varchar(100),
    type     varchar(100),
    category varchar(100),
    pp       int,
    power    int,
    accuracy int,
    gen      varchar(10)
);