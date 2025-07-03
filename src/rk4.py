import math
import numpy as np
import matplotlib.pyplot as plt
from ivp import assumptions, IVP, exactSolution

t_initial, t_final, N_0, decay_constant = assumptions()

def rk4Step(f:callable, t:float, y:float, h:float) -> float:
    k1 = h * f(t, y)
    k2 = h * f(t + 0.5 * h, y + 0.5 * k1)
    k3 = h * f(t + 0.5 * h, y + 0.5 * k2)
    k4 = h * f(t + h, y + k3)

    return y + (((k1) + (2 * k2) + (2 * k3) + (k4)) / 6)

def rk4Method(f:callable, N_0:float, t_initial:float, t_final:float, h:float) -> tuple[list[float], list[float]]:
    n = int((t_final - t_initial) / h)
    
    t_values = np.linspace(t_initial, t_final, n + 1)
    N_values = np.zeros(n + 1)
    N_values[0] = N_0
     
    for i in range(n):
        N_values[i + 1] = rk4Step(f, t_values[i], N_values[i], h)
        
    return t_values, N_values

h1 = 25
h2 = 20
h3 = 10
h4 = 1
h5 = 0.1

t_h1_rk4, N_h1_rk4 = rk4Method(IVP, N_0, t_initial, t_final, h1)
t_h2_rk4, N_h2_rk4 = rk4Method(IVP, N_0, t_initial, t_final, h2)
t_h3_rk4, N_h3_rk4 = rk4Method(IVP, N_0, t_initial, t_final, h3)
t_h4_rk4, N_h4_rk4 = rk4Method(IVP, N_0, t_initial, t_final, h4)
t_h5_rk4, N_h5_rk4 = rk4Method(IVP, N_0, t_initial, t_final, h5)

plt.figure(figsize = (14, 8))

plt.plot(t_h1_rk4, N_h1_rk4, '.-', label = 'h = 25')
plt.plot(t_h2_rk4, N_h2_rk4, '.-', label = 'h = 20')
plt.plot(t_h3_rk4, N_h3_rk4, '.-', label = 'h = 10')
plt.plot(t_h4_rk4, N_h4_rk4, '.-', label = 'h = 1')
plt.plot(t_h5_rk4, N_h5_rk4, '.-', label = 'h = 0.1')

t_values = np.linspace(t_initial, t_final, 100)
N_values = [exactSolution(t) for t in t_values]
plt.plot(t_values, N_values, label = 'Exact Solution', linewidth = 2)

plt.title('Decay of Cesium-137 in Isar 2 (RK4 Method)')
plt.xlabel('Number of Years Past')
plt.ylabel('Quantity (g)')
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()

print("Exact solution:", round(exactSolution(100),2), "grams\n")

print("Step size of 25:")
for t, y in zip(t_h1_rk4, N_h1_rk4):
    print(f"At year {t:.2f}: {y:.2f}g left")

print("\nStep size of 0.1:")
for t, y in zip(t_h5_rk4, N_h5_rk4):
    print(f"At year {t:.2f}: {y:.2f}g left")