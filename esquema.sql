drop table if exists entradas;
create table entradas (
    id integer auto_increment primary key,
    titulo string not null,
    text string not null
);