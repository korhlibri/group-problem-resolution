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


schedule_block = {'Lunes': [False] * 25 ,
                  'Martes': [False] * 25 ,
                  'Miercoles': [False] * 25 ,
                  'Jueves': [False] * 25 ,
                  'Viernes': [False] * 25}

# print(schedule_block)


def get_horario(teacher, horas):
    original = horas
    if horas > teachers_max[teacher]:
        return {}
    days = list(teachers[teacher].keys())
    copy_scheudle = {}
    for day in days:
        copy_scheudle[day] = []
    horario = {}
    n = 0
    while horas != 0:
        # print('me cicle')
        # print(horas)
        # print(original)
        # print(teacher)
        if n == 0 and len(days) != 0:
            m = random.randint(0, len(days) - 1)
            day = days.pop(m)
            period = random.randint(0, len(teachers[teacher][day]) - 1)
            if period not in copy_scheudle[day]:
                copy_scheudle[day].append(period)
                inicio = random.randint(int(teachers[teacher][day][period][0]), int(teachers[teacher][day][period][1]) - 1)
                horario[day] = [[inicio, inicio + 1]]
                horas -= 1
        else:
            if len(days) == len(list(teachers[teacher].keys())):
                n = random.randint(0,5)
                continue
            else:
                day = random.choice(list(horario.keys()))
                periodo = random.randint(0, len(horario[day]) - 1)
                if n < 4:
                    if horario[day][periodo][0] - 1 >= 7:
                        horario[day][periodo] = [horario[day][periodo][0] - 1, horario[day][periodo][1]]
                        horas -= 1
                else:
                    if horario[day][periodo][1] + 1 <= 20:
                        horario[day][periodo] = [horario[day][periodo][0], horario[day][periodo][1] + 1]
                        horas -= 1 
        n = random.randint(0,5)
                
            
            #day = random.choice(list(horario.keys()))
    return horario
            
            
            
    
def get_cromosoma():    
    general = {}
    for semester in range(1,3):
        period = period_even
        if semester == 1: period = period_odd
        materias = []
        for periodo in range(1, 4):
            materias += period[str(periodo)]
        materias = list(set(materias))
        materias_a = {}
        for materia in materias:
            cont = 0
            periodos = []
            for i in range(1,4):
                if materia in period[str(i)]: 
                    cont +=1
                    periodos.append(str(i))
            if materia[-1] == 'B':
                valid = False
                while not valid:
                    profes = {}
                    temp = {}
                    temp2 = {}
                    schedule = {'Lunes': [False] * 25 ,
                                'Martes': [False] * 25 ,
                                'Miércoles': [False] * 25 ,
                                'Jueves': [False] * 25 ,
                                'Viernes': [False] * 25}
                    for modulo in hours[materia].keys():
                        teacher = random.choice(professors_for_course[materia][modulo])
                        hour = hours[materia][modulo]
                        if teacher in temp:
                            temp[teacher] += int(hour)
                        else:
                            temp[teacher] = int(hour)
                            
                        if teacher in temp2:
                            temp2[teacher].append(modulo)
                        else:
                            temp2[teacher] = [modulo]
                    valid = True
                    for i in temp.keys():
                        temp[i] = temp[i] / cont
                        if float(temp[i]) < 5 * cont or float(temp[i]) % 1 != 0:
                            valid = False
                    if not valid: continue
                    for i in temp2.keys():
                        profe = {
                            "Modulos": temp2[i],
                            "Periodos": periodos,
                            #"Horas": int(temp[i] * cont)
                            "Horas_semana": round(temp[i] / 5),
                            "Horas_Totales": int(temp[i] * cont)
                        }
                        profe["Horarios"] = get_horario(i, round(temp[i] / 5))
                        
                        for key in profe["Horarios"].keys():
                            for lista in profe["Horarios"][key]:
                                for value in range(lista[0], lista[1]):
                                    if schedule[key][value] == True:
                                        valid = False
                                    else:
                                        schedule[key][value] = True
                        profes[i] = profe
                    if not valid: continue
                materias_a[materia] = profes
                print (materias)
            else:
                groups = groups_even
                if semester == 1: groups = groups_odd
                for group in range(groups[materia]):
                    profes = {}
                    temp = {}
                    temp2 = {}
                    teacher = random.choice(professors_for_course[materia]['1'])
                    hour = hours[materia]['1']
                    if teacher in temp:
                        temp[teacher] += int(hour)
                    else:
                        temp[teacher] = int(hour)
                        
                    if teacher in temp2:
                        temp2[teacher].append('1')
                    else:
                        temp2[teacher] = ['1']
                    for i in temp2.keys():
                        temp[i] = temp[i] / cont
                        profe = {
                            "Modulos": temp2[i],
                            "Periodos": periodos,
                            #"Horas": int(temp[i] * cont)
                            "Horas_semana": round(temp[i] / 5),
                            "Horas_Totales": int(temp[i] * cont)
                        }
                        profe["Horarios"] = get_horario(i, round(temp[i] / 5))
                    
                    
                        
                        profes[i] = profe
                    print(materia)
                    materias_a[materia + "-" + str(group)] = profes            
        general[semester] = materias_a
    return general
                    
                    
            
           
        
            
        
        
get_cromosoma()


# # Generar población aleatoria
# for _ in range(n_poblacion):
#     horarios = {}
#     for materia, clases in Materias.items():
#         horarios_materia = {}
#         for modulo, profesores in clases.items():
#             profesor = random.choice(profesores)
#             horario_profesor = random.choice(Periodo[materia])
#             horas_semana = Horas[materia][str(horario_profesor)] // len(profes[profesor])  
#             horario = {}
#             for dia, rangos_disponibles in profes[profesor].items():
#                 rango_disponible = random.choice(rangos_disponibles)
#                 hora_inicial, hora_final = rango_disponible
#                 horas_necesarias = min(horas_semana, hora_final - hora_inicial)
#                 hora_inicio_clase = random.randint(hora_inicial, hora_final - 2)  
#                 duracion_clase = random.choice([2, 4])
#                 hora_final_clase = hora_inicio_clase + duracion_clase
#                 while hora_final_clase not in range(hora_inicio_clase + 2, hora_final + 1) or hora_final_clase - hora_inicio_clase != duracion_clase:
#                     hora_inicio_clase = random.randint(hora_inicial, hora_final - 2)
#                     hora_final_clase = hora_inicio_clase + duracion_clase
#                 horario[dia] = {"Hora Inicial": hora_inicio_clase, "Hora Final": hora_final_clase}
#             horarios_materia[modulo] = {"Profesor": profesor, "Horario": horario}
#         horarios[materia] = horarios_materia
#     poblacion.append(horarios)

# # Imprimir la población generada
# for idx, individuo in enumerate(poblacion, 1):
#     print()
#     print(f"Individuo {idx}:")
#     for materia, modulos in individuo.items():
#         print(f"Materia: {materia}")
#         for modulo, detalles in modulos.items():
#             print(f"Módulo: {modulo}")
#             print(f"Profesor: {detalles['Profesor']}")
#             for dia, horas in detalles['Horario'].items():
#                 print(f"{dia}: {horas['Hora Inicial']} - {horas['Hora Final']}")
