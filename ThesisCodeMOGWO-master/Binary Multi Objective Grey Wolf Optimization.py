#!/usr/bin/env python
# coding: utf-8

# In[3039]:
import random

from pymoo.indicators.hv import Hypervolume
import numpy as np 
import random as r
import itertools as it
import math
from scipy.spatial import distance


# In[3040]:

Tasks=0
Servers=0

tasks_cached=np.array([])
power=np.array([])
data_input=np.array([])
rayleigh_channel=np.array([])
datacode=np.array([])
meu = np.array([])
c = np.array([])
f = np.array([])
costs_per_cycle= np.array([])
costs_per_unit=np.array([])

def innnit():
    print("Please Enter Task")
    Tasks=int(input())
    print("Please Enter Servers")
    Servers=int(input())
    global h,No,c,f,meu,meu_servers,bandwidth,c_servers,power,data_input,datacode,costs_per_cycle,costs_per_unit,tasks_cached,rayleigh_channel
    c = np.random.randint((6 * pow(10, 9)), (9 * pow(10, 10)), (1, Tasks))
    f = np.random.randint((300 * pow(10, 6)), (500 * pow(10, 6)), (1, Tasks))
    meu = np.random.uniform(low=0.0, high=1.0, size=(1, Tasks))
    meu_servers = np.array([])
    meu_servers = np.random.uniform(low=0.0, high=1.0, size=(1, Servers))
    bandwidth = np.random.uniform((0.5 * pow(10, 6)), (2.00001 * pow(10, 6)), (1, Tasks))
    c_servers = np.random.uniform((3.19 * pow(10, 9)), (19.15 * pow(10, 9)), (1, Servers))
    power = np.random.uniform((32 * pow(10, -3)), (198 * pow(10, -3)), (1, Tasks))
    data_input = np.random.uniform((200 * pow(10, -3)), (4 * pow(10, 3)), (1, Tasks))
    datacode = np.random.uniform((200 * pow(10, 3)), (4 * pow(10, 6)), (1, Tasks))
    costs_per_cycle = np.random.randint(2, 10, (1, Servers))
    costs_per_unit = np.random.randint(2, 8, (1, Servers))
    tasks_cached = np.random.randint(0, 2, (1, Tasks))
    h = np.random.randint(12000, 15000, (1, Tasks))
    No = 30
    rayleigh_channel = np.random.uniform((0.1 * pow(10, 3)), (4 * pow(10, 1)), (1, Tasks))
    return Tasks,Servers


def initialize_random_position_vector(Tasks,Servers,max_iter):
    #max_iter_pop=400
    population=[]
    for k in range(0,max_iter):
        X=np.zeros((Tasks,Servers))
        for i in range(0,len(X)):
            j=r.randint(0,Servers-1)
            X[i][j]=1
        Xw=np.zeros((1,Tasks*Servers))
        for i in range(0,Tasks):
            for j in range(0,Servers):
                d=((i-1)*Servers)+j
                Xw[0][d]=X[i][j]
        population.append(Xw)

    return population
      


# In[3043]:


class solution:
    def __init__(self,xw,time,energy,cost,tasks,servers):
        self.xw=xw
        self.time=time
        self.energy=energy
        self.cost=cost
        self.tasks=tasks
        self.servers=servers
    def find_index(self,ind):
        #print(self.servers)
        i=(math.ceil(ind/self.servers))
        #print(ind)
        #print("I :",i)
        j=abs(ind-((i-1)*self.servers))
        #print(" J :",j)
        if(i==0 and j!=0):
            return i,j-1
        elif(i!=0 and j==0):
            return i-1,j
        else:
            return i-1,j-1
    def calculate_val_per_wolf(self,xw):
        s_time=0.0
        s_energy=0.0
        s_cost=0.0
        #print(len(self.xw))
        #print(self.xw.shape)
        for k in range(0,self.xw.shape[1]):
           
            if(xw[0][k]==1):
                t=0.0
                e=0.0
                c=0.0
                i,j=self.find_index(k)
                if(i==j):
                    t,e,c=self.calc_local(i,j)
            
                else:
                    t,e,c=self.calc_server(i,j)
                s_time=s_time+t
                s_energy=s_energy+e
                #print(e)
                s_cost=s_cost+c
                #print("Energy So Far :",s_energy,i,j)
        self.time,self.energy,self.cost=s_time,s_energy,s_cost
