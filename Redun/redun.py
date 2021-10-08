import numpy as np
def redundancia(med, Ybus):
    num_med = med.shape[0]
    num_barras = Ybus.shape[0]
    num_linhas = np.sum(Ybus)/2
    # fluxo e injeção
    max_med = 2*num_linhas + num_barras
    redun = (num_med - num_barras)/(max_med - num_barras)

    return redun

def redundancia_G( med,G,Ybus):
    num_med = med.shape[0]

    num_barras = G.shape[0]

    num_linhas = 0
    for barra in G:
        for l in range(barra-1,num_barras): 
            num_linhas = num_linhas + Ybus[barra,l]

    # fluxo e injeção
    max_med = 2*num_linhas + num_barras
    redun = (num_med - num_barras)/(max_med - num_barras)
    return redun
