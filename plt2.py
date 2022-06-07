import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plik = pd.read_excel('C:/Users\Komputer\PycharmProjects\pythonProject\mieszkania1.xlsx')


dt = pd.DataFrame(data=plik, columns= ['Formy budownictwa','Zakres przedmiotowy','Rok','Wartosc'])
print(dt)

x1 = list(dt.loc[:,'Formy budownictwa'])
x2 = list(dt.loc[:,'Zakres przedmiotowy'])
x3= list(dt.loc[:,'Rok'])
x4= list(dt.loc[:,'Wartosc'])

dt.plot.bar(x ='Rok', y='Wartosc')
plt.show()