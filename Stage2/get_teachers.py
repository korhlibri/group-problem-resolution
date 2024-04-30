import json
import csv
import pandas as pd
import os
from pathlib import Path
from pprint import pprint, pp

mod_path = Path(__file__).parent


csv = (mod_path / "csvs" / "Profesores.csv").resolve()


def normailize_schedule(schedule : str) -> None:
    
    days_sample = {
        "Lu": "Lunes",
        "Ma": "Martes",
        "Mi": "Miércoles",
        "Ju": "Jueves",
        "Vi": "Viernes"
    }
    
    hours = []
    days = []
        
    if schedule.find(">") != -1:
        
        splitted_schedule = schedule.split(' ')
        
        schedule_days = splitted_schedule[-2]
        
        current_days = [days_sample[schedule_days[i:i+2]] for i in range(0, len(schedule_days), 2)]
        
        for i in current_days:
            days.append(i)     
        
        for i in splitted_schedule:
            if i.isdigit():
                hours.append(i)
        hours.append(20)
        
        return hours, days
        
    elif schedule.find("preferencia") != -1:
        
        splitted_schedule = schedule.split(' ')
        
        schedule_days = splitted_schedule[-3]
        days.append(days_sample[schedule_days])
        
        for i in splitted_schedule:
            if i.isdigit():
                hours.append(i)
                
        return hours, days
    
    elif schedule == "Flexible":
        
        hours.append(7)
        hours.append(20)
        
        days.append("Lunes")
        days.append("Martes")
        days.append("Miércoles")
        days.append("Jueves")
        days.append("Viernes")
        
        return hours, days
    
    else:
        
        splitted_schedule = schedule.split(' ')
        
        schedule = schedule.split(' ')[-1]
        splitted_schedule.pop(-1)
        
        current_days = [days_sample[schedule[i:i+2]] for i in range(0, len(schedule), 2)]
                
        for i in current_days:
            days.append(i)
        
        #cicle through the splitted_schedule list and retrieve all the hours only
        for i in splitted_schedule:
            if i.isdigit():
                hours.append(i)
                
        return hours, days
    
def get_teachers(csv):
    
    print("Hola")
    
    teachers = {}

    df = pd.read_csv(csv)
    
    #Select the Nombre, Nomina and Horario columns from dataframe and print it
    df = df[['Nombre', 'Nómina', 'Horario']]
    
    #Replace NaN values with "Flexible"
    df['Horario'].fillna("Flexible", inplace = True)
    
    for index, row in df.iterrows():
        
        hours, days = normailize_schedule(row['Horario'])
        
        teachers[row['Nombre']] = {}
        
        for day in days:
            teachers[row['Nombre']][day] = hours
    
    return teachers



pp(get_teachers(csv))