create table users (
    id serial primary key,
    username varchar(50) unique not null,
    email varchar(50) unique not null,
    password text not null
);