import random
import get_hours 
import get_teachers
import get_courses_period
import get_professors_for_course
import get_groups
import get_max_hours
import json
import os


period_even = get_courses_period.get_courses_period(True)
period_odd = get_courses_period.get_courses_period(False)
professors_for_course = get_professors_for_course.get_professors_for_course()
hours = get_hours.hoursCoursesUDF()
teachers = get_teachers.get_teachers()
groups_even = get_groups.get_period(False)
groups_odd = get_groups.get_period(True)
teachers_max = get_max_hours.get_max_hours()

"""
scheduleCollisionProf :  108
scheduleCollisionStu :  104
breakTime :  100
noMoreTwoAndPairs :  105
availableProf :  106
definedSchedulesUFsAndProf :  106
minMaxProfTotal :  104
catProfModuleRel :  104
oddHours :  100
noWednesday :  10
plantProfModuleRel :  15
minCatProf :  10
continousSchedule :  10
onlyEight :  13
notAfterSeven :  13
"""
gen = ['TC3008', 'G1', 'P2', 'M1', 'Victor Manon', '#Horas a la semana', 'Horario']

def calculate (cromosoma, restrictions, semester):
    teachers = {}
    castigo = 0
    for gen in cromosoma:
        if gen[4] in teachers:
            for day in gen[6].keys():
                if day in teachers[gen[4]]:
                    for hour in gen[6][day]:
                        if hour in teachers[gen[4]][day]:
                            castigo += restrictions["scheduleCollisionProf"]
                        else:
                            teachers[gen[4]][day].append(hour)
                            teachers[gen[4]][day].sort()
                else:
                    teachers[gen[4]][day] = gen[6][day]
        else:
            teachers[gen[4]] = gen[6]
    
        #print(castigo)
    return [castigo, cromosoma]