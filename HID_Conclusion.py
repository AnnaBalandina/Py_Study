# тут ничего не трогать!
import pandas as pd
import numpy as np

data = pd.read_csv('/Users/ASUS1/Desktop/Genomed/16256.csv', delimiter=';', header = 2,
    names=['Ped_1', 'Ped_2']) # Пропиши путь до файла
data

data.to_excel('output.xlsx') # Напиши под каким именем сохранить