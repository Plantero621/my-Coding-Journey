select * from filiale;
insert into filiale (name, ort, plaetze) VALUES ('Basiliea','Basel',87);
select * from filiale;

select * from pizza;
insert into pizza (name,preis) VAlues ('Pizza grande',9.8);

select * from zutat where bezeichnung = 'Origano';
Update zutat set soll_bestand='800' where bezeichnung='Origano';
select * from zutat where bezeichnung = 'Origano';

select * from pizza;
Update pizza set preis = preis+0.5 where preis > 7;
Update pizza set preis = preis+0.3 where preis < 7;
select * from pizza;

select * from umsatz where datum_verkauf<'2007-07-01';
delete from umsatz where datum_verkauf<'2007-07-01';
select * from umsatz where datum_verkauf<'2007-07-01';

delete from umsatz where idfiliale='3';
delete from pizzaiolo where idfiliale='3';
delete from filiale where idfiliale='3';

select * from filiale;


Load data infile 'land_daten.xyz' 
into table gesprochen
Fields Terminated by '  '
enclosed by '"'
lines Terminated by '\n'
ignore 1 rows;

select abtnr as Abbteilung, abtname as name from abteilg;
select Concat(pname,' ',pvname) as 'Nachname und Vorname' from persdat;
select Concat(pname,' ',pvname) As Name,abtnr As 'arbeitet in Abteilung' from persdat;
select pname,pvname from persdat where pname like 'me%';
select pname,pvname from persdat where pname like '%er';
select pname,pvname from persdat where pname like '%y%';




select * from pizzaiolo,filiale where idfiliale = 1;