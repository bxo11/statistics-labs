import random

import matplotlib.pyplot as plt
from math import *
import numpy as np

def polar():
    while(1):
        x1=random.uniform(-1,1)
        x2=random.uniform(-1,1)
        R=x1*x1+x2*x2
        if R<1 and R!=0:
            break
    y1=sqrt(-2*log(R)/R)*x1
    y2=sqrt(-2*log(R)/R)*x2
    return y1



points_anount = 50
x= np.linspace(-5,5,points_anount)
y=[]
wariancja = 1
wartosc_oczekiwana =0
for p in x:
    mianownik = wariancja*sqrt(2*pi)
    wyk = -((pow(p-wartosc_oczekiwana,2))/(2*pow(wariancja,2)))
    y.append((1/mianownik)*exp(wyk))

polar()

plt.plot(x,y, marker = 'o')
plt.show()