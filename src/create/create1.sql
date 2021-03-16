create table PLACE(
name varchar not null,
street varchar not null,
city varchar not null,
state varchar not null,
zip varchar not NULL,
PRIMARY KEY (street, city, state, zip)
);