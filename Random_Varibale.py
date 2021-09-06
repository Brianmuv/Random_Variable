#Librerias
"""

#Importe de librerias para el laboratorio ---- IMPORTANTE: ejecutar antes de
import numpy as np 
from matplotlib import cm
import sympy as sym
import matplotlib.pyplot as plt
from scipy.stats import norm
import scipy.stats as ss
from math import sqrt

"""# 1 -PDF Gausiana: 
  media cero, dispersion =1
"""

#crear el vector de -10 a 10 en pasos de 0.1
x=np.arange(-10,10,0.1)

#PDF :
u = 0   #  media = 0
var=1   # Varianza o dispersion
sdt = sqrt(var)  #  desviación estandar = 1, luego, Varianza =1
pdf= norm.pdf(x,u,sdt)  # pdf, usando la función normpdf
#parámetros para graficar
plt.title("PDF Normal")
plt.plot(x,pdf,'k-',label='norm pdf')
plt.xlabel('X')
plt.ylabel('Amplitud')
plt.grid()
plt.show()

"""#2 - Variar Media y dispersión: """

#PDF :
u =-2   #  media = 2
var=3   # Varianza o dispersion
sdt = sqrt(var)  #  desviación estandar = 1, luego, Varianza =1
pdf= norm.pdf(x,u,sdt)  # pdf, usando la función normpdf
#parámetros para graficar
plt.title("PDF Normal")
plt.plot(x,pdf,'k-',label='norm pdf')
plt.xlabel('X')
plt.ylabel('Amplitud')
plt.grid()
plt.show()

#PDF :
u = 3   #  media = 5
var=6   # Varianza o dispersion
sdt = sqrt(var)  #  desviación estandar = 1, luego, Varianza =1
pdf= norm.pdf(x,u,sdt)  # pdf, usando la función normpdf
#parámetros para graficar
plt.title("PDF Normal")
plt.plot(x,pdf,'k-',label='norm pdf')
plt.xlabel('X')
plt.ylabel('Amplitud')
plt.grid()
plt.show()

"""Observaciones: 
- Se logra apreciar en la variación de la media y dispersión, como se modifica la agrupación y distribución de los datos.
- La campana de Gauss apila los datos en base a la dispersión, por ende la variación de está misma afecta directamente los resultados probabilisticos, cargados en partes contrarias de la recta numérica.
- Se evidencia graficamente la propidad de la pdf que indica que el área bajo la curva es 1, esto se puede notar al momento de aumentar la dispersión, dado que la campana se hace mas ancha, se  reduce su amplitud; dicho efecto se puede abstraer como una conservación de la masa.

#3 - Vector de 10.000 muestras
"""

#Funciones para calcular media, Varianza y desviación standar
def media(x):
  s = 0
  for elemento in x:
    s += elemento
  return s / float(len(x))
 
def varianza(x):
  s = 0
  m = media(x)
  for elemento in x:
    s += (elemento - m) ** 2
  return s / float(len(x))
 
def sdt(x):
  return sqrt(varianza(x))
#Vector rand 
x=np.random.randint(low=0, high=1000, size=10000)
#Grafico del vector Rand
plt.title("VA generada por Rand")
plt.xlabel('X')
plt.plot(x)
print("Media = " +str(media(x)))
print("Varianza = "+str(varianza(x)))
print("Desviación estandar = "+str(sdt(x)))



print("---------------------------------\n\n")

"""# 4 - Calculo de media, varianza y desviacion estamdar

"""

print("Media = "+str(np.mean(x)))
print("Varianza = "+str(np.var(x)))
print("desviación estandar = "+str(np.std(x)))

"""**Observaciones**:

Los resultados obtenidos por medio de las fórmulas matematicas, en comparación a los obtenidos por medio de la función de numpy son practicamente iguales, en la desvicion estandar existe un diferencia infinitesimal, la cual, en la mayoria de contextos, se puede despreciar.  Más alla de los resultados, que se evidencian iguales, habria que analizar la eficiencia del codigo en términos computacionales, dado que en términos funcionales, logran hacer la misma tarea.

#5 -  12 Variables aleatorias
"""

#numero de muestras y variables aleatorias
numero_muestras=1000
VAS=[]

#12 variables aleatorias 

for i in range(12):
    VAS.append(np.random.rand(numero_muestras))
    plt.subplot(6,2,i+1),plt.hist(VAS[i])
    plt.xlabel("Posicion del dato ")
    plt.title("VA[" + str(i+1)+"]")
    plt.grid()
    plt.show()

#promedio de la suma de las variables generadas Y

Y=(VAS[0]+VAS[1]+VAS[2]+VAS[3]+VAS[4]+VAS[5]+VAS[6]+VAS[7]+VAS[8]+VAS[9]+VAS[10]+VAS[11])/12
plt.title('PDF')
plt.hist(Y)


#media y varianza de Y 
print("\n--------------------------------")
print("Media = "+str(np.mean(Y)))
print("Varianza = "+str(np.var(Y)))
print("--------------------------------\n")
