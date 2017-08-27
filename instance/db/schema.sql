drop table if exists teststeps;
drop table if exists stages;

    create table teststeps (
    id integer primary key autoincrement not null,
    url text not null,
    method text not null,
    detail text
);


    
    create table stages (
    id integer primary key autoincrement not null,
    parent integer not null,
    child integer not null,
    data text not null,
    detail text
);
INSERT INTO TESTSTEPS (URL,METHOD,DETAIL) VALUES ('https://restcountries.eu/rest/v2/name/london', 'GET', 'abk Basic Get 1');
INSERT INTO TESTSTEPS (URL,METHOD,DETAIL) VALUES ('https://restcountries.eu/rest/v2/name/paris', 'GET', 'abk Basic Get 2');
INSERT INTO STAGES (PARENT,CHILD,DATA,DETAIL) VALUES (0,1,'get country','abk about united');
INSERT INTO STAGES (PARENT,CHILD,DATA,DETAIL) VALUES (0,2,'get country','abk about india');
