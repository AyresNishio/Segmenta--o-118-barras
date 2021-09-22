
import matplotlib.pyplot as plt
import networkx as nx
from networkx import *
import numpy as np

from sklearn import cluster
from collections import defaultdict
from matplotlib import cm
import seaborn as sns
import pandas as pd
import random 
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics.cluster import adjusted_rand_score

from networkx.algorithms.community import kernighan_lin_bisection
from networkx.algorithms.community import greedy_modularity_communities
from networkx.algorithms.community import label_propagation_communities
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics.cluster import adjusted_rand_score



# IEEE 14-BUS POWER SYSTEM
med_plan = np.loadtxt('Med_Plan_14b_33m.txt',dtype = 'i')
Ybus = np.loadtxt("ieee-14-bus.txt", dtype='i', delimiter=',')
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

def graph_to_edge_matrix(G,weight):
    """Convert a networkx graph into an edge matrix.
    See https://www.wikiwand.com/en/Incidence_matrix for a good explanation on edge matrices
   
    Parameters
    ----------
    G : networkx graph
    """
    # Initialize edge matrix with zeros
    edge_mat = np.zeros((len(G), len(G)), dtype=int)

    # Loop to set 0 or 1 (diagonal elements are set to 1)
    for node in G:
        for neighbor in G.neighbors(node):
            edge_mat[node-1][neighbor-1] = 1
            #edge_mat[node-1][neighbor-1] = weight[node]+weight[neighbor]
        #edge_mat[node-1][node-1] = weight[node]+1
        edge_mat[node-1][node-1] = 1

    return edge_mat

def Monta_sys_w(Ss,Ybus,weight_list):

    G = nx.Graph()

    for v in Ss:
        G.add_node(v,nmedidas = weight_list[v])

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

weight = get_weight(med_plan,14) #retorna um dicionario que relaciona o num da barra com a qtde de medidas a ela associadas
weight_list = [weight[key] for key in weight.keys()]

G  = Monta_sys_w(range(1,np.size(Ybus,0)+1),Ybus,weight)
n_nodes = G.number_of_nodes
v_labels =  {x: x for x in G.nodes}
pos = coord
nodes = list(G.nodes)

#Convert Grapgh into a matrix
edge_mat = graph_to_edge_matrix(G,weight)
print(edge_mat)
k_clusters = 2
results = []
algorithms = {}

#K-Means
algorithms['kmeans'] = cluster.KMeans(n_clusters=k_clusters,n_init= 100,precompute_distances = True, n_jobs = -1, algorithm = "auto")

# #Agglomerative Clustering
# algorithms['agglom'] = cluster.AgglomerativeClustering(n_clusters=k_clusters, linkage="ward")

# #Spectral Clustering
# algorithms['spectral'] = cluster.SpectralClustering(n_clusters=k_clusters, affinity="precomputed", n_init=14, assign_labels="discretize")

# #Affinity Propagation
# algorithms['affinity'] = cluster.AffinityPropagation(damping=0.7,affinity="precomputed")

# Fit all models
for model in algorithms.values():
    model.fit(edge_mat)
    results.append(list(model.labels_))
print("Models Fitted")

#K-Means
grupos = []

nx.draw(G,coord,with_labels = True, node_color=list(algorithms['kmeans'].labels_))
plt.title("kmeans_test")
plt.show()
# plt.savefig("kmeans118_" + f'teste{k_clusters}_clusters'+ ".png")

#Agglomerative Clustering
# nx.draw(G,coord,with_labels = True, node_color=list(algorithms['agglom'].labels_))
# plt.title("Agglomerative_118_test")
# plt.show()
# # plt.savefig("Agglomerative_118_" + f'teste{k_clusters}_clusters'+ ".png")

# #Spectral Clustering
# nx.draw(G,coord,with_labels = True, node_color=list(algorithms['spectral'].labels_))
# plt.title("Spectral_118_test")
# plt.show()
# # plt.savefig("Spectral_118_."+ f'teste{k_clusters}_clusters'+ ".png")

# #Affinity
# nx.draw(G,coord,with_labels = True, node_color=list(algorithms['affinity'].labels_))
# plt.title("Affinity_118_test")
# plt.show()
# plt.savefig("Affinity_118_" +f'teste{k_clusters}_clusters'+".png")

print('plot finished')


r = lambda: random.randint(0,255)
colors = []
for i in range(40):
    color = '#{:02x}{:02x}{:02x}'.format(r(), r(), r())
    colors.append(color)


init_nodes = np.array_split(G.nodes(), 2)
init_partition = [set(init_nodes[0]), set(init_nodes[1])]
#lst_b = label_propagation_communities(G)
lst_b = kernighan_lin_bisection(G,init_partition)
#lst_b = greedy_modularity_communities(G)
color_map_b = ["black"] * nx.number_of_nodes(G)
counter = 0
for c in lst_b:
  for n in c:
    color_map_b[n-1] = colors[counter]
  counter = counter + 1
nx.draw_networkx_edges(G, coord)
nx.draw_networkx_nodes(G, coord, node_color=color_map_b)
nx.draw_networkx_labels(G, coord)
plt.axis("off")
plt.show()
print("acabou")
