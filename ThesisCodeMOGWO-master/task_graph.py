import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4
import matplotlib.pyplot as plt5
import matplotlib.pyplot as plt6
import matplotlib.pyplot as plt7
import matplotlib.pyplot as plt8
import matplotlib.pyplot as plt9
import matplotlib.pyplot as plt10
import matplotlib.pyplot as plt11

user = []
QoeBMOGWO = []
QoeMGBD = []
QoeiRAF = []
QoeMoEAD = []
EnergyBMOGWO = []
EnergyMGBD = []
EnergyiRAF = []
EnergyMoEAD = []
CostBMOGWO = []
CostMGBD = []
CostiRAF = []
CostMoEAD = []
TCRBMOGWO = []
TCRMGBD = []
TCRiRAF = []
TCRmoEAD = []

igdbmogwo=[]
igdMoead=[]
igdBat=[]

hypvalbmogwo=[]
hypvalMoead=[]
hypvalBat=[]

server = []
s_QoeBMOGWO = []
s_QoeMGBD = []
s_QoeiRAF = []
s_QoEMoead = []
s_EnergyBMOGWO = []
s_EnergyMGBD = []
s_EnergyiRAF = []
s_EnergyMoead = []
s_CostBMOGWO = []
s_CostMGBD = []
s_CostiRAF = []
s_CostMoead = []

cycle = []
cycle_LatencyBMOGWO = []
cycle_LatencyNoCaching = []
cycle_EnergyBMOGWO = []
cycle_EnergyNoCaching = []
cycle_CostBMOGWO = []
cycle_CostNoCaching = []

