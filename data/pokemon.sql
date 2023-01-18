drop table if exists pokemon_info;
create table pokemon_info
(
    idx    serial primary key,
    id     int,
    href   varchar(100),
    name   varchar(100),
    detail varchar(100),
    type1  varchar(100),
    type2  varchar(100),
    gen    varchar(10)
);

drop table if exists pokemon_attr;
create table pokemon_attr
(
    id              int,
    detail          varchar(100),
    hp              int,
    attack          int,
    defense         int,
    special_attack  int,
    special_defense int,
    speed           int
);
