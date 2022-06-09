import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2)

people = ('A', 'B', 'C', 'D', 'E')
y1 = (39, 40, 15, 45, 35)
y2 = (-30, -35, -38, -32, -30)
ax1.barh(people[0], y1[4], align='center', color='blue')
ax1.barh(people[1], y1[3], align='center', color='pink')
ax1.barh(people[2], y1[2], align='center', color='orange')
ax1.barh(people[3], y1[1], align='center', color='grey')
ax1.barh(people[4], y1[0], align='center', color='purple')

ax1.set_title("Wykres lewy")
ax2.barh(people, y2, align='center')
ax2.set_title("Wykres prawy")

#plt.show()

dt = pd.read_excel("ceny2.xlsx")

df = pd.DataFrame(data=dt).T

print(df)
df.drop('Jednostka miary', axis=1,inplace=True)
df.drop('Rodzaje towarów', axis=1,inplace=True)
print(df)

