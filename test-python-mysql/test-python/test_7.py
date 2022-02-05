

# 7) realice una consulta al archivo data.py, muestre los items que no tienen colores 
# y ordenelos por nombre
from data import Data as d 
items = d.items()
items_nombre=sorted(items, key=lambda x:x['name'])
for i in items_nombre:
    for l in i:
        if l.get('color')=="":
            print(i,end="\n")
