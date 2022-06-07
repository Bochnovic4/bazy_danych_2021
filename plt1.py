import numpy as np
import matplotlib.pyplot as plt
N = 6
menMeans = (100, 70, 80, 25, 60, 140)
womenMeans = (20, 10, 30, 10, 0, 0)
ind = np.arange(N) # the x locations for the groups
fig, ax = plt.subplots()


x = [0, 1, 2,3,4,5]
y = [120,120,120,120,120,120]

plt.plot(x, y, color='g')
ax.bar(ind[0], menMeans[0], color='g')
ax.bar(ind[0], womenMeans[0], color='purple')
ax.bar(ind[1], menMeans[1], color='g')
ax.bar(ind[1], womenMeans[1], color='b')
ax.bar(ind[2], menMeans[2], color='yellow')
ax.bar(ind[2], womenMeans[2], color='orange')
ax.bar(ind[3], menMeans[3], color='g')
ax.bar(ind[3], womenMeans[3], color='b')
ax.bar(ind[4], menMeans[5], color='w')
ax.bar(ind[4], menMeans[4], color='g')




ax.set_title('Tytuł')
ax.set_xticks(ind, ('0', '1', '2', '3', '4', '5'))


plt.show()
