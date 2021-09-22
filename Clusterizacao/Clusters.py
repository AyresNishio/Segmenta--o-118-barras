import matplotlib.pyplot as plt
import networkx as nx
from networkx import *
import numpy as np

import itertools

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


def Agrupar(G,pos, num_clusters):
    n_nodes = G.number_of_nodes
    v_labels =  {x: x for x in G.nodes}
    nodes = list(G.nodes)

    #Convert Grapgh into a matrix
    edge_mat = graph_to_edge_matrix(G)
    print(edge_mat)
    results = []
    algorithms = {}
    #algorithms['kmeans'] = cluster.KMeans(n_clusters=num_clusters,n_init= 100,precompute_distances = True, n_jobs = -1, algorithm = "auto")
    # #Spectral Clustering
    #algorithms['spectral'] = cluster.SpectralClustering(n_clusters=num_clusters, affinity="precomputed", n_init=14, assign_labels="discretize")
    algorithms['spectral'] = cluster.SpectralClustering( affinity="precomputed", n_init=14, assign_labels="discretize")
    # Fit all models
    for model in algorithms.values():
        model.fit(edge_mat)
        #results.append(list(model.labels_))
        results = list(model.labels_)
    num_clusters = max(results)+1
    #results = list(itertools.chain.from_iterable(results))
    
    #nx.draw(G,pos,with_labels = True, node_color=list(algorithms['kmeans'].labels_))
    nx.draw(G,pos,with_labels = True, node_color=list(algorithms['spectral'].labels_))
    plt.title("kmeans_test")
    plt.show()
    grupos = []
    nodes_G = list(G.nodes())
    for i  in range(num_clusters):
        temp =[]
        for j in range(len(results)):
            if (results[j] == i): 
                temp.append(int(nodes_G[j]))
        grupos.append(np.array(temp,dtype=np.int32))


    return grupos

def graph_to_edge_matrix(G):#(G,weight):
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

def get_weight(med_plan,num_bus): 
    weight_list = {}
    for i in range(num_bus):
        weight_list[i+1] = 0

    for med in med_plan:
            weight_list[med[5]] += 1

    return weight_list