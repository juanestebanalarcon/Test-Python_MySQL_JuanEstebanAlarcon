
from data import Data as d 
# 1) consulte la información del archivo data.py
companies = d.get_companies()
branch = d.get_branches()
items = d.get_items()
colors = d.get_colors()
print("Información de las compañías \n")
diccInfo = {}
dictBranch={}
diccInfo["branches"] = []
for index in companies:
    for k in index.items():
        diccInfo["name"] =k.get("name")
        diccInfo["nit"]=k.get("nit")
        if len(k.get("branches"))>1:
            for i in k.get("branches"):
                for llave in branch:
                    if llave.get(i):
                        diccInfo["branches"].append({"name":llave.get("name"),"address":i.get("address")})
        
    
# cree un objeto que contenga las empresas y dentro 
# las sucursales que corresponden para cada empresa


