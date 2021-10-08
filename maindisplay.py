
import numpy as np
import matplotlib.pyplot as plt
from Redun.redun import *
from System_Display.System_Display_w import *
num_barras = 118
coord, Ybus = coords(num_barras)
#Grupo 1
with open('Segmentador/SegNormal/Grupo1.txt', 'r') as f:
    S1 = np.array([int(b)  for b in f])
#print(G1)

#Grupo 2
with open('Segmentador/SegNormal/Grupo2.txt', 'r') as f:
    S2 = np.array([int(b)  for b in f])
#print(G2)

#Grupo 3
with open('Segmentador/SegNormal/Grupo3.txt', 'r') as f:
    S3 = np.array([int(b)  for b in f])

G  = Monta_sys(range(1,np.size(Ybus,0)+1),Ybus)
G1 = Monta_sys(S1,Ybus)
G2 = Monta_sys(S2,Ybus)
G3 = Monta_sys(S3,Ybus)

Display_sys(G, coord,'black')

Display_sys(G1,coord,'green')
Display_sys(G2,coord,'red')
Display_sys(G3,coord,'orange')



plt.close()

med = np.loadtxt('Casos/118bLRG1/med118b333m.txt',dtype=int)
display_w(med,num_barras)

redun_sis = redundancia(med,Ybus)
med_G1 = np.loadtxt('Casos/118bLRG1/FsS/medplan1_62m.txt',dtype=int)
redun_G1 = redundancia_G(med_G1, S1, Ybus) 
med_G2 = np.loadtxt('Casos/118bLRG1/FsS/medplan2_138m.txt',dtype=int)
redun_G2 = redundancia_G(med_G2, S2, Ybus) 
med_G3 = np.loadtxt('Casos/118bLRG1/FsS/medplan3_149m.txt',dtype=int)
redun_G3 = redundancia_G(med_G3, S3, Ybus) 

plt.show()

print('')