with open('file_1.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        user.append(int(row[0]))
        print(int(row[0]))
        QoeBMOGWO.append(float(row[1]))
        QoeMoEAD.append(float(row[2]))
        QoeMGBD.append(float(row[3]))
        QoeiRAF.append(float(row[4]))

        EnergyBMOGWO.append(float(row[5]))
        EnergyMoEAD.append(float(row[6]))
        EnergyMGBD.append(float(row[7]))
        EnergyiRAF.append(float(row[8]))

        CostBMOGWO.append(float(row[9]))
        CostMoEAD.append(float(row[10]))
        CostMGBD.append(float(row[11]))
        CostiRAF.append(float(row[12]))

        TCRBMOGWO.append(float(row[13]))
        TCRmoEAD.append(float(row[14]))
        TCRMGBD.append(float(row[15]))
        TCRiRAF.append(float(row[16]))

with open('igd_hypval_task.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        igdbmogwo.append(float(row[1]))
        igdMoead.append(float(row[2]))
        igdBat.append(float(row[3]))

        hypvalbmogwo.append(float(row[4]))
        hypvalMoead.append(float(row[5]))
        hypvalBat.append(float(row[6]))

with open('file_2.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)

    for row in csvReader:
        server.append(int(row[0]))
        s_QoeBMOGWO.append(float(row[1]))
        s_QoeMGBD.append(float(row[2]))
        s_QoeiRAF.append(float(row[3]))

        s_EnergyBMOGWO.append(float(row[4]))
        s_EnergyMGBD.append(float(row[5]))
        s_EnergyiRAF.append(float(row[6]))

        s_CostBMOGWO.append(float(row[7]))
        s_CostMGBD.append(float(row[8]))
        s_CostiRAF.append(float(row[9]))

with open('file_3_cached.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        cycle.append(float(row[0]))
        cycle_LatencyBMOGWO.append(float(row[1]))
        cycle_LatencyNoCaching.append(float(row[2]))
        cycle_EnergyBMOGWO.append(float(row[3]))
        cycle_EnergyNoCaching.append(float(row[4]))
        cycle_CostBMOGWO.append(float(row[5]))
        cycle_CostNoCaching.append(float(row[6]))


def task_graph():
    plt.errorbar(user, QoeBMOGWO, color='green', label='WOLVERINE', yerr=0.9, marker='+')
    plt.errorbar(user, QoeMoEAD, color='purple', label='MOEA/D', yerr=0.8, marker='*')
    plt.errorbar(user, QoeMGBD, color='red', label='MGBD', yerr=0.75, marker='o')
    plt.errorbar(user, QoeiRAF, color='blue', label='iRAF', yerr=0.69, marker='v')

    plt.xlim(2, 270)
    plt.ylim(-.01, 12.1)
    plt.xlabel('Number of tasks', fontsize=14)
    plt.xticks(np.arange(10, 261, step=50))
    plt.ylabel('Average Latency (s)', fontsize=14)
    plt.yticks(np.arange(0, 12.1, step=2))
    plt.legend()
    plt.savefig("Task_vs_Latency.jpg")
    plt.show()

    plt.errorbar(user, EnergyBMOGWO, color='green', label='WOLVERINE', yerr=30, marker='+')
    plt.errorbar(user, EnergyMoEAD, color='purple', label='MOEA/D', yerr=33, marker='*')
    plt.errorbar(user, EnergyMGBD, color='red', label='MGBD', yerr=35, marker='o')
    plt.errorbar(user, EnergyiRAF, color='blue', label='iRAF', yerr=38, marker='v')
    plt.xlim(2, 270)
    plt.ylim(-.01, 501)
    plt.xlabel('Number of tasks', fontsize=14)
    plt.xticks(np.arange(10, 261, step=50))
    plt.ylabel('Average Energy Consumption (mJ)', fontsize=14)
    plt.yticks(np.arange(0, 501, step=50))
    plt.legend()
    plt.savefig("Task_vs_Energy.jpg")
    plt.show()

    plt.errorbar(user, CostBMOGWO, color='green', label='WOLVERINE', yerr=.042, marker='+')
    plt.errorbar(user, CostMoEAD, color='purple', label='MOEA/D', yerr=.062, marker='*')
    plt.errorbar(user, CostMGBD, color='red', label='MGBD', yerr=.052, marker='o')
    plt.errorbar(user, CostiRAF, color='blue', label='iRAF', yerr=.068, marker='v')
    plt.xlim(2, 270)
    plt.ylim(-.01, 1.01)
    plt.xlabel('Number of tasks', fontsize=14)
    plt.xticks(np.arange(10, 261, step=50))
    plt.ylabel('Average Normalized Savings', fontsize=14)
    plt.yticks(np.arange(0, 1.01, step=.1))
    plt.legend()
    plt.savefig("Task_vs_Savings.jpg")
    plt.show()

    plt.errorbar(user, TCRBMOGWO, color='green', label='WOLVERINE', yerr=.032, marker='+')
    plt.errorbar(user, TCRmoEAD, color='purple', label='MOEA/D', yerr=.045, marker='*')
    plt.errorbar(user, TCRMGBD, color='red', label='MGBD', yerr=.050, marker='o')
    plt.errorbar(user, TCRiRAF, color='blue', label='iRAF', yerr=.059, marker='v')
    plt.xlim(2, 270)
    plt.ylim(0.29, 1.01)
    plt.xlabel('Number of tasks', fontsize=14)
    plt.xticks(np.arange(10, 261, step=50))
    plt.ylabel('Task Completion Reliability', fontsize=14)
    plt.yticks(np.arange(.3, 1.01, step=.1))
    plt.legend()
    plt.savefig("Task_vs_TCR.jpg")
    plt.show()


def server_graph():
    plt.errorbar(server, s_QoeBMOGWO, color='green', label='WOLVERINE', yerr=6, marker='+')
    plt.errorbar(server, s_QoeMGBD, color='red', label='MGBD', yerr=8.6, marker='o')
    plt.errorbar(server, s_QoeiRAF, color='blue', label='iRAF', yerr=9, marker='v')
    plt.xlim(1.5, 12.4)
    plt.ylim(18, 181)
    plt.xlabel('Number of servers', fontsize=14)
    plt.xticks(np.arange(2, 12.2, step=2))
    plt.ylabel('Average Latency (ms)', fontsize=14)
    plt.yticks(np.arange(20, 181, step=20))
    plt.legend()
    plt.savefig("Server_vs_Latency.jpg")
    plt.show()

    plt.errorbar(server, s_EnergyBMOGWO, color='green', label='WOLVERINE', yerr=.6, marker='+')
    plt.errorbar(server, s_EnergyMGBD, color='red', label='MGBD', yerr=.95, marker='o')
    plt.errorbar(server, s_EnergyiRAF, color='blue', label='iRAF', yerr=1, marker='v')
    plt.xlim(1.7, 12.4)
    plt.ylim(-0.1, 14.2)
    plt.xlabel('Number of servers', fontsize=14)
    plt.xticks(np.arange(2, 12.2, step=2))
    plt.ylabel('Average Energy Consumption (J)', fontsize=14)
    plt.yticks(np.arange(0, 14.2, step=2))
    plt.legend()
    plt.savefig("Server_vs_Energy.jpg")
    plt.show()

    plt.errorbar(server, s_CostBMOGWO, color='green', label='WOLVERINE', yerr=.015, marker='+')
    plt.errorbar(server, s_CostMGBD, color='red', label='MGBD', yerr=.021, marker='o')
    plt.errorbar(server, s_CostiRAF, color='blue', label='iRAF', yerr=.025, marker='v')
    plt.xlim(1.7, 12.4)
    plt.ylim(0.59, 1.01)
    plt.xlabel('Number of servers', fontsize=14)
    plt.xticks(np.arange(2, 12.4, step=2))
    plt.ylabel('Average Normalized Cost', fontsize=14)
    plt.yticks(np.arange(.6, 1.01, step=.1))
    plt.legend()
    plt.savefig("Server_vs_Cost.jpg")
    plt.show()


def cached_or_not():
    plt.errorbar(cycle, cycle_LatencyBMOGWO, color='dodgerblue', label='WOLVERINE', yerr=2.4, marker='x')
    plt.errorbar(cycle, cycle_LatencyNoCaching, color='darkorange', linestyle='dashed', label='No caching+offloading',
                 yerr=4.6, marker='d')
    plt.xlim(-.01, 3.1)
    plt.ylim(9, 100)
    plt.xlabel('Average computation per task (gigacycles)', fontsize=14)
    plt.xticks(np.arange(0, 3.02, step=.5))
    plt.ylabel('Average Latency (ms)', fontsize=14)
    plt.yticks(np.arange(10, 101, step=10))
    plt.legend()
    plt.savefig("Cached_Latency.jpg")
    plt.show()

    plt.errorbar(cycle, cycle_EnergyBMOGWO, color='dodgerblue', label='WOLVERINE', yerr=.4, marker='x')
    plt.errorbar(cycle, cycle_EnergyNoCaching, color='darkorange', linestyle='dashed', label='No caching+offloading',
                 yerr=.7, marker='d')
    plt.xlim(-.01, 3.1)
    plt.ylim(-.1, 14.2)
    plt.xlabel('Average computation per task (gigacycles)', fontsize=14)
    plt.xticks(np.arange(0, 3.02, step=.5))
    plt.ylabel('Average Energy consumption (J)', fontsize=14)
    plt.yticks(np.arange(0, 15, step=2))
    plt.legend()
    plt.savefig("Cached_Energy.jpg")
    plt.show()

    plt.errorbar(cycle, cycle_CostBMOGWO, color='dodgerblue', label='WOLVERINE', yerr=.04, marker='x')
    plt.errorbar(cycle, cycle_CostNoCaching, color='darkorange', linestyle='dashed', label='No caching+offloading',
                 yerr=.07, marker='d')
    plt.xlim(-.01, 3.1)
    plt.ylim(-.01, 1)
    plt.xlabel('Average computation per task (gigacycles)', fontsize=14)
    plt.xticks(np.arange(0, 3.02, step=.5))
    plt.ylabel('Average Normalized Cost', fontsize=14)
    plt.yticks(np.arange(0, 1.01, step=.1))
    plt.legend()
    plt.savefig("Cached_Cost.jpg")
    plt.show()

def igd_graph():
    print(user)
    print(igdbmogwo)
    print(igdMoead)
    print(igdBat)
    plt.errorbar(user, igdbmogwo, color='green', label='WOLVERINE', yerr=.3, marker='+')
    plt.errorbar(user, igdMoead, color='red', label='MOEAD', yerr=.25, marker='o')
    plt.errorbar(user, igdBat, color='blue', label='BAT', yerr=.2, marker='v')
    plt.xlim(2,270)
    plt.ylim(0.29, 1.01)
    plt.xlabel('Number of tasks', fontsize=14)
    plt.xticks(np.arange(10, 261, step=50))
    plt.ylabel('Inverted Generational Distance)', fontsize=14)
    plt.yticks(np.arange(0, 5, step=.5))
    plt.legend()
    plt.savefig("Users_Vs_IGD.jpg")
    plt.show()

    plt.errorbar(user, hypvalbmogwo, color='green', label='WOLVERINE', yerr=4, marker='+')
    plt.errorbar(user, hypvalMoead, color='red', label='MOEAD', yerr=4.3, marker='o')
    plt.errorbar(user, hypvalBat, color='blue', label='BAT', yerr=4.7, marker='v')
    plt.xlim(2,270)
    plt.ylim(0.29, 1.01)
    plt.xlabel('Number of Users', fontsize=14)
    plt.xticks(np.arange(10, 261, step=50))
    plt.ylabel('Hypervolume', fontsize=14)
    plt.yticks(np.arange(0, 114.2, step=10))
    plt.legend()
    plt.savefig("Users_Vs_Hypervolume.jpg")
    plt.show()



#task_graph()
#cached_or_not()
igd_graph()


user = [10, 60, 110, 160, 210, 260]
# time=[101.51,430.35,26.06,167.18,83.73,10.2,9.89,13.01,5.03]
time = [0.32, 1.06, 1.11, 1.15, 2.29, 3.01]
energy = [0.04, 0.09, 0.11, 0.14, 0.18, 0.24]
cost = [7.62, 13.05, 14.6, 15.7, 17.54, 20.34]
# user budget =25.00
# bhag diye nis
# Budget er graph e (25-cost[i])/25 kore nis. R naam dis Average Normalized Savings
# TCR o same,(1-Task ratio) Y axis e
