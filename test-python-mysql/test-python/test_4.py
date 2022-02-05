
# 4) ordenar los terceros que se tienen en el archivo data.py por identificationNumber
from data import Data as d 

terceros = d.thirds()
ordernados_identificacionNumber = sorted(terceros,key=lambda x: x['identificationNumber'])
 