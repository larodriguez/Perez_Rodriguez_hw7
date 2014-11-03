#Este programa grafica los resultados del archivo string.c
import sys
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D

#recogemos el nombre del archivo.dat que entra como parametro
data= sys.argv[1]

#cargar datos del archivo
datos = np.loadtxt(data)

#definir arreglos para graficar
t=[]
u=[]
x=[]

for i in range (1, len(datos)):
    t.append(datos[:,0])
    u.append(datos[:,i])
    x.append([i-1]*100)
print x, t, u
#saber cuales fueron las condiciones iniciales
l=list(datos)
n=len(l)
l[n-4:n]=[]
nombredatos="".join(l)


#Gracia 3D de la trayectoria en el plano x, y, z
#figura = plt.figure()
#tp = Axes3D(figura)
#tp.set_xlabel("$X$",fontsize=20)
#tp.set_ylabel("$Y$",fontsize=20)
#tp.set_zlabel("$Z$",fontsize=20)
#tp.set_title("$\mathrm{Trayectoria Particula en 3D}$", fontsize=30)
#tp.plot(x, y, z)
#plt.savefig(str(nombredatos)+'_3D_'+'.pdf')
