import create_cromosom
import restriccions_function
import restrictions
import os
import json
import random

directory = 'json'
if not os.path.exists(directory):
    os.makedirs(directory)

def save_dict_as_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
        
poblation = []
n_poblation = 100

for _ in range(n_poblation):
    poblation.append(create_cromosom.get_cromosoma(True))

restrictions_dict = restrictions.restrictionsGroups()

cromosom_sort = []

for i in poblation:
    cromosom_sort.append(restriccions_function.calculate(i,restrictions_dict, True))
    
cromosom_sort.sort()

indexs = []
for i in range(0, 50):
    indexs.append(i)

cromosom_sort = cromosom_sort[:50]
second_generation = []

for _ in range (0,25):
    n = random.randint(0, len(indexs) - 1)
    n = indexs.pop(n)
    
    
    m = random.randint(0, len(indexs) - 1)
    m = indexs.pop(m)
    
    second_generation.append((cromosom_sort[n][1], cromosom_sort[m][1]))
    
print(len(second_generation))