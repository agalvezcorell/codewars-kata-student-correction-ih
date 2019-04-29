import random 
import pandas as pd

def choose_presenter_last_kata(df): 
    last_kata = df.columns[-1]
    completada = list(df[df[last_kata]].index) # lista de estudiantes que han completado la kata a tiempo
    return random.choice(completada)

def display_presenter_last_kata(df): 
    student = choose_presenter_last_kata(df)
    last_kata = df.columns[-1]
    return '{} presentará la kata {}'.format(student, last_kata)