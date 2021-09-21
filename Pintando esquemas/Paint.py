import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx
from networkx import *
import numpy as np

# IEEE 14-BUS POWER SYSTEM
med_plan = np.loadtxt('Med_Plan_14b_33m.txt',dtype = 'i')
Ybus = np.loadtxt("ieee-14-bus.txt", dtype='i', delimiter='\t')
coord = {
0: np.array([0, 4]), 
1: np.array([0, 2]), 
2: np.array([0, 0]), 
3: np.array([6, 0]), 
4: np.array([6, 2]), 
5: np.array([2, 2]), 
6: np.array([0, 6]), 
7: np.array([4, 4]), 
8: np.array([2, 4]), 
9: np.array([6, 6]), 
10: np.array([4, 6]), 
11: np.array([2, 6]), 
12: np.array([0, 8]), 
13: np.array([2, 8]), 
14: np.array([6, 8])}

def Monta_sys(Ss,Ybus):

    G = nx.Graph()

    for v in Ss:
        G.add_node(v)

    for i in Ss:
        for j in Ss:
            if (i>j)  and (Ybus[i-1, j-1]) == 1:
               G.add_edge(i,j)

    return G    

def get_weight(med_plan,num_bus): 
    weight_list = {}
    for i in range(num_bus):
        weight_list[i+1] = 0

    for med in med_plan:
            weight_list[med[5]] += 1

    return weight_list
#G=nx.Graph()
G  = Monta_sys(range(1,np.size(Ybus,0)+1),Ybus)
n_nodes = G.number_of_nodes
v_labels =  {x: x for x in G.nodes}
pos = coord
weight = get_weight(med_plan,14) #retorna um dicionario que relaciona o num da barra com a qtde de medidas a ela associadas
weight_list = [weight[key] for key in weight.keys()]
nodes = list(G.nodes)
maxcolor = max(weight_list)
for key in weight.keys(): # define a cor pelo grau do nó 
    if weight[key] >= (maxcolor // 2):
        nx.draw_networkx_labels(G, pos,{key : key}, font_size=11, font_color='w')
    else:
        nx.draw_networkx_labels(G, pos, {key : key}, font_size=11, font_color='k')

nx.draw_networkx(G, pos, with_labels = True, labels = v_labels , node_color = weight_list,node_shape ='o', width = 0.5, font_size = 0.5, cmap = plt.get_cmap('Oranges'), vmin = min(weight_list), vmax = max(weight_list))
bounds = np.linspace(1,max(weight_list), len(nodes))
sm = plt.cm.ScalarMappable(cmap=plt.get_cmap('Oranges'),norm=plt.Normalize(vmin = min(weight_list), vmax = max(weight_list)))
sm._A = []
sm.set_array(list(range(min(weight_list), max(weight_list) + 1)))
plt.colorbar(sm, ticks = range(min(weight_list), max(weight_list) + 1))
plt.gca().set_facecolor('paleturquoise')
# plt.colorbar(sm)
plt.show() # display
print("acabou")
