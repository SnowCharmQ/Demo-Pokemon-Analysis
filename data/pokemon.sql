drop table if exists pokemon_info;
create table pokemon_info
(
    id            int primary key,
    english_name  varchar(100) unique,
    japanese_name varchar(100) unique,
    type1         varchar(100),
    type2         varchar(100),
    official_rom  varchar(100)
);

drop table if exists pokemon_attr;
create table pokemon_attr
(
    id              int primary key,
    hp              int,
    attack          int,
    defense         int,
    special_attack  int,
    special_defense int,
    speed           int
);


select * from pokemon_info;