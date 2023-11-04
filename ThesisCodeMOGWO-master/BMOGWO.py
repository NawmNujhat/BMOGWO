import numpy as np
import random
import math
import time
import pprint
import matplotlib.pyplot


dim = 4  # Number of variable

wolf = 10  # Search agent number
tau = 4  # number of tasks
E = 3  # number of Edge server
Max_Iter = 50  # number of maximum iteration
Archive_size = 5  # maximum capacity of Archive
nGrid = 10  # Number of grid per dimension

fitness = []  # list of fitness values(time, energy, cost, serial) for all search agents
Archive = []  # Archive implemented as a list which contains fitness values(time, energy, cost, serial) of
              # non-dominated solutions


# structure of a wolf
class structure:
    def __init__(self):
        self.time = 0
        self.energy = 0
        self.cost = 0
        self.serial = None

    # function needed for printing a list of class objects
    def __repr__(self):
        return "time: % s energy: % s cost: % s serial: % s" % (self.time, self.energy, self.cost, self.serial)


# calculating fitness for each search agent/solution
def calculate_fitness(P, w):
    total_time = [[a * b for a, b in zip(i, j)] for i, j in zip(P[w], Tij)]
    total_energy = [[a * b for a, b in zip(i, j)] for i, j in zip(P[w], Eij)]
    total_cost = [[a * b for a, b in zip(i, j)] for i, j in zip(P[w], Cij)]
    return sum(list(map(sum, total_time))), sum(list(map(sum, total_energy))), sum(list(map(sum, total_cost)))


# roulette wheel selection function, only needed for choosing leaders
def roulette_wheel_selection(index, probability, grid):
    box = []
    sum_of_probability = sum(probability)
    # print("index: " + str(index))
    # print("probability: " + str(probability))
    q = []
    for i in range(len(probability)):
        if i == 0:
            q.append(probability[i])
        else:
            q.append(q[i - 1] + probability[i])

    r = random.uniform(0, sum_of_probability)
    for i in range(len(probability)):
        if r <= q[0]:
            box = index[0]
        elif q[i - 1] < r < q[i]:
            box = index[i]
    return box  # return the index number of the segment/cube containing the leader


def leader_selection(grid):
    index = []
    probability = []

    # leader selection:
    for k in range(10):
        for i in range(10):
            for j in range(10):
                if len(grid[k][i][j]) > 0:
                    index.append([k, i, j])
                    probability.append(1 / len(grid[k][i][j]))

    # selecting alpha
    box_1 = roulette_wheel_selection(index, probability, grid)
    # size = len(grid[box_1[0]] [box_1[1]] [box_1[2]])
    alpha = random.choice(grid[box_1[0]][box_1[1]][box_1[2]])
    grid[box_1[0]][box_1[1]][box_1[2]].remove(alpha)
    # print(len(grid[box_1[0]][box_1[1]][box_1[2]]))

    # selecting beta from box_1
    if len(grid[box_1[0]][box_1[1]][box_1[2]]) > 0:
        beta = random.choice(grid[box_1[0]][box_1[1]][box_1[2]])
        grid[box_1[0]][box_1[1]][box_1[2]].remove(beta)

        # selecting delta from box_1
        if len(grid[box_1[0]][box_1[1]][box_1[2]]) > 0:
            delta = random.choice(grid[box_1[0]][box_1[1]][box_1[2]])
        # selecting delta from box_2
        else:
            # deltar jonno abar roulette_wheel_selection call dite hobe
            index = []
            probability = []

            # leader selection:
            for k in range(10):
                for i in range(10):
                    for j in range(10):
                        if len(grid[k][i][j]) > 0:
                            index.append([k, i, j])
                            probability.append(1 / len(grid[k][i][j]))
            box_2 = roulette_wheel_selection(index, probability, grid)
            delta = random.choice(grid[box_2[0]][box_2[1]][box_2[2]])

    # selecting beta from box_2
    else:
        index.clear()
        probability.clear()

        # leader selection:
        for k in range(10):
            for i in range(10):
                for j in range(10):
                    if len(grid[k][i][j]) > 0:
                        index.append([k, i, j])
                        probability.append(1 / len(grid[k][i][j]))

        box_2 = roulette_wheel_selection(index, probability, grid)
        beta = random.choice(grid[box_2[0]][box_2[1]][box_2[2]])
        grid[box_2[0]][box_2[1]][box_2[2]].remove(beta)

        # selcting delta from box_2
        if len(grid[box_2[0]][box_2[1]][box_2[2]]) > 0:
            delta = random.choice(grid[box_2[0]][box_2[1]][box_2[2]])
        # selcting delta from box_3
        else:
            index = []
            probability = []

            # leader selection:
            for k in range(10):
                for i in range(10):
                    for j in range(10):
                        if len(grid[k][i][j]) > 0:
                            index.append([k, i, j])
                            probability.append(1 / len(grid[k][i][j]))
            box_3 = roulette_wheel_selection(index, probability, grid)
            delta = random.choice(grid[box_3[0]][box_3[1]][box_3[2]])
    # print("alpha, beta, delta = " + str(alpha) + str(beta) + str( delta))
    return alpha, beta, delta  # Returned indices of alpha, beta, delta in Archive (not in total population)


