import csv
import os
from pathlib import Path
import re
import json

def get_professors_for_block(blockdir):
    mod_path = Path(__file__).parent
    result = {}
    with open(f"{mod_path}/csvs/{blockdir}", "r", encoding="utf-8") as f:
        lines = csv.reader(f)
        headers = []
        z = 1
        for i, line in enumerate(lines):
            if i == 1:
                headers = line
            if i <= 1:
                continue
            j = 3
            while j < len(line):
                if line[j] == "X":
                    if line[0] in result.keys():
                        result[line[0]].append(headers[j])
                    else:
                        result[line[0]] = [headers[j]]
                j += 1
            z += 1
    return result

def get_professors_for_course():
    mod_path = Path(__file__).parent
    professors = {}
    with open(f"{mod_path}/csvs/Profesores y Materias.csv", "r", encoding="utf-8") as f:
        lines = csv.reader(f)
        headers = []
        for i, line in enumerate(lines):
            if i == 0:
                headers = line
            if i <= 0:
                continue
            j = 2
            while j < len(line):
                if line[j] == "X":
                    if line[0] in professors.keys():
                        professors[line[0]]["1"].append(headers[j])
                    else:
                        professors[line[0]] = {"1": [headers[j]]}
                j += 1
    blocks = [x for x in os.listdir(f"{mod_path}/csvs") if re.match(r'^.*-Profesores.csv$', x)]
    for file in blocks:
        professors[re.match(r'^.*?(?=-)', file).group(0)] = get_professors_for_block(file)
    print(json.dumps(professors, sort_keys=True, indent=4))

get_professors_for_course()