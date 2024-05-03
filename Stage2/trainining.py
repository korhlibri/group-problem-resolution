import numpy as np
from random import randint, choice, choices

import os
import json

from create_cromosom import get_cromosoma
from restriccions_function import calculate
from restrictions import restrictionsGroups

#gen = ['TC3008', 'G1', 'P2', 'M1', 'Victor Manon', '#Horas a la semana', 'Horario']

directory = 'json'
if not os.path.exists(directory):
    os.makedirs(directory)

def save_dict_as_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    

def population_initialization(n_population):
    population = []
    for _ in range(n_population):
        population.append(get_cromosoma(True))
    restrictions_dict = restrictionsGroups()
    sorted_population = []
    for i in population:
        sorted_population.append(calculate(i,restrictions_dict, True))
    sorted_population.sort()
    return sorted_population, population

import uniform_crossover
import multi_point_crossover
import mutation_operator

def evolution(population, epochs):
    ep = 0
    while ep < epochs:
        temp_pop = []
        len_pop = len(population)
        while len(temp_pop) != len_pop:
            genetic_op = 2#choices(population=[0,1,2], weights=[1, 49, 50]) #seleccion de operadores geneticos temporal, se queda fija para propositos de prueba
            selected_individuals = choices(population=population, k=2)#esta es una seleccion de individuos temporal, regresa 2 individuos aleatorios
            #print(selected_individuals)
            if genetic_op == 0:#crossover uniforme
                temp_new = uniform_crossover.uniform_crossover(selected_individuals[0], selected_individuals[1])
                temp_pop.append(temp_new[0])
                temp_pop.append(temp_new[1])
            elif genetic_op == 1:#crossover point
                points = choices([1, 2, 3, 4, 5], weights=[20, 20, 5, 5, 5])
                temp_new = multi_point_crossover.multiCross(points, selected_individuals[0], selected_individuals[1])
                temp_pop.append(temp_new[0])
                temp_pop.append(temp_new[1])
            elif genetic_op == 2:#mutation
                temp_new = (mutation_operator.mutation_operator(selected_individuals[0], True), mutation_operator.mutation_operator(selected_individuals[1], True))
                temp_pop.append(temp_new[0])
                temp_pop.append(temp_new[1])
        ep += 1
        population = temp_pop
        print(ep)
    return population

population = []

n_population = 100

_,population = population_initialization(n_population)
population = evolution(population, 1000)

#print(population)