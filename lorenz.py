#Importamos las librerias

from matplotlib import pyplot as plt #Libreria para graficar, muy similar al matlab
import numpy as np # Libreria para trabajar con matrices y algunas expresiones matematicas
import pandas as pd # Libreria para trabajar con dataframes
import scipy as sp # Libreria para trabajar con funciones matematicas
from matplotlib import style # Libreria para estilos de graficos
plt.style.use(['science', 'notebook']) # Estilo de graficos
#from mpl_toolkits.mplot3d import axes3D
import matplotlib.animation as animation

beta = 8./3.
sigma = 10
rho = 28

def lorenz(x,y, z):
    u = -sigma*x+sigma*y
    v = rho*x-y-x*z
    w = -beta*z+x*y
    return u, v, w

xo = -8
yo = 8
zo = 27

xs = [xo]
ys = [yo]
zs = [zo]

dt = 0.01
tiempo = np.arange(0,600+dt,dt)

for i in range(600):
    x_derivada, y_derivada, z_derivada = lorenz(xs[i], ys[i], zs[i])
    xs.append(xs[i]+x_derivada*dt)
    ys.append(ys[i]+y_derivada*dt)
    zs.append(zs[i]+z_derivada*dt)
    



fig = plt.figure()
ax = fig.gca()

def actualizar(i):
    ax.clear()
    ax.plot(xs[:i], zs[:i], 'o-')
    plt.title('y vs x')
    plt.axis([min(xs), max(xs), min(zs), max(zs)])
plt.plot(xs, zs, '-')  
plt.show()  
#ani = animation.FuncAnimation(fig, actualizar, range(len(xs)), interval=1)
#plt.show()
'''
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
ax = plt.axes(projection='3d')
ax.plot3D(xs, ys, zs, 'magenta')'''
