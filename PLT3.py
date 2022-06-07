import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x = np.arange(-7,7, 0.1)
y_ax = np.arange(-40, 40)
y1 = 7-x
y2 = (2*x/5)-2
y3 = 20 * np.sin(x)

ax.plot(x,y3, label = 'y=20*sin(x)', linestyle='dashed', color = 'r')
ax.plot(x,y2, label = 'y=(2x/5)-2', linestyle='dashed', color = 'orange')
ax.plot(x,y1, label= 'y=7-x', color = 'g')

ax.legend(loc= 3)
plt.ylim(-30, 30)
plt.title('Tytuł ABCD')
plt.show()