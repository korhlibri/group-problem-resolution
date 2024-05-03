import numpy as np
from random import randint, choice, choices

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import os
import json

from create_cromosom import get_cromosoma
from restriccions_function import calculate
from restrictions import restrictionsGroups
from tournament import tournament
from plot_score import plot_score

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
    cost_hist = []
    
    while ep < epochs:
        temp_pop = []
        len_pop = len(population)
        penalisations, selected_individuals = tournament(population, 45)
        best_score = penalisations[0][0]
        cost_hist.append(best_score)

        for ind in penalisations[:10]:
            temp_pop.append(ind[1])
            #print(ind[1])
        #print(len(temp_pop))

        #print('pe: ',penalisations[0])
        i = 0
        while len(temp_pop) != len_pop:
            genetic_op = choices(population=[0,1,2], weights=[0.0, 0.1, 0.9])[0] #seleccion de operadores geneticos temporal, se queda fija para propositos de prueba
            #selected_individuals = choices(population=population, k=2)#esta es una seleccion de individuos temporal, regresa 2 individuos aleatorios

            #print(selected_individuals)
            if genetic_op == 0:#crossover uniforme
                temp_new = uniform_crossover.uniform_crossover(selected_individuals[i][0], selected_individuals[i][1])
                temp_pop.append(temp_new[0])
                temp_pop.append(temp_new[1])
            elif genetic_op == 1:#crossover point
                points = choices([1, 2, 3, 4, 5], weights=[.35, .35, .1, .1, .1])
                temp_new = multi_point_crossover.multiCross(points, selected_individuals[i][0], selected_individuals[i][1])
                temp_pop.append(temp_new[0])
                temp_pop.append(temp_new[1])
            elif genetic_op == 2:#mutation
                temp_new = (mutation_operator.mutation_operator(selected_individuals[i][0], True), mutation_operator.mutation_operator(selected_individuals[i][1], True))
                temp_pop.append(temp_new[0])
                temp_pop.append(temp_new[1])
            i+=1
        ep += 1
        population = temp_pop
        print(f"epoch: {ep} ---- best score: {best_score}")
    return population, cost_hist

population = []

n_population = 100
epochs = 100
_,population = population_initialization(n_population)
population, cost_hist = evolution(population, epochs)

print(population)
print(cost_hist)
print(np.min(cost_hist))
plot_score(cost_hist)