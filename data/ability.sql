drop table if exists ability;
create table ability
(
    id          int primary key,
    name        varchar(100),
    description varchar(1000),
    gen         varchar(10)
);

select * from ability;