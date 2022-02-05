# 10) realice una consulta al archivo data.py, muestre todos los terceros, reduzca la 
# información y solo muestre el nombre y la identificación, 
# ordenelos por identificación
# campos: (firstname, lastname, maidenname)
from data import Data as d 
terceros =d.thirds()
ordernados_identificacionNumber = sorted(terceros,key=lambda x: x['identificationNumber'])
for _ in ordernados_identificacionNumber:
    for a in _.items():
        if a["tradename"] !="":
            print(a["tradename"]+":" +a['identificationNumber'])
        else:
             print(f"{a['firstname']} {a['lastname']} {a['maidenname']}: {a['identificationNumber']}")
   