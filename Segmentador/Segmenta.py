

import numpy as np
from numpy.core.fromnumeric import reshape

def Segmenta_med_plan(med_plan, grupos, E):

    med_aux = med_plan.copy()

    for i in range(len(grupos)):
        sub_med_plan = Sub_med_plan(med_aux, i+1,grupos[i])

        Eg = Sub_Covax(sub_med_plan,E,i+1)

        np.savetxt(f'E{i+1}_{len(sub_med_plan)}m.txt',Eg,delimiter=' ', fmt='%i')
        np.savetxt(f'medplan{i+1}_{len(sub_med_plan)}m.txt',sub_med_plan, delimiter=' ', fmt='%i')

        #A = sub_Topology (grupos[i],A,i,num_barras)



def Sub_med_plan(med, n, G):
    sub_med_plan =  []
    
    for medida in med:
        if medida[1] in G or medida[2] in G:
            sub_med_plan.append(medida)


    # with open(f'Med_Plan{n}_{len(sub_med_plan)}m.txt','w') as f:
    #      np.savetxt(f, sub_med_plan,fmt='%d',delimiter=' ') 
    
    return sub_med_plan

#Monta Matriz de Covariância do Subsistemas de medição
def Sub_Covax ( med, E, n):

    # Constroi Matrizes E dos subsistemas
    #array =  np.arange(len(med)*len(med)).reshape(len(med),len(med))
    Eg = np.zeros((len(med),len(med)),np.float64)
    lin = 0
    for medi in med:
        col = 0
        for medj in med :
            de   = medi[0]-1 
            para = medj[0]-1
            Eg[lin,col] =  E[de,para]
            col = col + 1
        lin = lin + 1

    with open(f'E{n}_{len(med)}m.txt','w') as f:
        np.savetxt(f, Eg) 
    return Eg;

#Constroi Matrizes de coneção dos subsistemas (Averiguar se indices estão corretos *comceçam de zero)
def sub_Topology(G,A,n,nb):
    As=np.zeros((G.shape[0],G.shape[0]))
    nlin=0
    for i in G:
        ncol=0
        for j in G:
            As[nlin][ncol] = A[i-1][j-1]
            ncol=ncol+1
        nlin =nlin+1 
    
    with open(f'A{n}_{nb}b.txt','w') as f:
        np.savetxt(f, As, fmt='%i',delimiter=',') 
    
    return As


if __name__ == 'main' :
    #Carrega A
    with open('A118b.txt', 'r') as f:   
        A = np.array([[int(num) for num in line.split(',')] for line in f])

    #Grupo 1
    with open('Grupo1s.txt', 'r') as f:
        G1 = np.array([int(b)  for b in f])
    #print(G1)

    #Grupo 2
    with open('Grupo2s.txt', 'r') as f:
        G2 = np.array([int(b)  for b in f])
    #print(G2)

    #Grupo 3
    with open('Grupo3s.txt', 'r') as f:
        G3 = np.array([int(b)  for b in f])
    #print(G3)

    #Carrega E
    # with open('E118b176m.txt', 'r') as f:
    #     E = np.array([[np.float64(num) for num in line.split('\t')] for line in f])
    with open('E118b300m.txt', 'r') as f:
        E = np.array([[np.float64(num) for num in line.split(' ') if num != '\n'] for line in f])
        #E = np.loadtxt(f,dtype=np.float64,delimiter='\t')

    #Carrega plano de medição
    with open('Med_Plan_118b_300m.txt', 'r') as f:
        med = [[int(num) for num in line.split(' ')if num != '\n'] for line in f]
    #print(med)    

    


    # adiciona Barras sobrepostas
    # for m in med:
    #     if 