#         print("Final Time :",self.time)
        #print("Final Cost :",self.cost
        #print("Final Energy :",self.energy)
    def calc_local(self,i,j):
        t_ij= c[0][i]/(meu[0][i]*f[0][i])
        E_ij=pow(10,-26)*t_ij*pow(f[0][i],2)
        co_ij=0.00
        return t_ij,E_ij,co_ij
    def calc_server(self,i,j):
        #print(i,j)
        com_ij=math.ceil(((tasks_cached[0][i]*data_input[0][i])+((1-tasks_cached[0][i])*(data_input[0][i]+datacode[0][i])))/rayleigh_channel[0][i])
        t_ij= (c[0][i]/(meu[0][i]*f[0][i]))+com_ij
        E_ij=power[0][i]*com_ij
        #print("Power :",power[0][i])
        co_ij=(costs_per_cycle[0][j]*c[0][i])+(costs_per_unit[0][j]*datacode[0][i]*tasks_cached[0][i])
        
        return t_ij,E_ij,co_ij


# In[3044]:


def make_grid(dim_time,dim_cost,dim_energy,max_time,min_time,max_energy,min_energy,max_cost,min_cost,sol_array):
    grid=(np.zeros((400,400,400)))
    grid_index_val=list()
    dif_time=((max_time-min_time)/dim_time)
    dif_energy=((max_energy-min_energy)/dim_energy)
    dif_cost=((max_cost-min_cost)/dim_cost)
    ind_sol=0
    for i,sol in enumerate(sol_array):
        ind_time=int((int(abs(sol.time-min_time)/(dif_time+1))/100))
        ind_energy=int((int(abs(sol.energy-min_energy)/(dif_energy+1))/100))
        ind_cost=int((int(abs(sol.cost-min_cost)/(dif_cost+1))/100))
        grid[ind_time][ind_energy][ind_cost]=grid[ind_time][ind_energy][ind_cost]+1
        #print(i)
        grid_index_val.append(((ind_time,ind_energy,ind_cost),i))
    
    return grid,grid_index_val
    


# In[3045]:


def find_max_min(sol_array,P):
    max_time=-1.00
    max_energy=-1.00
    max_cost=-1.00
    min_time=100000000000
    min_energy=10000000000
    min_cost=100000000000000
    for sol in sol_array:
        if(sol.time>max_time):
            max_time=sol.time
        elif(sol.time<min_time):
            min_time=sol.time
        elif(sol.energy>max_energy):
            max_energy=sol.energy
        elif(sol.energy<min_energy):
            min_energy=sol.energy
        elif(sol.cost>max_cost):
            max_cost=sol.cost
        elif(sol.cost<min_cost):
            min_cost=sol.cost
    dim_time=int(len(P)*1.5)
    dim_cost=int(len(P)*3)
    dim_energy=int(len(P)*2)
    return max_time,min_time,max_energy,min_energy,max_cost,min_cost,dim_time,dim_cost,dim_energy


# In[3046]:


def calc_values(population,Tasks,Servers):
    sol_array=[]
    for i in range(0,len(population)):
        sol=solution(population[i],-1,-1,-1,Tasks,Servers)
        sol.calculate_val_per_wolf(sol.xw)
        sol_array.append(sol)
    return sol_array


# In[3047]:


def sigmoid(x):
    return 1 / (1 + math.exp(-(x)))


# In[3048]:


