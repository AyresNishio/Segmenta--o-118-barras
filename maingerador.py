from Generator.Gerador import*
import numpy as np
from System_Display.System_Display_w import *

num_barras = 118
redun_min = .6
nome_top = 'ieee-'+str(num_barras) + '-bus.txt'

barras_ini = [1, 5, 9, 12, 15, 19,21, 23, 27,29, 30, 32, 35, 37, 42, 43, 45, 49,52, 56, 62, 63,64, 65, 68]
grupo = [1, 2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,20,21,22,25,26,27,29,30,31,34,35,37,38,39,40,41,42,44,45,47,49,50,51,52,53,55,56,57,59,60,61,62,63,65,66,67,68,69,113]

#LÊ topologia
with open(nome_top, 'r') as f:
    A = np.array([[int(num) for num in line.split(',')] for line in f])

#GERA esquema de medição
# E,med_plan = gera_plano_medidas(A,redun_min)
E,med_plan = gera_plano_focado(A,redun_min,barras_ini,grupo)
med_plan = remove_desactivated(med_plan)

#ESCREVE esquema de medição
num_medidas =  sum(med_plan[:,6])
with open(f'E{num_barras}b{num_medidas}m.txt','w') as f:
        np.savetxt(f, E) 
with open(f'med{num_barras}b{num_medidas}m.txt','w') as f:
        np.savetxt(f, med_plan,fmt='%i')  

#display dos grafos
display_w(med_plan,num_barras)

