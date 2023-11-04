import csv
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt10
import matplotlib.pyplot as plt11
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4
import matplotlib.pyplot as plt5
import matplotlib.pyplot as plt6
import matplotlib.pyplot as plt7
import matplotlib.pyplot as plt8
import matplotlib.pyplot as plt9
import numpy as np

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
s_QoeMoeaD = []

s_EnergyBMOGWO = []
s_EnergyMGBD = []
s_EnergyiRAF = []
s_EnergyMoeaD = []

s_CostMoeaD = []
s_CostBMOGWO = []
s_CostMGBD = []
s_CostiRAF = []

s_IGDMoeaD=[]
s_IGDMOGWO=[]
s_IgdBat=[]

s_population_igd=[]
s_population_hpv=[]

s_HypoeaD=[]
s_hypMOGWO=[]
s_hypBat=[]

s_IgdBPSO=[]


archive_size=[]
population_size=[]
s_archive_igd=[]
s_archive_hpv=[]


s_TCRMoeaD = []
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
        print("Row : ",row)
        server.append(int(row[0]))

        s_QoeBMOGWO.append(float(row[9]))
        s_EnergyBMOGWO.append(float(row[10]))
        s_CostBMOGWO.append(float(row[11]))
        s_TCRBMOGWO.append(float(row[12]))

        s_QoeMGBD.append(float(row[5]))
        s_EnergyMGBD.append(float(row[6]))
        s_CostMGBD.append(float(row[7]))
        s_TCRMGBD.append(float(row[8]))

        s_QoeiRAF.append(float(row[1]))
        s_EnergyiRAF.append(float(row[2]))
        s_CostiRAF.append(float(row[3]))
        s_TCRiRAF.append(float(row[4]))

        s_QoeMoeaD.append(float(row[13]))
        s_EnergyMoeaD.append(float(row[14]))
        s_CostMoeaD.append(float(row[15]))
        s_TCRMoeaD.append(float(row[16]))


