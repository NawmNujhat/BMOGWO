import matplotlib.pyplot as plt
import matplotlib.patches as graph_patches
import numpy as np

ypoints = np.array([3, 8, 1, 10])
x = np.array([9,4,1])
plt.plot(ypoints, marker = '|', color='r',ms = 20, mec = 'r',mfc = 'r')

plt.plot(x, marker = 'o' , ms=20 )


BFS = graph_patches.Patch(color="purple",label="BFS")
plt.legend(handles=[BFS])

plt.show()