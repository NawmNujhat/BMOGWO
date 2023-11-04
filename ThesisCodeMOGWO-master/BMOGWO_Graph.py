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
EnergyBMOGWO = []
EnergyMGBD = []
EnergyiRAF = []
CostBMOGWO = []
CostMGBD = []
CostiRAF = []

server = []
s_QoeBMOGWO = []
s_QoeMGBD = []
s_QoeiRAF = []
s_EnergyBMOGWO = []
s_EnergyMGBD = []
s_EnergyiRAF = []
s_CostBMOGWO = []
s_CostMGBD = []
s_CostiRAF = []
s_TCRBMOGWO = []
s_TCRMGBD = []
s_TCRiRAF = []
cycle = []
cycle_LatencyBMOGWO = []
cycle_LatencyNoCaching = []
cycle_EnergyBMOGWO = []
cycle_EnergyNoCaching = []
cycle_CostBMOGWO = []
cycle_CostNoCaching = []
cycle_TCRBMOGWO = []
cycle_TCRNoCaching = []

# with open('file_1.csv') as csvDataFile:
#     csvReader = csv.reader(csvDataFile)
#     for row in csvReader:
#         user.append(int(row[0]))
#         QoeBMOGWO.append(float(row[1]))
#         QoeMGBD.append(float(row[2]))
#         QoeiRAF.append(float(row[3]))
#
#         EnergyBMOGWO.append(float(row[4]))
#         EnergyMGBD.append(float(row[5]))
#         EnergyiRAF.append(float(row[6]))
#
#         CostBMOGWO.append(float(row[7]))
#         CostMGBD.append(float(row[8]))
#         CostiRAF.append(float(row[9]))


