import pandas as pd
from pathlib import Path
from get_groups import get_period


def dict_prof_availability(df):
    schedule = {}
    
    for index, row in df.iterrows():
        #print(row['Nombre'], row['Horario'])
        if row['Horario'] != 'Flexible':
            schedule[row['Nombre']] = 'Catedra'
        else:
            schedule[row['Nombre']] = 'Flexible'
            
        
    return schedule


def get_profs_availability():
    mod_path = Path(__file__).parent
    df = pd.read_csv(f"{mod_path}/csvs/Profesores.csv")
    
    
    return dict_prof_availability(df)


get_profs_availability()