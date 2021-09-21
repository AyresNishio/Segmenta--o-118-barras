from sklearn import cluster
import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics.cluster import adjusted_rand_score

def graph_to_edge_matrix(G):
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
        edge_mat[node-1][node-1] = 1

    return edge_mat


def Monta_sys(Ss,Ybus):

    G = nx.Graph()

    for v in Ss:
        G.add_node(v)

    for i in Ss:
        for j in Ss:
            if (i>j)  and (Ybus[i-1, j-1]) == 1:
               G.add_edge(i,j)
    return G  

#######################################################Main#########################################################
Ybus = np.loadtxt("ieee-118-bus.txt", dtype='i', delimiter=",")
coord = {
1: np.array([15, 0]),
2: np.array([130, 0]),
3: np.array([15, -40]),
4: np.array([40, -60]),
5: np.array([15, -100]),
6: np.array([80, -100]),
7: np.array([130, -80]),
8: np.array([30, -160]),
9: np.array([30, -220]),
10: np.array([30, -280]),
11: np.array([80, -60]),
12: np.array([130, -40]),
13: np.array([180, -75]),
14: np.array([220, -15]),
15: np.array([220, -75]),
16: np.array([130, -130]),
17: np.array([170, -130]),
18: np.array([215, -130]),
19: np.array([275, -100]),
20: np.array([260, -160]),
21: np.array([260, -210]),
22: np.array([260, -285]),
23: np.array([260, -335]),
24: np.array([285, -235]),
25: np.array([260, -390]),
26: np.array([185, -310]),
27: np.array([60, -255]),
28: np.array([60, -190]),
29: np.array([60, -130]),
30: np.array([185, -230]),
31: np.array([145, -175]),
32: np.array([100, -220]),
33: np.array([300, -45]),
34: np.array([340, -100]),
35: np.array([295, -70]),
36: np.array([295, -145]),
37: np.array([370, -45]),
38: np.array([355, -220]),
39: np.array([300, 0]),
40: np.array([340, 0]),
41: np.array([390, -30]),
42: np.array([410, 0]),
43: np.array([320, -165]),
44: np.array([390, -70]),
45: np.array([390, -145]),
46: np.array([390, -190]),
47: np.array([440, -150]),
48: np.array([425, -85]),
49: np.array([475, -135]),
50: np.array([470, -80]),
51: np.array([500, -105]),
52: np.array([465, -40]),
53: np.array([430, 0]),
54: np.array([495, 0]),
55: np.array([585, 0]),
56: np.array([510, -40]),
57: np.array([525, -90]),
58: np.array([545, -50]),
59: np.array([560, -30]),
60: np.array([600, -60]),
61: np.array([585, -125]),
62: np.array([600, -180]),
63: np.array([585, -70]),
64: np.array([560, -125]),
65: np.array([580, -200]),
66: np.array([500, -180]),
67: np.array([600, -245]),
68: np.array([477, -250]),
69: np.array([440, -200]),
70: np.array([380, -235]),
71: np.array([285, -330]),
72: np.array([285, -285]),
73: np.array([285, -390]),
74: np.array([310, -350]),
75: np.array([345, -330]),
76: np.array([400, -330]),
77: np.array([450, -330]),
78: np.array([415, -250]),
79: np.array([455, -270]),
80: np.array([490, -290]),
81: np.array([535, -270]),
82: np.array([400, -365]),
83: np.array([345, -365]),
84: np.array([290, -430]),
85: np.array([345, -415]),
86: np.array([345, -490]),
87: np.array([310, -490]),
88: np.array([390, -385]),
89: np.array([390, -490]),
90: np.array([440, -490]),
91: np.array([480, -490]),
92: np.array([470, -415]),
93: np.array([415, -425]),
94: np.array([490, -370]),
95: np.array([415, -385]),
96: np.array([500, -330]),
97: np.array([465, -330]),
98: np.array([515, -330]),
99: np.array([535, -290]),
100: np.array([560, -325]),
101: np.array([505, -415]),
102: np.array([495, -490]),
103: np.array([535, -415]),
104: np.array([585, -365]),
105: np.array([600, -330]),
106: np.array([528, -245]),
107: np.array([580, -240]),
108: np.array([600, -410]),
109: np.array([600, -490]),
110: np.array([555, -490]),
111: np.array([510, -490]),
112: np.array([575, -400]),
113: np.array([150, -235]),
114: np.array([130, -320]),
115: np.array([130, -390]),
116: np.array([475, -170]),
117: np.array([200, 0]),
118: np.array([370, -270])}

#Monta G
G  = Monta_sys(range(1,np.size(Ybus,0)+1),Ybus)
nx.draw_networkx(G,coord,with_labels=True)
plt.show()

#Convert Grapgh into a matrix
edge_mat = graph_to_edge_matrix(G)
print(edge_mat)

k_clusters = 2
results = []
algorithms = {}

#K-Means
algorithms['kmeans'] = cluster.KMeans(n_clusters=k_clusters, n_init=118)

#Agglomerative Clustering
algorithms['agglom'] = cluster.AgglomerativeClustering(n_clusters=k_clusters, linkage="ward")

#Spectral Clustering
algorithms['spectral'] = cluster.SpectralClustering(n_clusters=k_clusters, affinity="precomputed", n_init=118)

#Affinity Propagation
algorithms['affinity'] = cluster.AffinityPropagation(damping=0.6)

# Fit all models
for model in algorithms.values():
    model.fit(edge_mat)
    results.append(list(model.labels_))
print("Models Fitted")

#K-Means

#Agglomerative Clustering

#Spectral Clustering


#Affinity
nx.draw(G,coord,with_labels = True, node_color=list(algorithms['affinity'].labels_))
plt.show()