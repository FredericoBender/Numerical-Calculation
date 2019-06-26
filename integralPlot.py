import matplotlib.pyplot as plt
import numpy as np
from benderMathLib import simpson,trapezios
from math import *

def geraListaPontos(a,b,function,nPontos):
    h = (b-a) / (nPontos - 1)
    pontosX = []
    pontosY = []
    while(a<=b):
        x=a #Para usar "a" na função
        y = eval(function)
        pontosX.append(a)
        pontosY.append(y)
        a=a+h
    if(len(pontosY)<nPontos):
        x=b #Para usar "b" na função
        y = eval(function)
        pontosX.append(b)#Adiciona o ponto final para o calculo, já que à um erro usando float no PC, pois ele trabalha em binário
        pontosY.append(y)
    return pontosX,pontosY

a = 0 #Limite inferior de integração
b = 6 #Limite superior de integração
nPontos = 101 #Número de pontos da integração numérica
#function="(x**2)-sin(x)" #Minha Função
#function="abs(x**0.5)"
#function="-0.00108039*(x**6) + 0.0405309935*(x**5)-0.57956310299*(x**4)+3.90581289*(x**3)-12.301946476*(x**2)+15.058704795*x" 
#function="e**(-0.1*x)+(5*sin(x)+cos(0.1*x))"
function="e**0.1*x+sin(8*x)+cos(x)-1"

r = simpson(a,b,function,nPontos) #Pode ou não passar o 3 e 4 (nPontos,precisao exibida no resultado)e ver o numero de casas decimais desejado
trapezios(a,b,function,nPontos)

xEstimado, yEstimado = np.array(geraListaPontos(a,b,function,nPontos)) #Tem que ser np.array para funcionar!
xReal, yReal = np.array(geraListaPontos(a-((b-a)/10),b+((b-a)/10),function,150000))

#Parte gráfica
fig = plt.figure()
graph = fig.add_subplot()
graph.plot(xReal, yReal , [a,b], [0,0], [b,b], [0,yEstimado[-1]], [a,a], [0,yEstimado[0]], "-", color="sienna")
graph.plot(xReal, yReal , "-", label="fx real", color="black")
graph.plot(xEstimado,yEstimado, ":",label="fx estimada",color="dimgrey")

graph.fill_between(xEstimado,0,yEstimado,where=yEstimado>=0,color="lawngreen",interpolate=True) #Pinta região do gráfico
graph.fill_between(xEstimado,0,yEstimado,where=yEstimado<0,color="r",interpolate=True)

plt.title("Área aproximada envolvida pela f(x) = " + str(r)) #Título do Plot
plt.xlabel("X") #Legenda X
plt.ylabel("Y") #Legenda Y

plt.grid()

plt.legend() #Coloca legenda na tela
plt.show() #Coloca interface na tela