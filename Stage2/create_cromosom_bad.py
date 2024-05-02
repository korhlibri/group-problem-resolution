import random
import get_hours 
import get_teachers
import get_courses_period
import get_professors_for_course
import get_groups
import json
import os

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
save_dict_as_json(groups_odd, os.path.join(directory, 'groups_odd.json'))


schedule_block = {'Lunes': [False] * 25 ,
                  'Martes': [False] * 25 ,
                  'Miercoles': [False] * 25 ,
                  'Jueves': [False] * 25 ,
                  'Viernes': [False] * 25}

print(schedule_block)

def get_cromosoma():
    general = {}
    for semester in range(1,3):
        period = period_even
        if semester == 1: period = period_odd
        periods = {}
        for periodo in range(1, 4):
            materias = {}
            for materia in period[str(periodo)]:
                if materia[-1] == 'B':
                    modulos = {}
                    valid = False
                    cont = 0
                    for i in range(1,4):
                        if materia in period[str(i)]: cont +=1
                    while not valid:
                        modulos = {}
                        temp = {}
                        schedule_temp = schedule_block
                        for modulo in hours[materia].keys():
                            teacher = random.choice(professors_for_course[materia][modulo])
                            hour = hours[materia][modulo]
                            if teacher in temp:
                                temp[teacher] += hour
                            else:
                                temp[teacher] = hour
                            modulos[modulo] = {'profesor' : teacher,'horas': str(int(hour) / cont) }
                        valid = True
                        for i in temp.keys():
                            if float(temp[i]) < 5 * cont or float(temp[i]) % 1 != 0:
                                print(i, temp[i],  cont)
                                valid = False
                            if not valid: continue
                        
                        for modulo in hours[materia].keys():
                            hour =  float(modulos[modulo]['horas'])
                            print(hour)
                            teacher_hours = modulos[modulo]['horas']
                            schedule = {}
                            modulos[modulo]['horario'] = schedule
                            
                           
                    materias[materia] = modulos
                else:
                    modulos = {}
                    valid = False
                    cont = 0
                    modulos = {}
                    groups = groups_even
                    if semester == 1: groups = groups_odd
                    for modulo in range(1, int(groups[materia]) + 1):
                        teacher = random.choice(professors_for_course[materia]['1'])
                        hour = hours[materia]['1']
                        schedule = {}
                        modulos[str(modulo)] = {'profesor' : teacher,'horas': hour,'horario' : schedule}
                    materias[materia] = modulos
                periods[str(periodo)] = materias
            general[str(semester)] = periods
    save_dict_as_json(general, os.path.join(directory, 'general.json'))
# Llamar a la función
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