def update_position_search_agent(sol,alpha,beta,gamma,a,A,C,Tasks,Servers):
    D_alpha=abs(np.dot(alpha.xw,np.transpose(C))-sol.xw)
    X_1=alpha.xw-np.dot(alpha.xw,np.transpose(A))
    A=np.random.uniform(0,1.0001,(1,Tasks*Servers))
    C=np.random.uniform(0,2.0001,(1,Tasks*Servers))
    D_beta=abs(np.dot(beta.xw,np.transpose(C))-sol.xw)
    X_2=beta.xw-np.dot(beta.xw,np.transpose(A))
    A=np.random.uniform(0,1.0001,(1,Tasks*Servers))
    C=np.random.uniform(0,2.0001,(1,Tasks*Servers))
    D_gamma=abs(np.dot(gamma.xw,np.transpose(C))-sol.xw)
    X_3=gamma.xw-np.dot(gamma.xw,np.transpose(A))
    X=np.add(X_1,X_2,X_3)/3
    sigmoid_v = np.vectorize(sigmoid)
    return sigmoid_v(X)


# In[3049]:


def binarize(sol,Tasks):
    
    for d in range (0,len(sol[0])):
        #print(d)
        if(sol[0][d]>=r.randrange(0,1,1)):
                if(np.count_nonzero(sol==1)>=Tasks):
                    #print("No")
                     sol[0][d]=0
                else:
                    sol[0][d]=1
        else:
            sol[0][d]=0
    #print("Before ",sol[0])  
    np.random.shuffle(sol[0])
    #print("Shuffled ",sol[0])
    return sol


# In[3050]:


def update_params(Tasks,Servers):
    a=np.random.uniform(0,2.000002,(1,Tasks*Servers))
    a=a[::-1]
    C=np.random.uniform(0,2.00002,(1,Tasks*Servers))
    A=np.random.uniform(-1,1.0001,(1,Tasks*Servers))
    return a,A,C


# In[3051]:

def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

def findIgd(obtained_set, true_pareto_front):
    print(obtained_set.shape)
    print(true_pareto_front.shape)
    distances = []
    max_value=-1
    for point in obtained_set:
        val_ob=np.array([point.time,point.energy,point.cost])
        for true_point in true_pareto_front:
         val_pf= np.array([true_point.time, true_point.energy,true_point.cost])
         hyp = Hypervolume(np.array([point.time, point.energy, point.cost]))
         result = hyp.do(val_pf)
         if(result>max_value):
             max_value=result
         min_distance = min([euclidean_distance(val_ob, val_pf)])
         distances.append(min_distance)

    igd_value = np.mean(distances)
    print("Inverted Generational Distance")
    print(igd_value/1000000000000)
    print("HyperVolume")
    print(max_value/100000000000000000000)




def findHyper(true_pareto_front, sigma):
    for point in sigma:
      hyp = Hypervolume(np.array([point.time,point.energy,point.cost]))
      result = hyp.do(true_pareto_front)
    print("Hyper Volume")
    print(result)


def algorithm_2(population,sol_array,Tasks,Servers,archive):
    obtained_set=np.array([])
    max_time,min_time,max_energy,min_energy,max_cost,min_cost,dim_time,dim_cost,dim_energy=find_max_min(sol_array,population)
    for i,omega in enumerate(sol_array):
        sigma=set()
        count=0
        if not archive:
                np.append(obtained_set,np.array([omega]),axis=0)
                archive.append(omega)
                
        if archive:
            max_time,min_time,max_energy,min_energy,max_cost,min_cost,dim_time,dim_cost,dim_energy=find_max_min(sol_array,population)
            archive_grid,archive_index_val= make_grid(dim_time,dim_cost,dim_energy,max_time,min_time,max_energy,min_energy,max_cost,min_cost,archive)
        for rho in archive:
                #print(np.array([rho.time, rho.energy, rho.cost]))
                if(omega.time<rho.time and omega.energy<=rho.energy and omega.cost<=rho.cost or omega.time<=rho.time and omega.energy<=rho.energy and omega.cost<rho.cost or omega.time<=rho.time and omega.energy<rho.energy and omega.cost<=rho.cost):
                #print("Added to Sigma",i)
                    sigma.add(rho)
                elif(omega.time>rho.time and omega.energy>=rho.energy and 
                    omega.cost>=rho.cost or omega.time>=rho.time and 
                    omega.energy>=rho.energy and omega.cost>rho.cost 
                    or omega.time>=rho.time and omega.energy>rho.energy 
                    and omega.cost>=rho.cost):
                    #print(np.array([omega.time,omega.cost,omega.energy]),)
                #print("Count Increased",i)
                    count=count+1
                #print("Current Count :",count)
        if(count==0):
            #print("Run algorithm 3 for ",i)
                  archive,archive_grid,archive_index_val,true_pareto_front=algorithm_3(archive,archive_grid,sigma,omega,100,archive_index_val)

            #print("Algorithm 3 Was Successful")
    return archive,archive_grid,archive_index_val            
            


