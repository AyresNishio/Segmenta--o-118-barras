from System_Display.System_Display_w import*
from Clusterizacao.Clusters import*

#A= np.loadtxt('ieee-118-bus.txt',dtype=np.int32,delimiter=',')
pos,A = coords(118)
G=Monta_sys(range(1,np.size(A,0)+1),A)
num_clusters =  3
grupos = Agrupar(G,pos,num_clusters)