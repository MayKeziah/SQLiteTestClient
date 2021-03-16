create table PROJECT(
location varchar not null,
eventType varchar not null,
managerFname varchar not null,
managerLname varchar not null,
EDate date not null,
PRIMARY KEY (managerFname, managerLname, EDate),
FOREIGN KEY (location) REFERENCES PLACE (name),
FOREIGN KEY (managerFname, managerLname) REFERENCES PERSON (Fname, Lname)
);