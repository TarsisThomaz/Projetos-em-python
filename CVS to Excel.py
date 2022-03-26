import panda as pd
import numpy as np

df_new = pd.read_csv('nome.csv')
myfile = pd.ExcelWriter('nomedoexcel.xlsx')
df_new.to_excel(myfile, index = false)
myfile.save()