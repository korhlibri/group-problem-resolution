import random
import get_hours 
import get_teachers
import get_courses_period
import get_professors_for_course
import get_groups
import get_max_hours
import max_udf_teacher
import get_uf_semester
import json
import os


period_even = get_courses_period.get_courses_period(True)
period_odd = get_courses_period.get_courses_period(False)
professors_for_course = get_professors_for_course.get_professors_for_course()
hours = get_hours.hoursCoursesUDF()
teachers_avilivity = get_teachers.get_teachers()
groups_even = get_groups.get_period(False)
groups_odd = get_groups.get_period(True)
teachers_max = get_max_hours.get_max_hours()
udf_teacher = max_udf_teacher.max_udf_teacher()
uf_semester = get_uf_semester.get_uf_semester()


"""
scheduleCollisionProf :  108 YAAAAAAAAAAAAAAAAAAAA
scheduleCollisionStu :  104 YAAAAAAAAAAAAAAAAAAAA 1/2
breakTime :  100 YAAAAAAAAAAAAAAAAAAAA
noMoreTwoAndPairs :  105 YAAAAAAAAAAAAAAAAAAAA
availableProf :  106 YAAAAAAAAAAAAAAAAAAAAAA
definedSchedulesUFsAndProf :  106   YAAAAAAAAAAAAAAAAAAAA
minMaxProfTotal :  104 YAAAAAAAAAAAAAAAAAAAAAA
catProfModuleRel :  104
oddHours :  100 YAAAAAAAAAAAAAAAAAAAAAAAAAAa
noWednesday :  10 YAAAAAAAAAAAA
plantProfModuleRel :  15
minCatProf :  10
continousSchedule :  10 Yaaaaaaaaaaaa
onlyEight :  13 Yaaaaaaaaaaaaaaaaaaaaaaa
notAfterSeven :  13 YAaaaaaaaaaaaaaaaa
noCapacity: 11 Yaaaaaaaaaaaaaa
"""
gen = ['TC3008', 'G1', 'P2', 'M1', 'Victor Manon', '#Horas a la semana', 'Horario']
def calculate (cromosoma, restrictions, semester):
    teachers_udf = {}
    subjects_udf_hours = {}
    teachers = {}
    subjects = {}
    castigo = 0
    for gen in cromosoma:
        if gen[4] not in professors_for_course[gen[0]]:
            castigo += restrictions["noCapacity"] 
        if gen[4] in teachers:
            if (('Lunes' in gen[6].keys() and 'Jueves' in gen[6].keys()) or ('Martes' in gen[6].keys() and 'Viernes' in gen[6].keys())):
                pass
            else:
                castigo += restrictions["noMoreTwoAndPairs"] 
            if "Miercoles" in gen[6].keys():
                castigo += restrictions["noWednesday"] 
            for day in gen[6].keys():
                if day in teachers[gen[4]]:
                    if len(gen[6][day]) > 2:
                        castigo += restrictions["noMoreTwoAndPairs"]
                    previous_hour = gen[6][day][0] - 1
                    if (gen[6][day][0] % 2 != 0):
                        castigo += restrictions["oddHours"]
                    for hour in gen[6][day]:
                        if previous_hour != hour - 1:
                            castigo += restrictions["continousSchedule"]
                        previous_hour = hour
                        if gen[4] in teachers_udf:
                            teachers_udf[gen[4]] += 5
                        else:
                            teachers_udf[gen[4]] = 5
                        if gen[0] in subjects:
                            if gen[1] in subjects[gen[0]]:
                                if gen[2] in subjects[gen[0]][gen[1]]:
                                    if hour in subjects[gen[0]][gen[1]][gen[2]]:
                                        castigo += restrictions["scheduleCollisionStu"]
                                    else:
                                        subjects[gen[0]][gen[1]][gen[2]].append(hour)
                                        subjects[gen[0]][gen[1]][gen[2]].sort()
                                else:
                                    subjects[gen[0]][gen[1]][gen[2]] = [hour]
                            else:
                                subjects[gen[0]][gen[1]] = {
                                    gen[2] : [hour]
                                }
                        else:
                            a = {gen[2] : [hour]}
                            subjects[gen[0]] = {
                                gen[1] : a
                            }

                        if hour == 13 or hour == 14:
                            castigo += restrictions["breakTime"]
                        if hour in teachers[gen[4]][day]:
                            castigo += restrictions["scheduleCollisionProf"]
                        else:    
                            teachers[gen[4]][day].append(hour)
                            teachers[gen[4]][day].sort()
                        
                        valid = False
                        if day in teachers_avilivity[gen[4]]:
                            for hour_range in teachers_avilivity[gen[4]][day]:
                                if int(hour_range[0]) <= hour or hour < int(hour_range[1]):
                                    valid = True
                            if not valid:
                                castigo += restrictions["availableProf"]
                        else:
                            castigo += restrictions["availableProf"]
                else:
                    teachers[gen[4]][day] = gen[6][day]
        else:
            teachers[gen[4]] = gen[6]
        
        if gen[0] in subjects_udf_hours:
            if gen[1] in subjects_udf_hours[gen[0]]:
                subjects_udf_hours[gen[0]][gen[1]] += (gen[5] *5)
            else:
                subjects_udf_hours[gen[0]][gen[1]] = (gen[5] *5)
        else:
            a = {
                gen[1] : (gen[5] *5)
            }
            subjects_udf_hours[gen[0]] = a
    
    for teacher in teachers.keys():
        for day in teachers[teacher].keys():
            if len(teachers[teacher][day]) > 8:
                castigo += restrictions["onlyEight"]
            
    max = 0
    for materia in subjects_udf_hours.keys():
        horas_totales = 0
        for h in hours[materia].values():
            horas_totales += int(h)
        for group in subjects_udf_hours[materia].keys():
            if subjects_udf_hours[materia][group] != horas_totales:
                castigo += restrictions["definedSchedulesUFsAndProf"]
    
    
    for teacher in teachers_udf.keys():
        if int(udf_teacher[teacher]) > int(teachers_udf[teacher] / 20):
            castigo += (restrictions["minMaxProfTotal"] * (int(udf_teacher[teacher]) - int (teachers_udf[teacher] / 20)))
    
        #print(castigo)
    return [castigo, cromosoma]