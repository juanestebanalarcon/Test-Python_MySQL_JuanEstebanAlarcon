# Generar scripts que realicen las siguientes eliminaciones

-------*Eliminar los items de la compañía #1*-------
delete from items where companyId=1;

-------*Eliminar los items que tengan el costo menor a 10.000*-------
delete from items where cost <10000;
