import urllib.request as req
import json
src="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=35aa3c53-28fb-423c-91b6-2c22432d0d70"
with req.urlopen(src) as response:
    data=json.load(response)  #這邊就不行.decode("utf-8")
clist=data["result"]["results"]
with open("open.txt", "w",encoding="utf-8") as file:
    for company in clist:
        file.write(company["Location"]+"  "+company["Address"]+"  "+company["IsCharge"]+"\n")
