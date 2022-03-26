import requests
import csv
import pandas as pd
import pprint as pp

#Puxando relatório de ocupação das agendas do dia atual
url = ""
header = {'Content-Type': 'application/json',

'x-access-token': ''

}

r = requests.post(url,data=header)
l = pd.read_json(r.content)
pp.pprint(l)

# -------------------------------------------------------------------------
frame = "ocupacao.csv"
with open(frame, "w") as file:
    csv_file = csv.writer(file, lineterminator='\n')
    csv_file.writerow(["Bloqueados"])
#     for item in l['data']:
#         csv_file.writerow(item[0])