import random
import get_hours 
import get_teachers
import get_courses_period
import get_professors_for_course

period = get_courses_period.get_courses_period(True)
professors_for_course = get_professors_for_course.get_professors_for_course()
hours = get_hours.hoursCoursesUDF()
teachers = get_teachers.get_teachers()

print(hours)

period = {'1': ['TC1003B', 'TC2037', 'TC2005B', 'TC3001B', 'TC3004B', 'TI3005B'], 
          '2': ['TC1002B', 'TC2037', 'TC2005B', 'TC3001B', 'TC3002B', 'TC3005B'], 
          '3': ['TC1030', 'TC2037', 'TC2006B', 'TC3001B', 'TC3003B', 'TC3005B']}

professors_for_course = {'TC1027': {'1': ['Juan Alvarado', 'Roberto Leyva', 'Mauricio Paletta', 'Jaime López', 'José Aguilera', 'Pedro Hernandez', 'Roberto Vera']}, 
                         'TC1028': {'1': ['Víctor Mañon', 'Juan Alvarado', 'Roberto Leyva', 'Mauricio Paletta', 'Yerly Flores', 'José Aguilera', 'Pedro Hernandez', 'Roberto Vera']}, 
                         'TC1029': {'1': ['Víctor Mañon', 'Juan Alvarado', 'Roberto Leyva', 'Mauricio Paletta', 'José Aguilera', 'Pedro Hernandez', 'Roberto Vera']}, 
                         'TC1030': {'1': ['Víctor Mañon', 'Mauricio Paletta']}, 
                         'TC1031': {'1': ['Víctor Mañon', 'Juan Alvarado', 'Roberto Leyva', 'Mauricio Paletta', 'José Aguilera']}, 
                         'TC1032': {'1': ['Yerly Flores', 'Jorge Rodríguez', 'Fernando Ruiz', 'Israel Tabarez']}, 
                         'TC1033': {'1': ['Víctor Mañon', 'Mauricio Paletta']}, 
                         'TC2037': {'1': ['Juan Alvarado', 'José Aguilera', 'Pedro Hernandez']}, 
                         'TC2038': {'1': ['Juan Alvarado', 'Mauricio Paletta', 'José Aguilera']}, 
                         'TI1015': {'1': ['Juan Alvarado', 'Roberto Leyva', 'José Aguilera', 'Luis Guadarrama', 'Pedro Hernandez', 'María Mirafuentes', 'Roberto Vera']}, 
                         'TC3005B': {'1': ['Juan Alvarado', 'Luis Guadarrama', 'María Mirafuentes'], '2': ['Víctor Mañón', 'Juan Alvarado', 'Roberto Leyva', 'José Aguilera', 'Pedro Hernandez'], '3': ['Víctor Mañón', 'Roberto Vera'], '4': ['Víctor Mañón', 'Mauricio Paletta', 'Pedro Hernandez'], '5': ['Juan Alvarado', 'Luis Guadarrama', 'María Mirafuentes'], '6': ['Juan Alvarado', 'Luis Guadarrama'], '7': ['Juan Alvarado', 'Luis Guadarrama']}, 
                         'TC2006B': {'1': ['Víctor Mañón', 'Juan Alvarado', 'Roberto Leyva', 'Yerly Flores'], '2': ['Víctor Mañón', 'Juan Alvarado', 'Roberto Leyva', 'Yerly Flores'], '3': ['Víctor Mañón', 'Juan Alvarado', 'Roberto Leyva', 'Yerly Flores']}, 
                         'TC1001B': {'1': ['Jorge Rodríguez'], '2': ['Mauricio Paletta'], '3': ['Víctor Mañón', 'Juan Alvarado', 'Roberto Leyva', 'Mauricio Paletta', 'Roberto Vera'], '4': ['Jorge Rodríguez'], '5': ['Roberto Leyva', 'Mauricio Paletta'], '6': ['Jorge Rodríguez', 'Octavio Silva'], '7': ['Jorge Rodríguez', 'Octavio Silva']}, 
                         'TC1002B': {'1': ['Jorge Rodríguez'], '2': ['Jorge Rodríguez'], '3': ['Jorge Rodríguez'], '4': ['Víctor Mañón', 'Juan Alvarado', 'Roberto Leyva', 'Mauricio Paletta'], '5': ['Jorge Rodríguez'], '6': ['Víctor Mañón', 'Mauricio Paletta'], '7': ['Jorge Rodríguez']}, 
                         'TC2005B': {'1': ['Juan Alvarado', 'Luis Guadarrama', 'María Mirafuentes'], '2': ['Víctor Mañón', 'Juan Alvarado', 'Roberto Leyva', 'Mauricio Paletta', 'José Aguilera', 'Luis Guadarrama', 'Pedro Hernandez'], '3': ['Juan Alvarado', 'Luis Guadarrama'], '4': ['Juan Alvarado', 'Luis Guadarrama'], '5': ['Víctor Mañón', 'Roberto Vera'], '6': ['Víctor Mañón', 'Juan Alvarado', 'Roberto Leyva', 'Mauricio Paletta', 'José Aguilera', 'Pedro Hernandez'], '7': ['Juan Alvarado', 'Mauricio Paletta', 'Luis Guadarrama', 'María Mirafuentes'], '8': ['Roberto Leyva']}, 
                         'TC3004B': {'1': ['Juan Alvarado', 'Luis Guadarrama'], '2': ['Juan Alvarado', 'Octavio Silva'], '3': ['Juan Alvarado', 'Luis Guadarrama', 'María Mirafuentes'], '4': ['Juan Alvarado', 'Luis Guadarrama', 'María Mirafuentes'], '5': ['Juan Alvarado', 'Luis Guadarrama', 'María Mirafuentes']}, 
                         'TC1004B': {'1': ['Yerly Flores', 'Jaime López', 'Israel Tabarez'], '2': ['Yerly Flores', 'Jaime López', 'Israel Tabarez'], '3': ['Yerly Flores', 'Jaime López', 'Israel Tabarez'], '4': ['Yerly Flores', 'Jaime López', 'Israel Tabarez'], '5': ['Yerly Flores', 'Jaime López', 'Israel Tabarez'], '6': ['Víctor Mañón', 'Juan Alvarado', 'Roberto Leyva', 'Mauricio Paletta', 'José Aguilera', 'Pedro Hernandez'], '7': ['Víctor Mañón', 'Juan Alvarado', 'Roberto Leyva', 'Mauricio Paletta', 'José Aguilera'], '8': ['José Aguilera', 'Pedro Hernandez', 'Israel Tabarez'], '9': ['Fernando Ruiz', 'Israel Tabarez']}, 
                         'TC3003B': {'1': ['Víctor Mañón', 'Juan Alvarado', 'Roberto Leyva', 'Mauricio Paletta', 'Yerly Flores'], '2': ['Víctor Mañón', 'Juan Alvarado', 'Roberto Leyva', 'Mauricio Paletta', 'Yerly Flores'], '3': ['Roberto Leyva'], '4': ['Víctor Mañón', 'Juan Alvarado', 'Roberto Leyva', 'Mauricio Paletta', 'Yerly Flores']}, 
                         'TC2008B': {'1': ['Roberto Leyva', 'Mauricio Paletta'], '2': ['Roberto Leyva', 'Mauricio Paletta'], '3': ['Pedro Hernandez', 'Ivan Olmos'], '4': ['Pedro Hernandez', 'Ivan Olmos'], '5': ['Pedro Hernandez', 'Ivan Olmos'], '6': ['Pedro Hernandez', 'Ivan Olmos'], '7': ['Israel Tabarez']}, 
                         'TC2007B': {'1': ['Víctor Mañón', 'Yerly Flores'], '2': ['Víctor Mañón', 'Yerly Flores'], '3': ['Víctor Mañón', 'Octavio Silva'], '4': ['Roberto Leyva'], '5': ['Juan Alvarado', 'Luis Guadarrama'], '6': ['Juan Alvarado', 'Luis Guadarrama']}, 
                         'TC3002B': {'1': ['Juan Alvarado', 'Roberto Leyva', 'Mauricio Paletta'], '2': ['Roberto Leyva', 'Mauricio Paletta'], '3': ['Mauricio Paletta', 'José Aguilera'], '4': ['Pedro Hernandez']}, 
                         'TI3005B': {'1': ['Juan Alvarado', 'Luis Guadarrama', 'María Mirafuentes'], '2': ['Juan Alvarado', 'Mauricio Paletta', 'José Aguilera', 'Luis Guadarrama', 'Pedro Hernandez', 'Roberto Vera'], '3': ['Roberto Leyva']}}

