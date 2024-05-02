import create_cromosom
import os
import json

directory = 'json'
if not os.path.exists(directory):
    os.makedirs(directory)

def save_dict_as_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
        
poblation = {}
n_poblation = 100

for _ in range(n_poblation):
    poblation["Cromosoma" + str(_)] = create_cromosom.get_cromosoma(True)

save_dict_as_json(poblation, os.path.join(directory, 'cromosomas.json'))