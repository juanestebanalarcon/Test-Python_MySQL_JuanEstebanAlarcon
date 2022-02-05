# Generar scripts que realicen las siguientes consultas

-------*Consultar los items de la compañia (utilizando INNER JOIN) #3*-------
select i.name,i.price,i.cost,co.name,c.name
from items as i 
inner join companies as c 
on i.companyId = c.id 
innter join colors as co 
on i.colorid = co.id;
-------*Mostrar los últimos 10 items en general*-------
SELECT * FROM (
SELECT * FROM items ORDER BY id DESC LIMIT 10)
ORDER BY id ASC;

-------*Mostrar los items que en el nombre terminen con la A*-------
select* from items where name like '%a';

-------*Mostrar los items que tengan relacionado el color Rojo*-------
select* from items where colorid =2;
