import numpy as np
from random import randint, choice

import get_hours 
import get_teachers
import get_courses_period
import get_professors_for_course
import get_groups
import get_max_hours

period_even = get_courses_period.get_courses_period(True)
period_odd = get_courses_period.get_courses_period(False)
professors_for_course = get_professors_for_course.get_professors_for_course()
hours = get_hours.hoursCoursesUDF()
teachers = get_teachers.get_teachers()
groups_even = get_groups.get_period(False)
groups_odd = get_groups.get_period(True)
teachers_max = get_max_hours.get_max_hours()

def mutation_operator(chromosome, semester):

    groups = groups_even
    if semester: groups = groups_odd
    periods = period_even
    if semester: periods = period_odd

    
    gen_i = randint(0,len(chromosome)-1)
    pick_gen_element = choice([1,2])
    gen = chromosome[gen_i]
    #print('ind: ',chromosome)
    #print('gen: ',gen)
    if pick_gen_element == 1:#Profesor de modulo
        #print(gen[3])
        options = list(professors_for_course[gen[0]][str(gen[3])])
        
        #options = list(professors_for_course['TC1001B'][str(gen[3])])
        #print(options)
        #print(gen)
        #m = randint(0,len(options)-1)
        m = choice(options)
        #print('m',m)
        gen[4] = m
        #print(gen)
        chromosome[gen_i] = gen
        return chromosome
    
    elif pick_gen_element == 2: #Horario
        days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
        #print('gen: ',gen)

        hour = int(gen[5])
        #print('h',hour)
        horario = {}
        while hour != 0:
            day = choice(days)
            new_hour = randint(7,20)
            if day in horario:
                if new_hour not in horario[day]:
                    horario[day].append(new_hour)
                    hour -= 1
            else:
                horario[day] = [new_hour]
                hour -= 1
        
        for day in horario.keys():
            horario[day].sort()

        gen[6] = horario
        #print(gen)
        chromosome[gen_i] = gen
        return chromosome

