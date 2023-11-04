import pprint
import random

import numpy as np


grid = [[[0 for j in range(3)] for i in range (5)] for k in range(2)]

# grid[0][4][2]=100
pprint.pprint(grid)

# grid[0][1][4] = "O"
# list = [1,3,4]
# v = np.array(list)
#
# grid[1][2][4]=list    # [k][i][j]
#

# pprint.pprint(grid)
# print(grid[1][2][4])

# lst = []
# grid[1][2][4].append(900)
# # print(grid[1][2][4][0])
# del grid[1][2][4][2]
#
# grid[0][0][0] = 0
# grid[0][1][0] = 1
# grid[1][0][0] = 2
# grid[1][1][0] = 3
#
# grid[0][0][1] = 4
# grid[0][1][1] = 5
# grid[1][0][1] = 6
# grid[1][1][1] = 7
for k in range(2):
    for i in range (5):
        for j in range(3):
            l = []
            grid[k][i][j] = l
            grid[k][i][j].append(2)
            grid[k][i][j].append(4)
            print(grid[k][i][j])
            print(len(grid[k][i][j]))
grid[0][0][0].append(5)
pprint.pprint(grid)
print(grid[0][0][0])
print(random.choice(grid[0][0][0]))
