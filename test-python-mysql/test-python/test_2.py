
from data import Data as d 
companies = d.get_companies()
branch = d.get_branches()
items = d.get_items()
colors = d.get_colors()
print("Información de las compañías \n")
diccInfo = {}
dictBranch={}
# 2) teniendo en cuenta el punto 1, cree una función que permita
# consultar las sucursales por su id, debe hacerse el mismo procedimiento
# que se realizó en el punto 1, pero, utilizando la función creada
def consultar_sucursales(id):
    for index in companies:
     for k in index.items():
        diccInfo["name"] =k.get("name")
        diccInfo["nit"]=k.get("nit")
        if len(k.get("branches"))>1:
            for i in k.get("branches"):
                for llave in branch:
                    if llave.get(i):
                        diccInfo["branches"].append({"name":llave.get("name"),"address":i.get("address")})
    return diccInfo
