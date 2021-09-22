from Segmentador.Segmenta import *

Grupos = []
G1 = np.loadtxt('Segmentador/Casos_feeling/Grupo1s.txt',dtype=np.int32)
Grupos.append(G1)
G2 = np.loadtxt('Segmentador/Casos_feeling/Grupo2s.txt',dtype=np.int32)
Grupos.append(G2)
G3= np.loadtxt('Segmentador/Casos_feeling/Grupo3s.txt',dtype=np.int32)
Grupos.append(G3)

med_plan = np.loadtxt('med118b333m.txt', dtype='i')

E = np.loadtxt('E118b333m.txt', dtype=np.float64)

Segmenta_med_plan( med_plan,Grupos,E)

print('')
