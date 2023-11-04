import csv
import matplotlib.pyplot as plt
import numpy as np
user = []
MEC10 = []
MEC15 = []
MEC20 = []
MEC25 = []
MEC30 = []

with open('NP_hard.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        user.append(int(row[1]))
        MEC10.append(float(row[2]))
        MEC15.append(float(row[3]))
        MEC20.append(float(row[4]))
        # MEC25.append(float(row[5]))
        # MEC30.append(float(row[6]))


plt.errorbar(user, MEC10, color='green', label='10 MEC', yerr=0.0,  marker='v')
plt.errorbar(user, MEC15, color='red', label='15 MEC', yerr=0.0,  marker='o')
plt.errorbar(user, MEC20, color='blue', label='20 MEC', yerr=0.0,  marker='X')
# plt.errorbar(user, MEC25, color='y', label='25 MEC', yerr=0.0,  marker='^')
# plt.errorbar(user, MEC30, color='red', label='30 MEC', yerr=0.0,  marker='s')
plt.xlim(48, 302)
plt.ylim(-0.01, 3001)
plt.xticks(np.arange(50, 300, step=50))
plt.ylabel('Running Time (ms)', fontsize=12)
plt.yticks(np.arange(0, 3001, step=500))
plt.show()
