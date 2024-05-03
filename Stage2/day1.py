import create_cromosom
import restriccions_function
import restrictions
import os
import json

directory = 'json'
if not os.path.exists(directory):
    os.makedirs(directory)

def save_dict_as_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
        
poblation = []
n_poblation = 5

for _ in range(n_poblation):
    poblation.append(create_cromosom.get_cromosoma(True))

restrictions_dict = restrictions.restrictionsGroups()

cromosom_sort = []

for i in poblation:
    cromosom_sort.append(restriccions_function.calculate(i,restrictions_dict, True))
    
cromosom_sort.sort()
print(cromosom_sort)