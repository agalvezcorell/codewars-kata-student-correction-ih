import pandas as pd
from datetime import datetime, timedelta



def clean_katas(df): 
    df_katas = df.copy()
    
    # transform minutes to int
    df_katas.minutes = df_katas.minutes.astype('int64')
    
    # transform date to datetime
    df_katas.date = pd.to_datetime(df_katas.date,infer_datetime_format=True)
    
    # add minutes to each row combining 2 columns
    df_katas['limit'] = df_katas.apply(lambda row: row['date'] + pd.Timedelta(minutes=row['minutes']), axis=1)
    
    # transform limit to datetime
    df_katas.limit = pd.to_datetime(df_katas.limit,infer_datetime_format=True)
    
    return df_katas