import matplotlib.pyplot as plt
import numpy as np
from math import *

def symetrieAxeY(Lx,Ly,value):
    Lxfinal=[]
    
    for i in Lx:
        Lxfinal.append(-i+2*value)
    return [Lxfinal,Ly]


def symetrieAxeX(Lx,Ly,value):
    Lyfinal=[]
    
    for i in Ly:
        Lyfinal.append(-i+2*value)
    return [Lx,Lyfinal]


def Phi1(x):
    return (x-1)*(x-1)*(2*x+1)

def Phi2(x):
    return x*x*(-2*x+3)

def Phi3(x):
    return (x-1)*(x-1)*x

def Phi4(x):
    return (x-1)*x*x


def interpollationHermite(Lx,Ly,Ld):
    X=[]
    Y=[]
    
    if len(Lx)<2:
        print("Tailles des listes trop faibles")
        return [[],[]]
    if len(Lx)!=len(Ly) or len(Ly)!=len(Ld):
        print("Tailles des listes différentes")
        return [[],[]]

    for i in range(len(Lx)-1):
        min = Lx[i]
        max = Lx[i+1]

        n=100
        h=(max-min)/n

        X2=[]
        Y2=[]
        for j in range(n):
            X2.append(min + h*j)

            value = Ly[i]*Phi1((X2[j]-Lx[i])/(Lx[i+1]-Lx[i])) + Ly[i+1]*Phi2((X2[j]-Lx[i])/(Lx[i+1]-Lx[i])) + (Lx[i+1]-Lx[i])*Ld[i]*Phi3((X2[j]-Lx[i])/(Lx[i+1]-Lx[i])) + (Lx[i+1]-Lx[i])*Ld[i+1]*Phi4((X2[j]-Lx[i])/(Lx[i+1]-Lx[i]))
            Y2.append(value)
        X+=X2
        Y+=Y2
    return [X,Y]




def drawForm(isSymX,isSymY,valueX,valueY,listpoint) :
    for i in range (len(listpoint)-1) :
        # choix d'avoir des "angles symétriques" : dérivée d en entrée -d en sortie
        Lx=[listpoint[i][0],listpoint[i+1][0]]
        Ly=[listpoint[i][1],listpoint[i+1][1]]
        Ld=[-listpoint[i][2],listpoint[i+1][2]]
        L=interpollationHermite(Lx,Ly,Ld)

        plt.plot(L[0],L[1])

        if (not isSymX and not isSymY):
            Lx2=[listpoint[len(listpoint)-1][0],listpoint[0][0]]
            Ly2=[listpoint[len(listpoint)-1][1],listpoint[0][1]]
            Ld2=[-listpoint[len(listpoint)-1][2],listpoint[0][2]]
            L2=interpollationHermite(Lx2,Ly2,Ld2)
        
            plt.plot(L2[0],L2[1])

            # si la symétrie est sur les 2, on commence par touver les points en X puis en Y
        if (isSymX):
            symList = symetrieAxeX(L[0],L[1],valueX)
            plt.plot(symList[0],symList[1])

            totalListX = symList[0]
            for val in L[0]:
                totalListX.append(val)

            totalListY = symList[1]
            for val in L[1]:
                totalListY.append(val)

            if (isSymY):
                symYList = symetrieAxeY(totalListX,totalListY,valueY)

        if (isSymY and not isSymX):
            symList=symetrieAxeY(L[0],L[1],valueY)
            plt.plot(symList[0],symList[1])

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Forme générée')
    plt.show()

# Premier exemple

P1=[1.8,6.2,-3]
plt.scatter(P1[0],P1[1])
P2=[6,7,2]
plt.scatter(P2[0],P2[1])
P3=[3.6,9.4,-2]
plt.scatter(P3[0],P3[1])
P4=[8.6,8.2,-4]
plt.scatter(P4[0],P4[1])
P5=[7.4,5.7,4]
plt.scatter(P5[0],P5[1])
P6=[9.4,5.4,0]
plt.scatter(P6[0],P6[1])
P7=[9.5,3.8,-4]
plt.scatter(P7[0],P7[1])
P8=[5.8,2.6,2]
plt.scatter(P8[0],P8[1])
P9=[6,1.8,-2.5]
plt.scatter(P9[0],P9[1])
P10=[2.2,2.2,-2.5]
plt.scatter(P10[0],P10[1])

lPoint=[P1,P2,P3,P4,P5,P6,P7,P8,P9,P10]
drawForm(False,False,0,0,lPoint)

#-------------------------EXEMPLE UTILISATION-------------------------------

# P1=[5,7,0]
# P2=[4.3,6,4]
# P3=[5,5,0]
# P4=[4.2,3.4,3.5]
# P5=[5,2,0]
# P6=[4,1,0]
# P7=[2,2,-4]
# P8=[3,4,0]
# P9=[1,8,-4]
# P10=[3,10,0.3]
# P11=[5,7,-1.5]

# lPoint=[P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11]

# #drawForm(False,True,0,5,lPoint)