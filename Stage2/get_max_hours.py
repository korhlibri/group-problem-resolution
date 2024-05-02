import json
import csv
import pandas as pd
import os
from pathlib import Path
from pprint import pprint, pp
from get_teachers import get_teachers


mod_path = Path(__file__).parent


csv = (mod_path / "csvs" / "Profesores.csv").resolve()

def get_max_hours():
    
    teachers = get_teachers()
    
    hours_per_teacher = {}
    
    #print the days and hours of each teacher
    for teacher in teachers:
        
        hours_per_teacher[teacher] = 0
        
        for schedule in teachers[teacher]:
            
            for day in teachers[teacher][schedule]:
                
                hours_per_teacher[teacher] += sum([int(i[1]) - int(i[0]) for i in teachers[teacher][schedule]])
        
        
    return hours_per_teacher