hours = {'TC3005B': {'1': '20', '2': '50', '3': '60', '4': '40', '5': '40', '6': '20', '7': '10'}, 
         'TC2006B': {'1': '20', '2': '30', '3': '30'}, 
         'TC1001B': {'1': '4', '2': '8', '3': '6', '4': '8', '5': '24', '6': '6', '7': '4'}, 
         'TC1002B': {'1': '2', '2': '2', '3': '6', '4': '24', '5': '16', '6': '8', '7': '2'}, 
         'TC2005B': {'1': '4', '2': '50', '3': '8', '4': '4', '5': '30', '6': '30', '7': '4', '8': '30'}, 
         'TC3004B': {'1': '12', '2': '24', '3': '24', '4': '30', '5': '30'}, 
         'TC1004B': {'1': '15', '2': '15', '3': '5', '4': '5', '5': '5', '6': '20', '7': '10', '8': '15', '9': '30'}, 
         'TC3003B': {'1': '10', '2': '16', '3': '34', '4': '60'}, 
         'TC2008B': {'1': '8', '2': '12', '3': '12', '4': '12', '5': '12', '6': '12', '7': '12'}, 
         'TC2007B': {'1': '15', '2': '20', '3': '25', '4': '50', '5': '30', '6': '20'}, 
         'TC3002B': {'1': '20', '2': '40', '3': '30', '4': '30'}, 
         'TI3005B': {'1': '30', '2': '30', '3': '60'}, 
         'TC1027': {'1': '20'}, 'TC1028': {'1': '40'}, 
         'TC1029': {'1': '60'}, 'TC1030': {'1': '20'}, 
         'TC1031': {'1': '60'}, 'TC1032': {'1': '20'}, 
         'TC1033': {'1': '20'}, 'TC2037': {'1': '60'}, 
         'TC2038': {'1': '60'}, 'TI1015': {'1': '20'}, 
         'TI3001C': {'1': '140'}, 
         'TI3002C': {'1': '260'}}

# print(period)
# print(professors_for_course)
# print(hours)
# print(teachers)


n_poblacion = 2
poblacion = []

def get_cromosoma():
    
    return {}

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
