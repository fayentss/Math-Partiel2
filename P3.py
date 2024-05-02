import matplotlib.pyplot as plt
import numpy as np
from math import *

#--------------------TRAJECTOIRE NAUTILUS----------------------------


def trajectoire_Nautilus(x0, y0, V0, F, ms, g, O, mu_water, D_nautilus, V, peau, t, n):

    h = t/n
    x = [x0, x0 + h * V0 * cos(O)]
    y = [y0, y0 + h * V0 * sin(O)]

    for i in range(n):
        x.append((((h**2) * 2*F)/ms) * cos(O) - ((3*pi*mu_water*D_nautilus*h)/ms) * (x[i + 1] - x[i]) + 2*x[i + 1] - x[i])
        y.append((((h**2) * 2*F)/ms) * sin(O) + ((3*pi*mu_water*D_nautilus*h)/ms) * (y[i + 1] - y[i]) + g*(h**2)*(((peau*V)/ms)-1) + 2*y[i + 1] - y[i])
    
    return x, y

x0 = 0  # Position initiale en x
y0 = -2  # Position initiale en y
V0 = 2  # Vitesse initiale en x
F = 50  # Force
ms = 200000 # Masse
g = 9.81  # Accélération gravitationnelle
V = 100   # Volume
O = -0.5 # Angle
mu_water = 0.000001  # Viscosité de l'eau
D_nautilus = 5  # Diamètre du Nautilus
peau = 1000 # Masse volumique de l'eau
t = 200
n = 1000

x, y = trajectoire_Nautilus(x0, y0, V0, F, ms, g, O, mu_water, D_nautilus, V, peau, t, n)

plt.plot(x, y)
plt.xlabel('Position en x')
plt.ylabel('Position en y')
plt.title('Trajectoire du Nautilus')
plt.grid(True)
plt.show()