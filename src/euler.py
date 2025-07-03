import math
import numpy as np
import matplotlib.pyplot as plt
from ivp import assumptions, IVP, exactSolution

t_initial, t_final, N_0, decay_constant = assumptions()

def eulerStep(f:callable, t:float, y:float, h:float) -> float:
    return y + h * f(t, y)

def eulerMethod(f:callable, N_0:float, t_initial:float, t_final:float, h:float) -> tuple[list[float], list[float]]:
    n = int((t_final - t_initial) / h)
    
    t_values = np.linspace(t_initial, t_final, n + 1)
    N_values = np.zeros(n + 1)
    N_values[0] = N_0
    
    for i in range(n):
        N_values[i + 1] = eulerStep(f, t_values[i], N_values[i], h)
        
    return t_values, N_values

h1 = 25
h2 = 20
h3 = 10
h4 = 1
h5 = 0.1

t_h1_euler, N_h1_euler = eulerMethod(IVP, N_0, t_initial, t_final, h1)
t_h2_euler, N_h2_euler = eulerMethod(IVP, N_0, t_initial, t_final, h2)
t_h3_euler, N_h3_euler = eulerMethod(IVP, N_0, t_initial, t_final, h3)
t_h4_euler, N_h4_euler = eulerMethod(IVP, N_0, t_initial, t_final, h4)
t_h5_euler, N_h5_euler = eulerMethod(IVP, N_0, t_initial, t_final, h5)

plt.figure(figsize = (14, 8))

plt.plot(t_h1_euler, N_h1_euler, '.-', label = 'h = 25')
plt.plot(t_h2_euler, N_h2_euler, '.-', label = 'h = 20')
plt.plot(t_h3_euler, N_h3_euler, '.-', label = 'h = 10')
plt.plot(t_h4_euler, N_h4_euler, '.-', label = 'h = 1')
plt.plot(t_h5_euler, N_h5_euler, '.-', label = 'h = 0.1')

t_values = np.linspace(t_initial, t_final, 100)
N_values = [exactSolution(t) for t in t_values]
plt.plot(t_values, N_values, label = 'Exact Solution', linewidth = 2)

plt.title('Decay of Cesium-137 in Isar 2 (Euler Method)')
plt.xlabel('Number of Years Past')
plt.ylabel('Quantity (g)')
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()

print("Exact solution:", round(exactSolution(100),2), "grams\n")

print("Step size of 25:")
for t, y in zip(t_h1_euler, N_h1_euler):
    print(f"At year {t:.2f}: {y:.2f}g left")

print("\nStep size of 0.1:")
for t, y in zip(t_h5_euler, N_h5_euler):
    print(f"At year {t:.2f}: {y:.2f}g left")