# In[3052]:


def remove_solution(archive,grid,grid_index_val):
    array_cnt=[]
    array_prob=[]
    origin=(0,0,0)
    max_val=-1
    array_seg_map=dict()
    for val in range (0,len(grid_index_val)):
        dis_origin=int(distance.euclidean((origin),(grid_index_val[val][0])))
        indices= list(grid_index_val[val][0])
        find_cnt=grid[indices[0]][indices[1]][indices[2]]
        array_cnt.append((find_cnt,indices))
    #print(array_cnt)
    for i in range (0,len(array_cnt)):
        if(max_val<array_cnt[i][0]):
            max_val=array_cnt[i][0]
    for i in range (0,len(array_cnt)):
        a=array_cnt[i][0]/max_val
        array_seg_map[str(array_cnt[i])]=a
    remove_sol=(max(array_seg_map,key=array_seg_map.get))
    t1=0
    t2=0
    for s in range (0,len(remove_sol)):
        if(remove_sol[s]=='['):
            t1=s
        if(remove_sol[s]==']'):  
            t2=s
    remove_sol=list(remove_sol[t1+1:t2].split(","))
    remove_sol=list(map(int,remove_sol))
    i=int(remove_sol[0])
    j=int(remove_sol[1])
    k=int(remove_sol[2])
    grid[i][j][k]=grid[i][j][k]-1
    for ind in grid_index_val:
        if(ind[0]==(i,j,k)):
            print(ind[1])
            grid_index_val.remove(ind)
            #print(archive[ind[1]])
            archive.remove(archive[ind[1]])
    #print("Grid : ",grid_index_val)
    #print("Archive : ",archive)
    return archive,grid,grid_index_val


# In[3053]:


def roulette_wheel_selection(archive,array_prob):
    rn=r.random()
    for i,individual in enumerate(archive):
        #print("Individual :",individual.xw)
        if(rn<=array_prob[i]):
            #print("Probability :",array_prob[i])
            return individual
        


# In[3054]:


def select_leader(archive,grid,grid_index_val):
    array_cnt=[]
    array_prob=[0]*300
    origin=(0,0,0)
    array_seg_map=dict()
    for val in range (0,len(grid_index_val)):
        dis_origin=int(distance.euclidean((origin),(grid_index_val[val][0])))
        indices= list(grid_index_val[val][0])
        find_cnt=grid[indices[0]][indices[1]][indices[2]]
        array_cnt.append((find_cnt,indices,grid_index_val[val][1]))
    #print(array_cnt)
    for i in range (0,len(array_cnt)):
        a=1/array_cnt[i][0]
        array_prob[i]=a
    #print(type(array_prob[0]))
    if(len(archive)==1):
        return archive[0]
    else:
        while(True):
            leader=roulette_wheel_selection(archive,array_prob)
            if(leader is not None):
                return leader
        
         


# In[3055]:


