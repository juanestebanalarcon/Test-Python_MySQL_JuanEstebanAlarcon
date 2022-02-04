# Generar scripts para las siguientes solicitudes

-------*Eliminar los datos de la tabla colors*-------
DELETE FROM colors;

-------*Agregar un campo llamado Description en la tabla items, que permita NULL, y un máximo de 200 caracteres*-------
alter table items add description varchar(200) null; 
