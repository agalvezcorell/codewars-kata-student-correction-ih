import pandas as pd

def get_csv(csv, index): 
    try: 
        df = pd.read_csv(csv).set_index(index)
    except FileNotFoundError as e: 
        return e
    return df


def get_students_and_katas(students_csv='input/students.csv', 
                           katas_csv='input/katas.csv', 
                           students_index='username', 
                           katas_index='slug'): 
    
    df1 = get_csv(students_csv, students_index)
    df2 = get_csv(katas_csv, katas_index)
    return df1, df2

def adquire(): 
    return get_students_and_katas()