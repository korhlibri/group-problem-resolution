import numpy as np
from random import randint, choice, choices


import os
import json

from create_cromosom import get_cromosoma
from restriccions_function import calculate
from restrictions import restrictionsGroups

import uniform_crossover

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

def evolution(population, epochs):
    ep = 0
    while ep < epochs:
        temp_pop = []
        len_pop = len(population)
        while len(temp_pop) != len_pop:
            genetic_op = 0#choices(population=[0,1,2], weights=[1, 49, 50]) #seleccion de operadores geneticos temporal, se queda fija para propositos de prueba
            selected_individuals = choices(population=population, k=2)#esta es una seleccion de individuos temporal, regresa 2 individuos aleatorios
            if genetic_op == 0:#crossover iniforme
                temp_new = uniform_crossover.uniform_crossover(selected_individuals[0], selected_individuals[1])
                temp_pop.append(temp_new[0])
                temp_pop.append(temp_new[1])
        ep += 1
        population = temp_pop
        print(ep)
    return population



n_population = 100

_,population = population_initialization(n_population)
population = evolution(population, 1000)
#population