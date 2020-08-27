import pandas as pd
from modules.checking_functions import get_slug

def clean_df(df): 
    df.columns = df.columns.str.strip() # strip column names
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x) # strip all columns of str type
    return df


def get_csv(csv_file, new_index_col): 
    try: 
        df = pd.read_csv(csv_file)
        df = clean_df(df)
        df = df.set_index(new_index_col)
    except FileNotFoundError as e: 
        return e
    return df


def get_students_and_katas(students_csv='input/students.csv', 
                           katas_csv='input/katas.csv', 
                           students_index='username', 
                           katas_index='id'): 
    
    df1 = get_csv(students_csv, students_index)
    df2 = get_csv(katas_csv, katas_index)
    return df1, df2

def update_slugs(katas_csv='input/katas.csv'):
    katas = pd.read_csv(katas_csv)
    missing_slug = set(katas[katas["slug"].isna()]["id"])
    slugger = {id:get_slug(id) for id in missing_slug}
    katas.loc[katas["slug"].isna(),"slug"] = katas["id"].apply(lambda id: slugger.get(id))
    katas.to_csv('input/katas.csv',index=False)

def adquire(): 
    update_slugs()
    return get_students_and_katas()
