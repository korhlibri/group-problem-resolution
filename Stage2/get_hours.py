import csv
import os
from pathlib import Path
import re
import numpy as np

def hoursCoursesTopics(nombre_archivo):
    hoursUDFTopic = {}
    mod_path = Path(__file__).parent
    blocks = [x for x in os.listdir(f"{mod_path}/csvs") if re.match(r'^.*-Profesores.csv$', x)]
    with open(f"{mod_path}/csvs/{nombre_archivo}","r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        next(reader)
        data= {}
        
        for row in reader:
            
            tema = row[0]
            horas = row[2]
            if tema != '':
                data[tema] = horas

    return data   


def hoursCoursesUDF():
    hoursUDF = {}
    data = {}
    mod_path = Path(__file__).parent
    blocks = [x for x in os.listdir(f"{mod_path}/csvs") if re.match(r'^.*-Profesores.csv$', x)]

    for file in blocks:
        clave = file.split("-")[0]
        if "B-" in file: 
            data = hoursCoursesTopics(file)
        else:
            data = {'1': 1} 
        hoursUDF[clave] = data

    with open(f"{mod_path}/csvs/UDF.csv","r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if "B" not in row["ï»¿Clave"]:
                #dic["1"] = row['Horas']
                hoursUDF[row["ï»¿Clave"]] = {'1': row['Horas']}


    return hoursUDF

