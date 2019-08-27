import pandas as pd
import numpy as np
import requests
import json
from bs4 import BeautifulSoup

CW_HOST = 'https://www.codewars.com/api/v1/users/'
CW_RECURSE = '/code-challenges/completed'


def get_completed_by_user(user, host=CW_HOST, path=CW_RECURSE):
    url = host + user + path
    resp = requests.get(url)    
    return resp.json()

def user_time_kata(user, slug, completed, katas): 
    res = '2090-01-01T00:00:00.000Z'# default
    for data in completed[user]: 
        if data['slug'] == slug: 
            res = data['completedAt']
            break
    return res

def get_info_dict(df_students): 
    completed = {u: get_completed_by_user(u) for u in df_students.index}

    ## print(completed)
    res_dict = dict( [(k, v['data']) for k, v in completed.items()] )
    return res_dict

def create_df_checking(df_students, df_katas): 
    katas = df_katas.index
    students = df_students.index
    
    # Creamos un DataFrame: Students x Katas
    df_res = pd.DataFrame(index=df_students.index, columns=df_katas.index)
        
    # tarda un rato
    completed_katas_dict = get_info_dict(df_students)
       
    # cada celda es el tiempo que ese student(row) tardó en realizar la kata(column)
    # TO DO: si solo hay una kata y no una lista, da problemas. 
    for user in students: 
        for slug in katas: 
            df_res.loc[user, slug] = user_time_kata(user, slug, completed_katas_dict, katas)
    
    # convertimos las columnas a tipo Datetime
    for col in df_res.columns: 
        df_res[col] = pd.to_datetime(df_res[col],infer_datetime_format=True)
        
    # En este punto df_res son valores temporales    
    # copiamos la solución en otro DF porque en el bucle la segunda vez da problemas al cambiar el tipo
    df_sol = df_res.copy()

    # display(df_res)
    for user in students: 
        df_sol.loc[user] = df_res.loc[user] < df_katas.limit
    
    return df_sol