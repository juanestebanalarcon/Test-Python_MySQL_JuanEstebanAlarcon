# 9) realice una consulta al archivo data.py, muestre todos los items, 
# ordenelos por nombre y dentro de cada item agregue el color correspondiente,
# en caso de que esté lo tenga. 
# El resultado del ordenando debe ser así, en la parte inicial los items 
# que no tienen color y en la parte final los que si tienen color
from data import Data as d 
items = d.items()
colors = d.colors()
InfoItems=[]
for l in items:
    for j in l:
        for clave in colors:
            if j.get("color") !="":
                if clave.get(j.get("color")):
                    colorAux=clave.get(j.get("color"))
                InfoItems.append({"code":j.get("code"),"name":j.get("name"),"color":colorAux.get("ColorName")})
            else:
                InfoItems.append({"code":j.get("code"),"name":j.get("name"),"color":""})
ordered_items=sorted(InfoItems, key=lambda x:x["name"])
