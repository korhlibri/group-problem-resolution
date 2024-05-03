import day1
from create_cromosom import get_cromosoma
from pprint import pprint as pp
import random

def multiCross(nPoints, cromosome1, cromosome2):

    puntos_master = []
    while nPoints > 0:
        point = random.randint(1, len(cromosome1['Cromosoma0'].keys()))
        if point in puntos_master:
            continue
        else:
            puntos_master.append(point)
            nPoints -= 1

    cromosome_son1 = []
    cromosome_son2 = []
    
    for i in range(len(cromosome1['Cromosoma0'])):
        if i in puntos_master:
            cromosome_son1['Cromosoma0'].append(cromosome2['Cromosoma0'][i])
            cromosome_son2['Cromosoma0'].append(cromosome1['Cromosoma0'][i])
        else:
            cromosome_son1['Cromosoma0'].append(cromosome1['Cromosoma0'][i])
            cromosome_son2['Cromosoma0'].append(cromosome2['Cromosoma0'][i])
        contador += 1
        
    return cromosome_son1, cromosome_son2