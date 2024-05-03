import json
import csv
import pandas as pd
import os
from pathlib import Path
from pprint import pprint, pp

mod_path = Path(__file__).parent


def get_uf_semester():
    
    
    csv = (mod_path / "csvs" / "UDF.csv").resolve()
    
    df = pd.read_csv(csv)
    
    ufs = {}
    
    #Make the df a json with the "Clave" column as the key and the "Semestre" column as the value 
    for index, row in df.iterrows():
        ufs[row["Clave"]] = row["Semestre"]
        
    return ufs 

