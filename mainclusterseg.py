from Segmentador.Segmenta import *
from Clusterizacao.Clusters import *

from System_Display.System_Display_w import*
med_plan = np.loadtxt('med118b333m.txt', dtype='i')
E = np.loadtxt('E118b333m.txt', dtype=np.float64)

pos,A = coords(118)
G=Monta_sys(range(1,np.size(A,0)+1),A)
num_clusters =  3
weight = get_weight(med_plan,118)
Grupos = Agrupar(G,pos,num_clusters,weight)
n = 1
for grupo in Grupos:
    np.savetxt(f"Grupo{n}.txt", grupo, fmt='%i')
    n +=1


Segmenta_med_plan( med_plan,Grupos,E)