with open('igd_hypval_server.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        print("Row : ",row)
        #server.append(int(row[0]))
        s_IGDMoeaD.append(float(row[5]))
        s_IGDMOGWO.append(float(row[4]))
        s_IgdBat.append(float(row[6]))

        s_hypMOGWO.append(float(row[1]))
        s_HypoeaD.append(float(row[2]))
        s_hypBat.append(float(row[3]))


with open('file_3_cached.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        # print(row)
        cycle.append(float(row[0]))
        cycle_LatencyBMOGWO.append(float(row[5]))
        cycle_EnergyBMOGWO.append(float(row[6]))
        cycle_CostBMOGWO.append(float(row[7]))
        cycle_TCRBMOGWO.append(float(row[8]))
        cycle_LatencyNoCaching.append(float(row[1]))
        cycle_EnergyNoCaching.append(float(row[2]))
        cycle_CostNoCaching.append(float(row[3]))
        cycle_TCRNoCaching.append(float(row[4]))
with open('ablation.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        archive_size.append(int(row[0]))
        s_archive_igd.append(float(row[1]))
        s_archive_hpv.append(float(row[2]))
with open('ablation_population.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        population_size.append(int(row[0]))
        s_population_igd.append(float(row[1]))
        s_population_hpv.append(float(row[2]))


def task_graph():
    plt.errorbar(user, QoeBMOGWO, color='green', label='WOLVERINE', yerr=10, marker='+')
    plt.errorbar(user, QoeBMOGWO, color='purple', label='WOLVERINE', yerr=10, marker='+')
    plt.errorbar(user, QoeMGBD, color='red', label='MGBD', yerr=15, marker='o')
    plt.errorbar(user, QoeiRAF, color='blue', label='iRAF', yerr=15, marker='v')
    plt.xlim(2, 270)
    plt.ylim(-.01, 301)
    plt.xlabel('Number of tasks', fontsize=14)
    plt.xticks(np.arange(10, 261, step=50))
    plt.ylabel('Average Latency (ms)', fontsize=14)
    plt.yticks(np.arange(0, 301, step=50))
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
    plt.savefig("Task_vs_Savings.jpg")
    plt.show()


def server_graph():
    plt.errorbar(server, s_QoeBMOGWO, color='green', label='WOLVERINE', yerr=0.33, marker='+')
    plt.errorbar(server, s_QoeMoeaD, color='purple', label='MOEA/D', yerr=0.40, marker='*')
    plt.errorbar(server, s_QoeMGBD, color='red', label='MGBD', yerr=0.43, marker='o')
    plt.errorbar(server, s_QoeiRAF, color='blue', label='iRAF', yerr=0.45, marker='v')
    plt.xlim(5.6, 18.4)
    plt.ylim(-0.1, 4.1)
    plt.xlabel('Number of servers', fontsize=16)
    plt.xticks(np.arange(6, 18.2, step=2))
    plt.ylabel('Average Latency (s)', fontsize=16)
    plt.yticks(np.arange(0, 4.1, step=.5))
    plt.legend()
    plt.savefig("Server_vs_Latency.jpg")
    plt.show()

    plt.errorbar(server, s_EnergyBMOGWO, color='green', label='WOLVERINE', yerr=20, marker='+')
    plt.errorbar(server, s_EnergyMoeaD, color='purple', label='MOEA/D', yerr=30, marker='*')
    plt.errorbar(server, s_EnergyMGBD, color='red', label='MGBD', yerr=33, marker='o')
    plt.errorbar(server, s_EnergyiRAF, color='blue', label='iRAF', yerr=35, marker='v')
    plt.xlim(5.6, 18.4)
    plt.ylim(-0.1, 501)
    plt.xlabel('Number of servers', fontsize=16)
    plt.xticks(np.arange(6, 18.2, step=2))
    plt.ylabel('Average Energy Consumption (mJ)', fontsize=16)
    plt.yticks(np.arange(0, 501, step=50))
    plt.legend()
    plt.savefig("Server_vs_Energy.jpg")
    plt.show()

    plt.errorbar(server, s_CostBMOGWO, color='green', label='WOLVERINE', yerr=.038, marker='+')
    plt.errorbar(server, s_CostMoeaD, color='purple', label='MOEA/D', yerr=.046, marker='*')
    plt.errorbar(server, s_CostMGBD, color='red', label='MGBD', yerr=.059, marker='o')
    plt.errorbar(server, s_CostiRAF, color='blue', label='iRAF', yerr=.065, marker='v')
    plt.xlim(5.6, 18.4)
    plt.ylim(0.29, 1.01)
    plt.xlabel('Number of servers', fontsize=16)
    plt.xticks(np.arange(6, 18.4, step=2))
    plt.ylabel('Average Normalized Savings', fontsize=16)
    plt.yticks(np.arange(.3, 1.01, step=.1))
    plt.legend()
    plt.savefig("Server_vs_Savings.jpg")
    plt.show()

    plt.errorbar(server, s_TCRBMOGWO, color='green', label='WOLVERINE', yerr=.042, marker='+')
    plt.errorbar(server, s_TCRMoeaD, color='purple', label='MOEA/D', yerr=.048, marker='*')
    plt.errorbar(server, s_TCRMGBD, color='red', label='MGBD', yerr=.053, marker='o')
    plt.errorbar(server, s_TCRiRAF, color='blue', label='iRAF', yerr=.058, marker='v')
    plt.xlim(5.7, 18.4)
    plt.ylim(.29, 1)
    plt.xlabel('Number of servers', fontsize=18)
    plt.xticks(np.arange(6, 18.4, step=2))
    plt.ylabel('Task Completion Reliability', fontsize=18)
    plt.yticks(np.arange(.3, 1.01, step=.1))
    plt.legend()
    plt.savefig("Server_vs_TCR.jpg")
    plt.show()


def cached_or_not():
    plt.errorbar(cycle, cycle_LatencyBMOGWO, color='dodgerblue', label='WOLVERINE', yerr=.073, marker='x')
    plt.errorbar(cycle, cycle_LatencyNoCaching, color='darkorange', linestyle='dashed', label='No caching+offloading',
                 yerr=.1, marker='d')
    plt.xlim(-.01, 3.1)
    plt.ylim(1, 2.01)
    plt.xlabel('Average computation per task (gigacycles)', fontsize=18)
    plt.xticks(np.arange(0, 3.02, step=.5))
    plt.ylabel('Average Latency (s)', fontsize=18)
    plt.yticks(np.arange(0, 2.01, step=.4))
    plt.legend()
    plt.savefig("Cached_Latency.jpg")
    plt.show()

    plt.errorbar(cycle, cycle_EnergyBMOGWO, color='dodgerblue', label='WOLVERINE', yerr=25, marker='x')
    plt.errorbar(cycle, cycle_EnergyNoCaching, color='darkorange', linestyle='dashed', label='No caching+offloading',
                 yerr=35, marker='d')
    plt.xlim(-.01, 3.1)
    plt.ylim(-.1, 801)
    plt.xlabel('Average computation per task (gigacycles)', fontsize=18)
    plt.xticks(np.arange(0, 3.02, step=.5))
    plt.ylabel('Average Energy consumption (mJ)', fontsize=18)
    plt.yticks(np.arange(0, 801, step=100))
    plt.legend()
    plt.savefig("Cached_Energy.jpg")
    plt.show()

    plt.errorbar(cycle, cycle_CostBMOGWO, color='dodgerblue', label='WOLVERINE', yerr=.038, marker='x', fontsize=12)
    plt.errorbar(cycle, cycle_CostNoCaching, color='darkorange', linestyle='dashed', label='No caching+offloading',
                 yerr=.055, marker='d')
    plt.xlim(-.01, 3.1)
    plt.ylim(-.01, 1)
    plt.xlabel('Average computation per task (gigacycles)', fontsize=18)
    plt.xticks(np.arange(0, 3.02, step=.5))
    plt.ylabel('Average Normalized Savings', fontsize=18)
    plt.yticks(np.arange(0, 1.01, step=.2))
    plt.legend()
    plt.savefig("Cached_Savings.jpg")
    plt.show()

    plt.errorbar(cycle, cycle_TCRBMOGWO, color='dodgerblue', label='WOLVERINE', yerr=.018, marker='x')
    plt.errorbar(cycle, cycle_TCRNoCaching, color='darkorange', linestyle='dashed', label='No caching+offloading',
                 yerr=.028, marker='d')
    plt.xlim(-.01, 3.1)
    plt.ylim(.9, 1)
    plt.xlabel('Average computation per task (gigacycles)', fontsize=18)
    plt.xticks(np.arange(0, 3.02, step=.5))
    plt.ylabel('Task Completion Reliability', fontsize=18)
    plt.yticks(np.arange(.5, 1.01, step=.1))
    plt.legend()
    plt.savefig("Cached_TCR.jpg")
    plt.show()


def igd_graph():
    print(server)
    print(s_IGDMOGWO)
    plt.errorbar(server, s_IGDMOGWO, color='green', label='WOLVERINE', yerr=0.25, marker='+')
    plt.errorbar(server, s_IGDMoeaD, color='purple', label='MOEA/D', yerr=0.32, marker='*')
    plt.errorbar(server, s_IgdBat, color='red', label='BAT', yerr=0.35, marker='o')

    plt.xlim(5.6, 18.4)
    plt.ylim(-0.1, 4.1)
    plt.xlabel('Number of servers', fontsize=14)
    plt.xticks(np.arange(6, 18.2, step=2))
    plt.ylabel('IGD', fontsize=14)
    plt.yticks(np.arange(0, 5, step=.5))
    plt.legend()
    plt.savefig("Server_vs_IGD.jpg")
    plt.show()

    plt.errorbar(server, s_hypMOGWO, color='green', label='WOLVERINE', yerr=1.5, marker='+')
    plt.errorbar(server, s_HypoeaD, color='purple', label='MOEA/D', yerr=1.9, marker='*')
    plt.errorbar(server, s_hypBat, color='red', label='BAT', yerr=2.1, marker='o')

    plt.xlim(5.6, 18.4)
    plt.ylim(0.1, 25.1)
    plt.xlabel('Number of servers', fontsize=14)
    plt.xticks(np.arange(6, 18.2, step=2))
    plt.ylabel('Hypervolume', fontsize=14)
    plt.yticks(np.arange(0, 40, step=5))
    plt.legend()
    plt.savefig("Server_vs_hypval.jpg")
    plt.show()


def ablation_archive():
    print(server)
    print(s_IGDMOGWO)
    #plt.errorbar(archive_size, s_archive_hpv, color='green', label='WOLVERINE', yerr=0.25, marker='+')
    plt.errorbar(archive_size, s_archive_igd, color='purple', yerr=0.32, marker='*')

    plt.xlim(100.6,500.6)
    plt.ylim(-0.1, 4.1)
    plt.xlabel('Size of Archive', fontsize=14)
    plt.xticks(np.arange(50, 550, step=50))
    plt.ylabel('Inverted Generational Distance (IGD)', fontsize=18)
    plt.yticks(np.arange(0, 5, step=.5))
    plt.legend()
    plt.savefig("Archive_vs_IGD.jpg")
    plt.show()

    plt.errorbar(archive_size, s_archive_hpv, color='green', yerr=1.2, marker='*')

    plt.xlim(100.6, 500.6)
    plt.ylim(0.1, 25.1)
    plt.xlabel('Size of Archive', fontsize=14)
    plt.xticks(np.arange(50, 550, step=50))
    plt.ylabel('Hypervolume', fontsize=18)
    plt.yticks(np.arange(0, 25, step=5))
    plt.legend()
    plt.savefig("Archive_vs_HyperVolume.jpg")
    plt.show()
    # plt.errorbar(server, s_hypMOGWO, color='green', label='WOLVERINE', yerr=1.5, marker='+')
    # plt.errorbar(server, s_HypoeaD, color='purple', label='MOEA/D', yerr=1.9, marker='*')
    # plt.errorbar(server, s_hypBat, color='red', label='BAT', yerr=2.1, marker='o')
    #
    # plt.xlim(5.6, 18.4)
    # plt.ylim(0.1, 25.1)
    # plt.xlabel('Number of servers', fontsize=14)
    # plt.xticks(np.arange(6, 18.2, step=2))
    # plt.ylabel('Hypervolume', fontsize=14)
    # plt.yticks(np.arange(0, 40, step=5))
    # plt.legend()
    # plt.savefig("Server_vs_hypval.jpg")
    # plt.show()
    #

def ablation_population():
    print(server)
    print(s_IGDMOGWO)
    #plt.errorbar(archive_size, s_archive_hpv, color='green', label='WOLVERINE', yerr=0.25, marker='+')
    plt.errorbar(population_size, s_population_igd, color='blue', yerr=0.32, marker='*')

    plt.xlim(100.6,500.6)
    plt.ylim(-0.1, 4.1)
    plt.xlabel('Size of Population', fontsize=14)
    plt.xticks(np.arange(50, 550, step=50))
    plt.ylabel('Inverted Generational Distance (IGD)', fontsize=14)
    plt.yticks(np.arange(0, 5, step=.5))
    plt.legend()
    plt.savefig("Population_vs_IGD.jpg")
    plt.show()

    plt.errorbar(population_size,s_population_hpv, color='red', yerr=1.2, marker='*')

    plt.xlim(100.6, 500.6)
    plt.ylim(0.1, 25.1)
    plt.xlabel('Size of Population', fontsize=14)
    plt.xticks(np.arange(50, 550, step=50))
    plt.ylabel('Hypervolume', fontsize=14)
    plt.yticks(np.arange(0, 25, step=5))
    plt.legend()
    plt.savefig("Population_vs_HyperVolume.jpg")
    plt.show()

#task_graph()
#server_graph()
# igd_graph()
# ablation_archive()
# ablation_population()
cached_or_not()
