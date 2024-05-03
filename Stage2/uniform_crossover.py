import random
import copy
import copy
import random
from pprint import pprint as pp
import json
import json

cromosomes_pots = json.load(open(".//json//cromosomas.json"))

#Select 2 random cromosomes
def select_cromosomes():
    cromosomes = list(cromosomes_pots.keys())
    cromosomes = random.sample(cromosomes, 2)
    return cromosomes


def uniform_crossover(cr1, cr2):
    cr1 = cromosomes_pots[cr1]
    cr2 = cromosomes_pots[cr2]
    
    # Select a random point in the cromosomes
    point = random.randint(0, len(cr1))
    
    # Create a new cromosome
    new_cromosome = []
    
    # Copy the first part of the cromosome
    for i in range(0, point):
        new_cromosome.append(cr1[i])
    
    # Copy the second part of the cromosome
    for i in range(point, len(cr2)):
        new_cromosome.append(cr2[i])
        
    point = random.randint(0, len(cr2))
        
    #Generate another cromosome
    new_cromosome2 = []
    
    # Copy the first part of the cromosome
    for i in range(0, point):
        new_cromosome2.append(cr2[i])
        
    # Copy the second part of the cromosome
    for i in range(point, len(cr1)):
        new_cromosome2.append(cr1[i])
        
    return new_cromosome, new_cromosome2
    

# pp(uniform_crossover(*select_cromosomes()))