def grid_mecha_for_leader():
    grid = [[[0 for j in range(10)] for i in range(10)] for w in range(10)]
    for k in range(10):
        for i in range(10):
            for j in range(10):
                l = []
                grid[k][i][j] = l

    for i in range(len(Archive)):
        posX = int((Archive[i].time - 1) / 39)
        posY = int((Archive[i].energy - 1) / 39)
        posZ = int((Archive[i].cost - 1) / 39)
        grid[posX][posY][posZ].append(i)

    alpha_index, beta_index, delta_index = leader_selection(grid)
    # print(alpha_index, beta_index, delta_index)
    return Archive[alpha_index].serial, Archive[beta_index].serial, Archive[delta_index].serial


def grid_mecha_for_deletion(w):
    grid = [[[0 for j in range(10)] for i in range(10)] for w in range(10)]
    for k in range(10):
        for i in range(10):
            for j in range(10):
                l = []
                grid[k][i][j] = l
    for i in range(len(Archive)):
        posX = int((Archive[i].time - 1) / 39)
        posY = int((Archive[i].energy - 1) / 39)
        posZ = int((Archive[i].cost - 1) / 39)
        grid[posX][posY][posZ].append(i)

    most_crowded = 0
    for k in range(10):
        for i in range(10):
            for j in range(10):
                if (len(grid[k][i][j]) > 0):
                    if len(grid[k][i][j]) > most_crowded:
                        most_crowded = len(grid[k][i][j])
                        ke = k
                        ai = i
                        je = j

    ar = random.choice(grid[ke][ai][je])
    del Archive[ar]
    grid[ke][ai][je].remove(ar)

    l = len(Archive)
    Archive.append(structure())
    Archive[l].time, Archive[l].energy, Archive[l].cost, Archive[l].serial = fitness[w].time, fitness[w].energy, \
                                                                             fitness[w].cost, fitness[w].serial

    # pprint.pprint(grid)
    return


# algorithm 3
def algorithm_3(omega, w):
    for i in reversed(range(len(omega))):  # line 1
        del Archive[omega[i]]  # line 2

    if len(Archive) < Archive_size:  # line 4
        l = len(Archive)
        Archive.append(structure())  # making room for adding newly come non-dominated solution
        Archive[l].time, Archive[l].energy, Archive[l].cost, Archive[l].serial = fitness[w].time, fitness[w].energy, \
                                                                                 fitness[w].cost, fitness[
                                                                                     w].serial  # line 5

    elif len(Archive) == Archive_size:  # line 6
        grid_mecha_for_deletion(w)
    return


# algorithm 2
def algorithm_2(fitness):
    for w in range(wolf):  # line 1
        omega = []  # line 2
        count = 0  # line 3
        if len(Archive) == 0:  # adding 1st value to fully blank archive
            # print(len(Archive))
            l = len(Archive)
            Archive.append(structure())
            # print(len(Archive))
            Archive[l].time, Archive[l].energy, Archive[l].cost, Archive[l].serial = fitness[w].time, fitness[w].energy, \
                                                                                     fitness[w].cost, fitness[w].serial

        else:  # if there is already some value in Archive
            for rho in range(len(Archive)):  # line 4
                if ((fitness[w].time < Archive[rho].time) & (fitness[w].energy <= Archive[rho].energy) & (
                        fitness[w].cost <= Archive[rho].cost)) or \
                        ((fitness[w].time <= Archive[rho].time) & (fitness[w].energy < Archive[rho].energy) & (
                                fitness[w].cost <= Archive[rho].cost)) or \
                        ((fitness[w].time <= Archive[rho].time) & (fitness[w].energy <= Archive[rho].energy) & (
                                fitness[w].cost < Archive[rho].cost)):  # line 5
                    omega.append(rho)  # line 6

                elif ((Archive[rho].time < fitness[w].time) & (Archive[rho].energy <= fitness[w].energy) & (
                        Archive[rho].cost <= fitness[w].cost)) or \
                        ((Archive[rho].time <= fitness[w].time) & (Archive[rho].energy < fitness[w].energy) & (
                                Archive[rho].cost <= fitness[w].cost)) or \
                        ((Archive[rho].time <= fitness[w].time) & (Archive[rho].energy <= fitness[w].energy) & (
                                Archive[rho].cost < fitness[w].cost)):  # line 7
                    count += 1  # line 8

            if count == 0:  # line 11 # if w is a non-dominated solution
                algorithm_3(omega, w)  # line 12
    return


# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================


P = [[[0 for j in range(E)] for i in range(tau)] for w in range(wolf)]
print(P)
Tij = [[random.uniform(1, 100) for j in range(E)] for i in range(tau)]
Eij = [[random.uniform(1, 100) for j in range(E)] for i in range(tau)]
Cij = [[random.uniform(1, 100) for j in range(E)] for i in range(tau)]
# time_fitness = [float('inf') for w in range(wolf)]


# line 3-6
for w in range(wolf):
    for i in range(tau):
        rand = random.randint(0, (E - 1))
        P[w][i][rand] = 1  # line 4

    fitness.append(structure())
    fitness[w].time, fitness[w].energy, fitness[w].cost = calculate_fitness(P, w)  # line 5
    fitness[w].serial = w

# line 7 (Finding non-dominated solutions using algo 2 & 3)
algorithm_2(fitness)
# pprint.pprint(Archive)

# line 8 (leader selection, here alpha beta delta are the positions/index number of wolfs in total population)
Alpha_serial, Beta_serial, Delta_serial = grid_mecha_for_leader()

# print("Alpha: " + str(Alpha_serial))
# print("Beta: " + str(Beta_serial))
# print("Delta: " + str(Delta_serial))
print("Initial random population:=========================================================")
pprint.pprint(len(P))
print()

Alpha = P[Alpha_serial]
Beta = P[Beta_serial]
Delta = P[Delta_serial]
#
# print("Alpha serial & Alpha:===============================================")
# print(Alpha_serial, Alpha)
# print("Beta serial & Beta:=================================================")
# print(Beta_serial, Beta)
# print("Delta serial & Delta:===============================================")
# print(Delta_serial, Delta)
# print()


# line 9 (iteration er loop)
for it in range(1, Max_Iter + 1):
    # print()
    # print("Iteration number: " + str(it))
    a = 2 - (it * (2 / Max_Iter))  # initializing parameter 'a'

    for w in range(wolf):  # line 10 - proti wolf er jonno iteration
        C1 = 2 * random.uniform(0, 1)  # eqn-41 from my paper
        C2 = 2 * random.uniform(0, 1)  # eqn-41 from my paper
        C3 = 2 * random.uniform(0, 1)  # eqn-41 from my paper
        A1 = (2 * a * random.uniform(0, 1)) - a  # eqn-45 from my paper
        A2 = (2 * a * random.uniform(0, 1)) - a  # eqn-45 from my paper
        A3 = (2 * a * random.uniform(0, 1)) - a  # eqn-45 from my paper
        # print("A1, A2, A3: ================================================")
        # print((A1, A2, A3))
        # print()
        # print("C1, C2, C3: ================================================")
        # print((C1, C2, C3))
        # print()
        for i in range(tau):  # line 11
            for j in range(E):  # line 11
                D_alpha = abs((C1 * Alpha[i][j]) - P[w][i][j])
                D_beta = abs((C1 * Beta[i][j]) - P[w][i][j])
                D_delta = abs((C1 * Delta[i][j]) - P[w][i][j])

                x1 = Alpha[i][j] - (A1 * D_alpha)  # eqn-42
                x2 = Beta[i][j] - (A1 * D_beta)  # eqn-43
                x3 = Delta[i][j] - (A1 * D_delta)  # eqn-44

                x = (x1 + x2 + x3) / 3  # eqn-46 from my paper
                # sigmoid function:
                sig = 1 / (1 + np.exp(-x))
                if sig >= random.uniform(0, 1):
                    x = 1
                else:
                    x = 0
                P[w][i][j] = x

    # again calculating fitness values of all solutions
    fitness.clear()
    for w in range(wolf):
        fitness.append(structure())
        fitness[w].time, fitness[w].energy, fitness[w].cost = calculate_fitness(P, w)  # line 5
        fitness[w].serial = w

    pprint.pprint(fitness)
    print()

    # line 19
    algorithm_2(fitness)

    Alpha_serial, Beta_serial, Delta_serial = grid_mecha_for_leader()
    Alpha = P[Alpha_serial]
    Beta = P[Beta_serial]
    Delta = P[Delta_serial]
# population after update
print("Population after update:=========================================================")
pprint.pprint(P)
