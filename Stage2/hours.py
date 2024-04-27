import csv
import os
from pathlib import Path
import re

def hoursCourses():
    hours = {}
    mod_path = Path(__file__).parent
    blocks = [x for x in os.listdir(f"{mod_path}/csvs") if re.match(r'^.*-Profesores.csv$', x)]
    print (blocks)

    for _ in range(len(blocks)):
        with open(f"{mod_path}/csvs/"+blocks[_], "r") as f:
            lines = csv.reader(f)
            for i, line in enumerate(lines):



hoursCourses()