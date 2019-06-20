import random 
import pandas as pd

NO_STUDENT = 'Nadie'

def choose_presenter_last_kata(df): 
    last_kata = df.columns[-1]
    completada = list(df[df[last_kata]].index) # lista de estudiantes que han completado la kata a tiempo
    
    if completada: 
        return random.choice(completada), last_kata
    else: 
        return NO_STUDENT, last_kata

def display_presenter_last_kata(df): 
    student, last_kata = choose_presenter_last_kata(df)
    print( '{} presentará la kata {}'.format(student, last_kata) )