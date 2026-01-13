PRAGMA foreign_keys = ON;

create table tipos(
    id int primary key,
    nombre text
);

create table items(
    id int primary key,
    tipoid int,
    valor text,
    cantidad int,
    foreign key(tipoid) references tipos(id)
);