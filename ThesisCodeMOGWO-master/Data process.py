#!/usr/bin/env python
# coding: utf-8

# In[63]:


import operator
import math
import matplotlib.pyplot as plt


# In[67]:


time=[93887.05503365818,786306.77849613,852657.1023104,1660517.4675571998, 2870295.3281984883, 3540635.65642302]
energy=[4122.807983598852, 67916.9504370838, 92491.60816042068,193118.3337562242,312639.1048198713,408635.18185789906]
cost=[719702093002.4559,15240704677514.018,28420532258001.066,50970385998547.445,58920795825280.04,58899943244238.81]
user=[10,60,110,160,210,260]
#Time=sorted(Time, key = lambda x:float(x))
for i in range(0,len(user)):
    time[i]=time[i]/20000
    energy[i]=energy[i]/10000
    cost[i]=cost[i]/(pow(10,14))
print("Time : ",time)
print("Cost : ",cost)
print("Energy : ",energy)
user_time=dict(zip(user, time))
user_time=sorted(user_time.items(), key=operator.itemgetter(1))
user_energy=dict(zip(user, energy))
user_energy=sorted(user_energy.items(), key=operator.itemgetter(1))
user_cost=dict(zip(user, cost))
user_cost=sorted(user_cost.items(), key=operator.itemgetter(1))
print("Time ",user_time)
print("Energy ",user_energy)
print("Cost ",user_cost)
plt.plot(user,time,label = "BMOGWO",marker='p')
plt.xlabel('Number of Users')
# naming the y axis
plt.ylabel('Average Latency (ms)')
plt.legend()
plt.show()
plt.plot(user,energy,label = "BMOGWO",marker='p')
plt.xlabel('Number of Users')
# naming the y axis
plt.ylabel('Average Energy (J)')
plt.legend()
plt.show()
plt.plot(user,cost,label = "BMOGWO",marker='p')
plt.xlabel('Number of Users')
# naming the y axis
plt.ylabel('Average Normalized Cost')
plt.legend()
plt.show()


# In[68]:


time=[875559.1514925808,512482.18652468536, 380632.55702828494,314873.28477302386,285250.3090532269,224777.2488068372]
energy=energy=[64649.18900367724,53036.451334234036,31477.068059010617,30645.590326744365,28651.669700860377,26406.269199703936]
cost=cost=[6078478494002.11,6417590509076.156,7531957977224.47,8944716678170.506,9025856739530.27,9106942117231.41]
server=[2,4,6,8,10,12]
#Time=sorted(Time, key = lambda x:float(x))
for i in range(0,len(user)):
    time[i]=time[i]/10000
    energy[i]=energy[i]/1000
    cost[i]=cost[i]/(pow(10,13))
print("Time : ",time)
print("Cost : ",cost)
print("Energy : ",energy)
server_time=dict(zip(server, time))
server_time=sorted(server_time.items(), key=operator.itemgetter(1))
server_energy=dict(zip(server, energy))
server_energy=sorted(server_energy.items(), key=operator.itemgetter(1))
server_cost=dict(zip(server, cost))
server_cost=sorted(server_cost.items(), key=operator.itemgetter(1))
print("Time :",server_time)
print("Energy :",server_energy)
print("Cost :",server_cost)
plt.plot(server,time,label = "BMOGWO",marker='p')
plt.xlabel('Number of Servers')
# naming the y axis
plt.ylabel('Average Latency (ms)')
plt.legend()
plt.show()
plt.plot(server,energy,label = "BMOGWO",marker='p')
plt.xlabel('Number of Servers')
# naming the y axis
plt.ylabel('Average Energy (J)')
plt.legend()
plt.show()
plt.plot(server,cost,label = "BMOGWO",marker='p')
plt.xlabel('Number of Servers')
# naming the y axis
plt.ylabel('Average Normalized Cost')
plt.legend()
plt.show()


# In[ ]:




