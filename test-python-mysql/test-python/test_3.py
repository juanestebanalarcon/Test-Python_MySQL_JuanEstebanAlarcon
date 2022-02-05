
# 3) ordenar los terceros que se tienen en el archivo data.py 
# por nombre, para obtener el nombre correcto se debe tener en 
# cuenta la siguiente validación:
#  si el tercero tiene un tradename != '' entonces se muestra este valor, 
# en caso contrario se debe obtener concatenando los siguientes 
# campos: (firstname, lastname, maidenname) en el orden dado
from data import Data as d 
terceros =d.thirds()
ordernados_identificacionNumber = sorted(terceros,key=lambda x: x['identificationNumber'])
for _ in ordernados_identificacionNumber:
    for a in _.items():
        if a["tradename"] !="":
            print(a["tradename"]+":" +a['identificationNumber'])
        else:
             print(f"{a['firstname']} {a['lastname']} {a['maidenname']}: {a['identificationNumber']}")
   