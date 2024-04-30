import csv
import os
from pathlib import Path
import re

def hoursCourses():
    hours = {}
    mod_path = Path(__file__).parent
    #blocks = [x for x in os.listdir(f"{mod_path}/csvs") if re.match(r'^.*-Profesores.csv$', x)]
    #print (blocks)

    #for _ in range(len(blocks)):
    with open(f"{mod_path}/csvs/UDF.csv","r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            hours[row['Nombre']] = row['Horas']

    for clave, valor in hours.items():
        print(clave, ": ", valor)



hoursCourses()