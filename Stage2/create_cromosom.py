import random
import get_hours 
import get_teachers
import get_courses_period
import get_professors_for_course
import get_groups
import get_max_hours
import json
import os
from collections import defaultdict


def save_dict_as_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

period_even = get_courses_period.get_courses_period(True)
period_odd = get_courses_period.get_courses_period(False)
professors_for_course = get_professors_for_course.get_professors_for_course()
hours = get_hours.hoursCoursesUDF()
teachers = get_teachers.get_teachers()
groups_even = get_groups.get_period(False)
groups_odd = get_groups.get_period(True)
teachers_max = get_max_hours.get_max_hours()


# Directorio donde se guardarán los archivos JSON
directory = 'json'
if not os.path.exists(directory):
    os.makedirs(directory)

# Guardar cada diccionario como un archivo JSON
save_dict_as_json(period_even, os.path.join(directory, 'period_even.json'))
save_dict_as_json(period_odd, os.path.join(directory, 'period_odd.json'))
save_dict_as_json(professors_for_course, os.path.join(directory, 'professors_for_course.json'))
save_dict_as_json(hours, os.path.join(directory, 'hours.json'))
save_dict_as_json(teachers, os.path.join(directory, 'teachers.json'))
save_dict_as_json(teachers_max, os.path.join(directory, 'teachers_max.json'))
save_dict_as_json(groups_odd, os.path.join(directory, 'groups_odd.json'))

days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']

gen = ['TC3008', 'G1', 'P2', 'M1', 'Victor Manon', '#Horas a la semana', 'Horario']


def get_cromosoma(semester):
    
    
    groups = groups_even
    if semester: groups = groups_odd
    periods = period_even
    if semester: periods = period_odd
    
    if semester: groups_odd
    materias = list(groups.keys())
    n_gen = 0
    
    for materia in list(set(materias)):
        temp = 0
        group = groups[materia]
        cont = 0 
        for i in range(1,4):
            if materia in periods[str(i)]:
                cont += 1
        modulos = len(list(professors_for_course[materia].keys()))
        n_gen += group* cont* modulos
        
    
    
    
    cromosoma = []
    for _ in range(n_gen):
        gen = []
        materia = random.choice(list(set(materias)))
        gen.append(materia)
        group = random.randint(1, int(groups[materia]))
        gen.append(group)
        while True:
            p = random.randint(1,3)
            if materia in periods[str(p)]:
                gen.append(p) 
                break
        
        modulo = random.choice(list(professors_for_course[materia].keys()))
        gen.append(int(modulo)) 
        
        teacher = random.choice(list(professors_for_course[materia][modulo]))
        gen.append(teacher)
        
        hour = hours[materia][modulo]
        cont = 0 
        for i in range(1,4):
            if materia in periods[str(i)]:
                cont += 1
        hour = int(hour) / cont
        if (hour % 1 != 0):
            hour = int(hour + random.choice([-.5, 0.5]))
            if hour == 0:
                hour = 1
        hour = int(hour / 5)
        gen.append(hour)
        
        horario = {}
        while hour != 0:
            day = random.choice(days)
            new_hour = random.randint(7,20)
            if day in horario:
                if new_hour not in horario[day]:
                    horario[day].append(new_hour)
                    hour -= 1
            else:
                horario[day] = [new_hour]
                hour -= 1
        
        for day in horario.keys():
            horario[day].sort()
        gen.append(horario)
        cromosoma.append(gen)
        
    return cromosoma

cromosom = get_cromosoma(True)


