
# 5) ordenar los terceros que se tienen en el archivo data.py por nombre y 
# agregar dentro de cada tercero la compañia a la que pertenece
from data import Data as d 
terceros =d.thirds()
companies = d.get_companies()
InfoCompanies = {}
InfoBranches=[]
InfoTerceros=[]
branch=d.get_branch()
for index in companies:
    for k in index:
        for i in k.get("branches"):
            for llave in branch:
                    if llave.get(i):
                       InfoBranches.append({"name":llave.get("name"),"address":i.get("address")})
                    else: 
                        continue 
        InfoCompanies.append({"name":k.get("name"),"nit":k.get("nit"),"branches":InfoBranches})
for t in terceros:
    for s in t:
        for r in t.get("companyid"):
            for k in InfoCompanies:
                if k.get(r):
                    InfoTerceros.append({
    "billAddress1": s.get("billaddress1"),
    "cellPhone": s.get("cellphone"),
    "cityName": s.get("cityname"),
    "companyid": k.get(r),
    "email": s.get("email"),
    "firstname": s.get("firstname"),
    "identificationDv": s.get("identificationDv"),
    "identificationNumber": s.get("identificationNumber"),
    "lastname": s.get("lastname"),
    "maidenname": s.get("maidenname"), 
    "phone": s.get("phone"),
    "state": s.get("state"),
    "tradename":s.get("tradename")
})
ordered_by_name = sorted(InfoTerceros, key=lambda x: x["firstname"])

'''
"billAddress1": ,
"cellPhone": ,
"cityName": ,
"companyid": ,
"email": ,
"firstname": ,
"identificationDv": ,
"identificationNumber": ,
"lastname": ,
"maidenname": , 
"phone": "",
"state": ,
"tradename":
'''