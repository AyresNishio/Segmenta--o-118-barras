from Segmentador.Segmenta import *

Grupos = []
G1 = np.loadtxt('Segmentador/Casos_feeling/Grupo1.txt',dtype=np.int32)
Grupos.append(G1)
G2 = np.loadtxt('Segmentador/Casos_feeling/Grupo2.txt',dtype=np.int32)
Grupos.append(G2)
G3= np.loadtxt('Segmentador/Casos_feeling/Grupo3.txt',dtype=np.int32)
Grupos.append(G3)

med_plan = np.loadtxt('Casos/118bLRG1/med118b333m.txt', dtype='i')

E = np.loadtxt('Casos/118bLRG1/E118b333m.txt', dtype=np.float64)

Segmenta_med_plan( med_plan,Grupos,E)

print('')

#######################
