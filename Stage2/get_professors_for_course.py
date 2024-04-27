import csv
import os
from pathlib import Path

def get_professors_for_course():
    mod_path = Path(__file__).parent
    professors = {}
    with open(f"{mod_path}/csvs/Profesores y Materias.csv", "r") as f:
        lines = csv.reader(f)
        headers = []
        for i, line in enumerate(lines):
            if i == 0:
                headers = line
            j = 2
            while j < len(line):
                if line[j] == "X":
                    if line[0] in professors.keys():
                        professors[line[0]].append(headers[j])
                    else:
                        professors[line[0]] = [headers[j]]
                j += 1
    print(professors)

get_professors_for_course()