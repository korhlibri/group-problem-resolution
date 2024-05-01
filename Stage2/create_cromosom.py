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



print("Archivos JSON guardados correctamente en la carpeta 'json'.")

period = get_courses_period.get_courses_period(True)
professors_for_course = get_professors_for_course.get_professors_for_course()
hours = get_hours.hoursCoursesUDF()
teachers = get_teachers.get_teachers()
groups = get_groups.get_period(False)


# Directorio donde se guardarán los archivos JSON
directory = 'json'
if not os.path.exists(directory):
    os.makedirs(directory)

# Guardar cada diccionario como un archivo JSON
save_dict_as_json(period, os.path.join(directory, 'period.json'))
save_dict_as_json(professors_for_course, os.path.join(directory, 'professors_for_course.json'))
save_dict_as_json(hours, os.path.join(directory, 'hours.json'))
save_dict_as_json(teachers, os.path.join(directory, 'teachers.json'))
save_dict_as_json(groups, os.path.join(directory, 'groups.json'))


n_poblacion = 2
poblacion = []

import random

def get_cromosoma():
    general = {}
    periods = {}
    for periodo in range(1, 4):
        materias = {}
        for materia in period[str(periodo)]:
            modulos = {}
            for modulo in hours[materia].keys():
                modulos[modulo] = random.choice(professors_for_course[materia][modulo])
            materias[materia] = modulos
        periods[str(periodo)] = materias
    print(periods)

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
