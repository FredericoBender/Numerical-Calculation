#Encoding=utf-8
from math import *
### function sempre em termos de x ###
#Retorna o resultado aproximado da integral definida por Regra de Trapezios
def trapezios(a,b,function,nPontos=100001,precisao=3): #Integração pela soma de vários trapézios
    def geraPontos(a,b,h,function): #Gera os pontos Y baseado no passo
        pontosY = []
        while(a<=b):
            x=a #Para usar "a" na função
            y = eval(function)
            pontosY.append(y)
            erroPC=a
            a+=h
        if(len(pontosY)<nPontos):
            x=b #Para usar "b" na função
            y = eval(function) #Adiciona o ponto final para o calculo, já que à um erro usando float no PC, pois ele trabalha em binário
            pontosY.append(y)
        return pontosY

    h = (b-a) / (nPontos - 1) #Cálcula o Passo
    pontos=geraPontos(a,b,h,function)
    somatorio = pontos[0]+pontos[-1] #fx0 + fxn
    somatorio2 = 0
    for i in pontos[1:-1:1]: #fx1+fx2+...+fxn-1
        somatorio2 = somatorio2 + i
    somatorio2 = 2 * somatorio2
    somatorio = round((h/2) * (somatorio + somatorio2),precisao)
    print("Integration of Trapezoids = " + str(somatorio))
    return somatorio

#Retorna o resultado aproximado da integral definida por Regra de Simpson
def simpson(a,b,function,nPontos=100001,precisao=3): #Integração pela soma de várias parábolas
    def geraPontos(a,b,h,function): #Gera os pontos Y baseado no passo
        pontosY = []
        while(a<=b):
            x=a #Para usar "a" na função
            y = eval(function)
            pontosY.append(y)
            a+=h
        if(len(pontosY)<nPontos):    
            x=b #Para usar "b" na função
            y = eval(function) #Adiciona o ponto final para o calculo, já que à um erro usando float no PC, pois ele trabalha em binário
            pontosY.append(y)
        return pontosY

    if (nPontos%2==0): #Verifica se nPontos é ímpar
        raise Exception("nPontos deve ser ímpar!")

    h = (b-a) / (nPontos - 1) #Cálcula o Passo
    pontos=geraPontos(a,b,h,function)

    somatorio = pontos[0]+pontos[-1] #fx0 + fxn
    somatorio2 = 0
    for i in pontos[1:-1:2]: #fx1+fx3+...+fxn-1
        somatorio2 = somatorio2 + i
    somatorio2 = 4 * somatorio2

    somatorio = somatorio + somatorio2
    somatorio2 = 0

    for i in pontos[2:-1:2]: #fx2+fx4+...+fxn-2
        somatorio2 = somatorio2 + i
    somatorio2 = 2 * somatorio2   
    somatorio = round((h/3) * (somatorio + somatorio2),precisao)
    print("Integration of Simpson = " + str(somatorio))
    return somatorio

#Retorna o resultado pelo método de MIL para zero de FUNÇÕES NÃO LINEARES
def mil(function,precisaoNoResultado=3):
    x=0.5

    exibe = precisaoNoResultado #Calcula o numero da precisão
    calculado="0."
    for i in range(precisaoNoResultado):
        calculado = calculado +"0"
    precisaoNoResultado = eval(calculado + "1")
    
    cont=0
    while(True):
        try:
            x1 = eval(function)
        except:
            break
        a=abs(x1-x)
        if(a<precisaoNoResultado):
            x1=round(x1,exibe)
            print("Zero de função: " +function + " = " + str(x1))
            return x1
        x=x1
        cont+=1
        if(cont>10000):
            break
    print("Não converge")
    
def gaussJordan():
    pass

#IMPLEMENTAR

#RESOLUÇÃO DE SISTEMAS LINEARES
    #Gauss Jordan para sistemas lineares (Muito útil para sistemas pequenos).
    #Gauss Jacobi (Muito útil em sistemas grandes, como para circuitos por exemplo).
    #Gauss Seidel.

#AJUSTE DE CURVAS
    #Minimos quadrados, para polinomio de grau n, dada uma lista de pontos.
    #Exponencial, dada uma lista de pontos onde todo y>0.

#INTERPOLAÇÃO POLINOMIAL
    #Interpolação polinomial
        #HARD, TALVEZ NÃO FAÇA##Dada uma string (x-1)(x-5) = retornar a string de multiplicação resultante
        #HARD, TALVEZ NÃO FAÇA, OU UTILIZO FORMA ABREVIADA ex:(x-1)(x-0)##Interpolaçao pelo método de Newton