
from data import Data as d 
# 1) consulte la información del archivo data.py
companies = d.get_companies()
branch = d.get_branches()
items = d.get_items()
colors = d.get_colors()
print("Información de las compañías \n")
for key,value in companies.items():
    print(key["name"]+": "+value) 
    print(key["nit"]+": "+value)
    print(branch[key["branch"]].get("name") +" "+branch[key["branch"]].get("address"))
for llave,valor in items.items():
    print(llave["name"]+": "+valor)
    print(colors[llave["color"]]+": ")
    
# cree un objeto que contenga las empresas y dentro 
# las sucursales que corresponden para cada empresa


