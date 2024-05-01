import pandas as pd
from pathlib import Path
from get_groups import get_period

def dict_courses_period(df):
    p1, p2, p3 = [],[],[]
    
    for index, row in df.iterrows():
        #print(row['Clave'],row['P1'], row['P2'], row['P3'])
        periods = [i for i,p in enumerate([row['P1'], row['P2'], row['P3']],1) if p != '-']
        for i in periods:
            if i == 1:
                p1.append(row['Clave'])
            if i == 2:
                p2.append(row['Clave'])
            if i == 3:
                
                per1 = get_period(True)
                per2 = get_period(False)
                        
                if row['Clave'] in per1 or row['Clave'] in per2:
                    p3.append(row['Clave'])
                
                
    courses_period = {1:p1, 2:p2, 3:p3}
    print(courses_period)
    #return courses_period

def get_courses_period(semester_even):
    mod_path = Path(__file__).parent
    df = pd.read_csv(f"{mod_path}/csvs/UDF.csv")
    df = df.fillna('-')
    #print(df)
    if semester_even is True:
        df = df.drop(df[(df.Semestre % 2) != 0].index)
    else:
        df = df.drop(df[(df.Semestre % 2) == 0].index)
    return dict_courses_period(df)


# get_courses_period(True)
# print('---')
# get_courses_period(False)