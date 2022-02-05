# 8) realice una consulta al archivo data.py, muestre los items que si tienen colores, 
# ordenelos por nombre y dentro de cada item agregue el color correspondiente
from data import Data as d 
items = d.items()
colors = d.colors()
InfoItems=[]
for l in items:
    for j in l:
        for clave in colors:
            if clave.get(j.get("color")):
                colorAux=clave.get(j.get("color"))
                if j.get("color") !="":
                    InfoItems.append({"code":j.get("code"),"name":j.get("name"),"color":colorAux.get("ColorName")})
                else:
                    continue 
orderedItemsByName=sorted(InfoItems,key=lambda j:j["name"])
for a in orderedItemsByName:
    for b in a:
        print(b,end="\n")
