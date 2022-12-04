import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import json
import os
from pathlib import Path

os.chdir(Path(__file__).parent)
my_data={ 'country': 'Germany',

            'year': ['2023','2024','2025','2026','2027','2028''2029','2030']
        }

print(my_data)


# reading data from csv 
# def read_data(df):
#     df= pd.read_csv('./data1.csv',skiprows=3)
#     germany_df=df.loc[df['Country Name'] =='Germany'].T
    
#     return germany_df

# x= read_data(d)
# print(x)

