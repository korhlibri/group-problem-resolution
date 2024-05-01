import json
import csv
import pandas as pd
import os
from pathlib import Path
from pprint import pprint, pp

mod_path = Path(__file__).parent


csv_period_1 = (mod_path / "csvs" / "Agosto-Diciembre.csv").resolve()
csv_period_2 = (mod_path / "csvs" / "Febrero-Junio.csv").resolve()


def get_groups(csv : str) -> dict:
    
    groups = {}
    df = pd.read_csv(csv)
    
    #Cicle through the rows of the csv and assign the CLAVE column as a key for the dictionary and the # GPOs column as the value
    for index, row in df.iterrows():
        groups[row["CLAVE"]] = row["# GPOs"]
    
    return groups
        
def get_period(even : bool) -> dict:
    
    period = {}
    
    if even == True:
        period = get_groups(csv_period_1)
        
    elif even == False:
        period = get_groups(csv_period_2)
    
    else:
        print("Invalid argument")
        
    return period