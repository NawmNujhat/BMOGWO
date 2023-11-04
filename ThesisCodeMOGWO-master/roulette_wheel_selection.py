import pprint
wolf = 5
class structure:
    def __init__(self):
        self.time = 0
        self.energy = 0
        self.cost = 0
        self.serial = -1
        # self.dominated = False

    def __repr__(self):
        return "time: % s energy: % s cost: % s serial: % s" % (self.time, self.energy, self.cost, self.serial)

fitness = []

for w in range(wolf):
    fitness.append(structure())
    fitness[w].time, fitness[w].energy, fitness[w].cost = 1, 10, 100 # line 5
    fitness[w].serial = w
    print("time: ")
    print(fitness[w].time)
    print("serial: ")
    print(fitness[w].serial)
    # print()
print("fitness: ")
pprint.pprint(fitness)