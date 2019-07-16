import pandas as pd
from modules.chosing_functions import display_presenter_last_kata


def save_results(df, folder='./output/'): 
    # CSV
    df.to_csv(folder + 'output.csv', index=True) 
    
    # excel
    writer = pd.ExcelWriter(folder + 'output.xlsx')
    df.to_excel(writer, 'Sheet1')
    writer.save()

def color_negative_red(x):
    """
    Takes a boolean and returns a string with
    the css property `'color: red'` for False
    strings, green otherwise.
    """
    color = 'red' if x == False else 'green'
    return 'color: {}'.format(color) 

def display_with_colors(df): 
    df_style = df.style.applymap(color_negative_red)
    display(df_style)


def outputs(df): 
    display_presenter_last_kata(df)       
    display_with_colors(df)   
    save_results(df)