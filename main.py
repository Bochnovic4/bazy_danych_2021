import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# Example data
people = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(people))
performance = np.arange(-50,0,10)

ax.barh(people[0], -47, color = 'yellow')
ax.barh(people[1], -27, color = 'brown')
ax.barh(people[2], -23, color = 'purple')
ax.barh(people[3], -15, color = 'red')
ax.barh(people[4], -50, color = 'blue')
ax.set_yticks(y_pos, labels=people)

ax.set_title('Test')

plt.savefig('test.jpg')
plt.show()