with open('file_2.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        print(row)
        server.append(int(row[0]))
        s_QoeBMOGWO.append(float(row[9])*1000)
        s_EnergyBMOGWO.append(float(row[10]))
        s_CostBMOGWO.append(float(row[11]))
        s_TCRBMOGWO.append(float(row[12]))
        s_QoeMGBD.append(float(row[5])*1000)
        s_EnergyMGBD.append(float(row[6]))
        s_CostMGBD.append(float(row[7]))
        s_TCRMGBD.append(float(row[8]))
        s_QoeiRAF.append(float(row[1])*1000)
        s_EnergyiRAF.append(float(row[2]))
        s_CostiRAF.append(float(row[3]))
        s_TCRiRAF.append(float(row[4]))

with open('file_3_cached.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        #print(row)
        cycle.append(float(row[0]))
        cycle_LatencyBMOGWO.append(float(row[5])*1000)
        cycle_EnergyBMOGWO.append(float(row[6]))
        cycle_CostBMOGWO.append(float(row[7]))
        cycle_TCRBMOGWO.append(float(row[8]))
        cycle_LatencyNoCaching.append(float(row[1])*1000)
        cycle_EnergyNoCaching.append(float(row[2]))
        cycle_CostNoCaching.append(float(row[3]))
        cycle_TCRNoCaching.append(float(row[4]))

def task_graph():
    plt.errorbar(user, QoeBMOGWO, color='green',label='WOLVERINE', yerr=10,  marker='+')
    plt.errorbar(user, QoeMGBD, color='red', label='MGBD', yerr= 15, marker='o')
    plt.errorbar(user, QoeiRAF, color='blue', label='iRAF', yerr=15, marker='v')
    plt.xlim(2, 270)
    plt.ylim(-.01, 301)
    plt.xlabel('Number of tasks', fontsize=14)
    plt.xticks(np.arange(10, 261, step=50))
    plt.ylabel('Average Latency (ms)', fontsize=14)
    plt.yticks(np.arange(0, 301, step= 50))
    plt.legend()
    plt.savefig("Task_vs_Latency.jpg")
    plt.show()

    plt.errorbar(user, EnergyBMOGWO, color='green', label='WOLVERINE', yerr=.6, marker='+')
    plt.errorbar(user, EnergyMGBD, color='red', label='MGBD', yerr=.9, marker='o')
    plt.errorbar(user, EnergyiRAF, color='blue', label='iRAF', yerr=1.1, marker='v')
    plt.xlim(2, 270)
    plt.ylim(-.01, 21.5)
    plt.xlabel('Number of tasks', fontsize=14)
    plt.xticks(np.arange(10, 261, step=50))
    plt.ylabel('Average Energy Consumption (J)', fontsize=14)
    plt.yticks(np.arange(0, 22, step=3))
    plt.legend()
    plt.savefig("Task_vs_Energy.jpg")
    plt.show()
    # print(EnergyBMOGWO)
    # print(EnergyLyp)
    # print(EnergyMGBD)

    plt.errorbar(user, CostBMOGWO, color='green', label='WOLVERINE', yerr=.028, marker='+')
    plt.errorbar(user, CostMGBD, color='red', label='MGBD', yerr=.04, marker='o')
    plt.errorbar(user, CostiRAF, color='blue', label='iRAF', yerr=.05, marker='v')
    plt.xlim(2, 270)
    plt.ylim(-.01, 1.01)
    plt.xlabel('Number of tasks', fontsize=14)
    plt.xticks(np.arange(10, 261, step=50))
    plt.ylabel('Average Normalized Cost', fontsize=14)
    plt.yticks(np.arange(0, 1.1, step=.1))
    plt.legend()
    plt.savefig("Task_vs_Cost.jpg")
    plt.show()


def server_graph():
    # plt.errorbar(server, s_QoeBMOGWO, color='green',label='WOLVERINE', yerr=0.4,  marker='+')
    # plt.errorbar(server, s_QoeMGBD, color='red', label='MGBD', yerr= 0.6, marker='o')
    # plt.errorbar(server, s_QoeiRAF, color='blue', label='iRAF', yerr=0.8, marker='v')
    # plt.xlim(1.5, 18.4)
    # plt.ylim(-0.1, 1000)
    # plt.xlabel('Number of servers', fontsize=14)
    # plt.xticks(np.arange(2, 18.2, step=2))
    # plt.ylabel('Average Latency (ms)', fontsize=14)
    # plt.yticks(np.arange(0, 14000, step= 2000))
    # plt.legend()
    # plt.savefig("Server_vs_Latency.jpg")
    # plt.show()

    # print(s_EnergyBMOGWO)
    # print(s_EnergyMGBD)
    # print(s_EnergyiRAF)
    plt.errorbar(server, s_EnergyBMOGWO, color='green', label='WOLVERINE', yerr=50, marker='+')
    plt.errorbar(server, s_EnergyMGBD, color='red', label='MGBD', yerr=85, marker='o')
    plt.errorbar(server, s_EnergyiRAF, color='blue', label='iRAF', yerr=70, marker='v')
    plt.xlim(1.7, 18.4)
    plt.ylim(-0.1, 1200)
    plt.xlabel('Number of servers', fontsize=14)
    plt.xticks(np.arange(2, 18.2, step=2))
    plt.ylabel('Average Energy Consumption (mJ)', fontsize=14)
    plt.yticks(np.arange(0, 1400, step=200))
    plt.legend()
    plt.savefig("Server_vs_Energy.jpg")
    plt.show()

    print(s_CostBMOGWO)
    plt.errorbar(server, s_CostBMOGWO, color='green', label='WOLVERINE', yerr=.015, marker='+')
    plt.errorbar(server, s_CostMGBD, color='red',  label='MGBD', yerr=.021, marker='o')
    plt.errorbar(server, s_CostiRAF, color='blue', label='iRAF', yerr=.025, marker='v')
    plt.xlim(1.7, 18.4)
    plt.ylim(0.059, 0.60)
    plt.xlabel('Number of servers', fontsize=14)
    plt.xticks(np.arange(2, 18.4, step=2))
    plt.ylabel('Average Normalized Savings', fontsize=14)
    plt.yticks(np.arange(0, 0.60, step=.1))
    plt.legend()
    plt.savefig("Server_vs_Savings.jpg")
    plt.show()

    plt.errorbar(server, s_TCRBMOGWO, color='green', label='WOLVERINE', yerr=.001, marker='+')
    plt.errorbar(server, s_TCRMGBD, color='red', label='MGBD', yerr=.0021, marker='o')
    plt.errorbar(server, s_TCRiRAF, color='blue', label='iRAF', yerr=.0025, marker='v')
    plt.xlim(1.7, 18.4)
    plt.ylim(0.059, 0.5)
    plt.xlabel('Number of servers', fontsize=14)
    plt.xticks(np.arange(2, 18.4, step=2))
    plt.ylabel('Task Drop Ratio', fontsize=14)
    plt.yticks(np.arange(0,0.6, step=.1))
    plt.legend()
    plt.savefig("Server_vs_TCR.jpg")
    plt.show()


def cached_or_not():
    plt.errorbar(cycle, cycle_LatencyBMOGWO, color='dodgerblue', label='WOLVERINE', yerr=2.4, marker='x')
    plt.errorbar(cycle, cycle_LatencyNoCaching, color='darkorange', linestyle='dashed', label='No caching+offloading', yerr =4.6, marker='d')
    plt.xlim(-.01, 3.1)
    plt.ylim(1, 12000)
    plt.xlabel('Average computation per task (gigacycles)', fontsize=14)
    plt.xticks(np.arange(0, 3.02, step=.5))
    plt.ylabel('Average Latency (ms)', fontsize=14)
    plt.yticks(np.arange(0, 12000, step=2000))
    plt.legend()
    plt.savefig("Cached_Latency.jpg")
    plt.show()

    plt.errorbar(cycle, cycle_EnergyBMOGWO, color='dodgerblue',label='WOLVERINE', yerr=.4 ,  marker='x')
    plt.errorbar(cycle, cycle_EnergyNoCaching, color='darkorange',linestyle='dashed', label='No caching+offloading', yerr=.7,  marker='d')
    plt.xlim(-.01, 3.1)
    plt.ylim(-.1, 1000)
    plt.xlabel('Average computation per task (gigacycles)', fontsize=14)
    plt.xticks(np.arange(0, 3.02, step=.5))
    plt.ylabel('Average Energy consumption (J)', fontsize=14)
    plt.yticks(np.arange(0, 1000, step=200))
    plt.legend()
    plt.savefig("Cached_Energy.jpg")
    plt.show()

    plt.errorbar(cycle, cycle_CostBMOGWO, color='dodgerblue', label='WOLVERINE', yerr=.04, marker='x')
    plt.errorbar(cycle, cycle_CostNoCaching, color='darkorange', linestyle='dashed', label='No caching+offloading', yerr=.07, marker='d')
    plt.xlim(-.01, 3.1)
    plt.ylim(-.01, 1)
    plt.xlabel('Average computation per task (gigacycles)', fontsize=14)
    plt.xticks(np.arange(0, 3.02, step=.5))
    plt.ylabel('Average Normalized Savings', fontsize=14)
    plt.yticks(np.arange(0, 1.01, step=.2))
    plt.legend()
    plt.savefig("Cached_Savings.jpg")
    plt.show()

    plt.errorbar(cycle, cycle_TCRBMOGWO, color='dodgerblue', label='WOLVERINE', yerr=.04, marker='x')
    plt.errorbar(cycle, cycle_TCRNoCaching, color='darkorange', linestyle='dashed', label='No caching+offloading',
                 yerr=.07, marker='d')
    plt.xlim(-.01, 3.1)
    plt.ylim(-.01, 0.6)
    plt.xlabel('Average computation per task (gigacycles)', fontsize=14)
    plt.xticks(np.arange(0, 3.02, step=.5))
    plt.ylabel('Task Drop Ratio', fontsize=14)
    plt.yticks(np.arange(0, 0.6, step=.2))
    plt.legend()
    plt.savefig("Cached_Cost.jpg")
    plt.show()


#task_graph()
# server_graph()
cached_or_not()

