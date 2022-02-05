
from data import Data as d 
companies = d.get_companies()
branch = d.get_branches()
items = d.get_items()
colors = d.get_colors()
print("Información de las compañías \n")
# 2) teniendo en cuenta el punto 1, cree una función que permita
# consultar las sucursales por su id, debe hacerse el mismo procedimiento
# que se realizó en el punto 1, pero, utilizando la función creada
def consultar_sucursales(id):
    InfoCompanies = {}
    InfoBranches=[]
    InfoItems=[]
    colorAux={}
    for index in companies:
        for k in index:
            for i in k.get("branches"):
                for llave in branch:
                    if llave.get(i):
                       InfoBranches.append({"name":llave.get("name"),"address":i.get("address")})
                    else: 
                        continue 
        InfoCompanies.append({"name":k.get("name"),"nit":k.get("nit"),"branches":InfoBranches})
    for l in items:
        for j in l:
            for clave in colors:
                if clave.get(j.get("color")):
                    colorAux=clave.get(j.get("color"))
                InfoItems.append({"code":j.get("code"),"name":j.get("name"),"color":colorAux.get("ColorName")})
    for e in InfoCompanies:
        for c in e:
            if c.get(id):
                print("Información hallada: \n")
                print(c.get(id))
            else:
                continue 

    dictInfo = {}
    dictInfo["Empresas"] = InfoCompanies
    dictInfo["Items"] = InfoItems
    
