import pandas as pd
from pathlib import Path

def dict_courses_period(df):
    courses_period = {}
    for index, row in df.iterrows():
        #print(row['Clave'],row['P1'], row['P2'], row['P3'])
        periods = [i for i,p in enumerate([row['P1'], row['P2'], row['P3']],1) if p != '-']
        #print(periods)
        courses_period[row['Clave']] = periods
    print(courses_period)
    #return courses_period

def get_courses_period(semester_even):
    mod_path = Path(__file__).parent
    df = pd.read_csv(f"{mod_path}/csvs/UDF.csv")
    if semester_even is True:
        df = df.drop(df[(df.Semestre % 2) != 0].index)
    else:
        df = df.drop(df[(df.Semestre % 2) == 0].index)
    dict_courses_period(df)


get_courses_period(True)
print('---')
get_courses_period(False)