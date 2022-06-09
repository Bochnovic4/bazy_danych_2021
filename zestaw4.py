import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#x = np.arange(-5,5, 0.01)
#x_pos = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
#y1 = -x**3 +3*x-7
#y2 = 4*x +6
#y3 = 6+4*x**3

#plt.plot(x,y1, label="-x^3 + 3 * x - 7")
#plt.plot(x,y2, label="4 * x + 6")
#plt.plot(x,y3, label="6 + 4 * x^3")
#plt.legend()
#plt.grid()
#plt.show()

#dt = pd.read_excel("kina4.xlsx")

#df = pd.DataFrame(data=dt)
#df2 = df.groupby("Wykaz").mean()
#print(df2)
#df3= df.groupby("Rok").mean()
#s = "TEXT"
#print(df3)

#plt.rcParams["figure.figsize"] = (10,10)

#df3.plot.bar( y=0, legend=None)
#plt.text(2,25000,s, size=15)

#plt.show()

dt = pd.read_csv("sprzedaz4.csv",sep='@')
df = pd.DataFrame(data=dt)
df = df.dropna()
df.rename(columns = {'Jabłka.1':'Jabłka', 'Jabłka.2':'Jabłka','Jabłka.3':'Jabłka','Śliwki.1':'Śliwki', 'Śliwki.2':'Śliwki','Śliwki.3':'Śliwki','Gruszki.1':'Gruszki', 'Gruszki.2':'Gruszki','Gruszki.3':'Gruszki'}, inplace = True)
df2 = df.transpose()
print(df2)

df3 = df2.groupby(level=0).mean()
print("------------------------------")
print(df3)
df3 = df3.transpose()
print(df3)
x = df3.iloc[1]
explode = (0, 0.1, 0)
Rodzaj = ["Gruszki","Śliwki","Jabłka"]
fig, ax = plt.subplots()
ax.pie(x, explode=explode, labels=Rodzaj, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax.axis('equal')

plt.show()