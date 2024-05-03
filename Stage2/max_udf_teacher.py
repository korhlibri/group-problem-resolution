import json
import csv
import pandas as pd
import os
from pathlib import Path
from pprint import pprint, pp

mod_path = Path(__file__).parent


csv = (mod_path / "csvs" / "Profesores.csv").resolve()

def max_udf_teacher():
    
    df = pd.read_csv(csv)
    
    udf_by_teachers = {}

    for index, row in df.iterrows():
        
        if row["Nombre"] == "Yerly Flores":
            udf_by_teachers[row["Nombre"]] = 7.0
        else:
            udf_by_teachers[row["Nombre"]] = row["Máx UdC"]
                
        
    return udf_by_teachers