def algorithm_3(archive,archive_grid,sigma,omega,max_archive,archive_index_val):
    true_pareto_front=np.array([])
    for  rho_prime in sigma:
         archive.remove(rho_prime)
         np.append(true_pareto_front,rho_prime)
    if (len(archive)!=max_archive):
        archive.append(omega)
    elif(len(archive)==max_archive):
        archive,archive_grid,archive_index_val=remove_solution(archive,archive_grid,archive_index_val)
        archive.append(omega)
    np.append(true_pareto_front, omega)
    return archive,archive_grid,archive_index_val,true_pareto_front
        


# In[3056]:


def algorithm_1(Tasks,Servers):
    #print(Tasks,Servers)
    a=np.random.uniform(0,2.000002,(1,Tasks*Servers))
    a=a[::-1]
    C=np.random.uniform(0,2.00002,(1,Tasks*Servers))
    A=np.random.uniform(-1,1.0001,(1,Tasks*Servers))
    P=initialize_random_position_vector(Tasks,Servers,300)
    sol_array=calc_values(P,Tasks,Servers)
    max_time,min_time,max_energy,min_energy,max_cost,min_cost,dim_time,dim_cost,dim_energy=find_max_min(sol_array,P)
    grid,grid_index_val=make_grid(dim_time,dim_cost,dim_energy,max_time,min_time,max_energy,min_energy,max_cost,min_cost,sol_array)
    archive=[]
    alpha=None
    beta=None
    gamma=None
    archive,archive_grid,archive_index_val=algorithm_2(P,sol_array,Tasks,Servers,archive)
    true_pareto_front=np.array(archive)
    obtained_set=np.array([sol_array])
    findIgd(np.random.choice(obtained_set.flatten(),true_pareto_front.shape[0]), true_pareto_front)
    tpf=np.array([])
    for val in true_pareto_front:
        np.append(tpf,np.array([val.time,val.energy,val.cost]))
    ob=np.random.choice(obtained_set.flatten(),1)
    #findHyper(tpf,ob)
    alpha=select_leader(archive,archive_grid,archive_index_val)
    print(alpha.time,alpha.energy,alpha.cost)
    archive.remove(alpha)
    if(archive):
        beta=select_leader(archive,archive_grid,archive_index_val)
        print(beta.time,beta.energy,beta.cost)
        archive.remove(beta)
    if(archive):

        gamma=select_leader(archive,archive_grid,archive_index_val)
        print(gamma.time, gamma.energy, gamma.cost)
    archive.append(alpha)
    archive.append(beta)
    max_iter=10
    t=0
    while(t<10):
        updated_array=[]
        for i,sol in enumerate(sol_array):
            if(alpha is not None and beta is not None and gamma is not None):
                #print(sol.xw.shape)
                #print("Prev :",np.count_nonzero(sol.xw==1))
                updated_vec=update_position_search_agent(sol,alpha,beta,gamma,a,A,C,Tasks,Servers)
                #print(type(updated_vec))
                #print("Updated Vec: ",updated_vec)
                bin_vec=binarize(updated_vec,Tasks)
                #print(bin_vec)
                updated_solution=solution(bin_vec,-1,-1,-1,Tasks,Servers)
                updated_solution.calculate_val_per_wolf(updated_solution.xw)
                sol_array[i]=updated_solution
                #print("Now :",np.count_nonzero(sol_array[i].xw==1))
        a,A,C=update_params(Tasks,Servers)
        #print("size archive ",len(archive))
        archive,archive_grid,archive_index_val=algorithm_2(P,sol_array,Tasks,Servers,archive)
        alpha=select_leader(archive,archive_grid,archive_index_val)
        
        archive.remove(alpha)
        if(archive):
            beta=select_leader(archive,archive_grid,archive_index_val)
            #print(beta in archive)
            archive.remove(beta)
        if(archive):
            gamma=select_leader(archive,archive_grid,archive_index_val)
        archive.append(alpha)
        archive.append(beta)
        t=t+1
    print("Solution :" ,alpha.xw)
        


# In[3057]:


Tasks,Servers=innnit()
algorithm_1(Tasks,Servers)


# In[ ]:




