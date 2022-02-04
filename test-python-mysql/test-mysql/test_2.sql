# Generar scripts que realicen las siguientes modificaciones

-------*Colocarle el Precio a los items que lo tengan en NULL, tomando como referencia el costo más 10.000*-------
select* from items where price=null and cost>10000;

-------*Incrementar el precio de los items un 10%*-------
update items set price=price*0.1+price;

-------*Anteponer la palabra Nuevo a los items que comiencen con C en el nombre*-------
update items set name='Nuevo '+name where name like 'C%'; 
