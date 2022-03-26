import requests
import io
import gzip
import csv
import pandas as pd
import pprint as pp

url = "link"header = {'Content-Type': 'application/json',
'x-access-token': 'chave'
}

r = requests.get(url, headers=header)
l = pd.read_json(r.content)
pp.pprint(l)

# -------------------------------------------------------------------------
frame = "output.csv"
with open(frame, "w") as file:
    csv_file = csv.writer(file, lineterminator='\n')
    csv_file.writerow(["agendamento_id","data","horario","paciente_id","procedimento_id","status_id",
                      "local_id","profissional_id","unidade_id","nome_fantasia"])
    for item in l["content"]:
        csv_file.writerow([item['agendamento_id'],item['data'],item['horario'],item['paciente_id'],
                           item['procedimento_id'],item['status_id'],item['local_id'],item['profissional_id'],
                           item['unidade_id'],item['nome_fantasia']])