
from data import Data as d 
# 1) consulte la información del archivo data.py
companies = d.get_companies()
branch = d.get_branches()
items = d.get_items()
colors = d.get_colors()
print("Información de las compañías \n")
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
for i in InfoItems:
    print(i,end="\n")
for e in InfoCompanies:
    print(e,end="\n")
class Empresas:
   def __init__(self,name:str,nit:str,branches:list):
       self.name = name
       self.nit = nit 
       self.branches= branches
       def __str__(self):
        return f"Nombre empresa: {self.name}  NIT {self.nit} Branches {self.branches}"
               
InformacionEmpresas=Empresas()                        
        
    
# cree un objeto que contenga las empresas y dentro 
# las sucursales que corresponden para cada empresa


