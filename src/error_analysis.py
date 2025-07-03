import math
import numpy as np
import matplotlib.pyplot as plt
from ivp import assumptions, IVP, exactSolution
from euler import eulerMethod, eulerStep
from rk4 import rk4Method, rk4Step

t_initial, t_final, N_0, decay_constant = assumptions()

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

t_h1_rk4, N_h1_rk4 = rk4Method(IVP, N_0, t_initial, t_final, h1)
t_h2_rk4, N_h2_rk4 = rk4Method(IVP, N_0, t_initial, t_final, h2)
t_h3_rk4, N_h3_rk4 = rk4Method(IVP, N_0, t_initial, t_final, h3)
t_h4_rk4, N_h4_rk4 = rk4Method(IVP, N_0, t_initial, t_final, h4)
t_h5_rk4, N_h5_rk4 = rk4Method(IVP, N_0, t_initial, t_final, h5)

error25_euler = [exactSolution(t) - N_h1_euler[i] for i, t in enumerate(t_h1_euler)]
print("Euler error at h = 25:", round(exactSolution(100) - N_h1_euler[-1], 2), "grams")
error25_rk4 = [exactSolution(t) - N_h1_rk4[i] for i, t in enumerate(t_h1_rk4)]
print("RK4 error at h = 25:", round(exactSolution(100) - N_h1_rk4[-1], 2), "grams\n")

error20_euler = [exactSolution(t) - N_h2_euler[i] for i, t in enumerate(t_h2_euler)]
print("Euler error at h = 20:", round(exactSolution(100) - N_h2_euler[-1], 2), "grams")
error20_rk4 = [exactSolution(t) - N_h2_rk4[i] for i, t in enumerate(t_h2_rk4)]
print("RK4 error at h = 20:", round(exactSolution(100) - N_h2_rk4[-1], 2), "grams\n")

error10_euler = [exactSolution(t) - N_h3_euler[i] for i, t in enumerate(t_h3_euler)]
print("Euler error at h = 10:", round(exactSolution(100) - N_h3_euler[-1], 2), "grams")
error10_rk4 = [exactSolution(t) - N_h3_rk4[i] for i, t in enumerate(t_h3_rk4)]
print("RK4 error at h = 10:", round(exactSolution(100) - N_h3_rk4[-1], 2), "grams\n")

error1_euler = [exactSolution(t) - N_h4_euler[i] for i, t in enumerate(t_h4_euler)]
print("Euler error at h = 1:", round(exactSolution(100) - N_h4_euler[-1], 2), "grams")
error1_rk4 = [exactSolution(t) - N_h4_rk4[i] for i, t in enumerate(t_h4_rk4)]
print("RK4 error at h = 1:", round(exactSolution(100) - N_h4_rk4[-1], 2), "grams\n")

error01_euler = [exactSolution(t) - N_h5_euler[i] for i, t in enumerate(t_h5_euler)]
print("Euler error at h = 0.1:", round(exactSolution(100) - N_h5_euler[-1], 2), "grams")
error01_rk4 = [exactSolution(t) - N_h5_rk4[i] for i, t in enumerate(t_h5_rk4)]
print("RK4 error at h = 0.1:", round(exactSolution(100) - N_h5_rk4[-1], 2), "grams")

plt.figure(figsize = (14, 8))
plt.plot(t_h1_euler, error25_euler, '.-', label = 'h = 25')
plt.plot(t_h2_euler, error20_euler, '.-', label = 'h = 20')
plt.plot(t_h3_euler, error10_euler, '.-', label = 'h = 10')
plt.plot(t_h4_euler, error1_euler, '.-', label = 'h = 1')
plt.plot(t_h5_euler, error01_euler, '.-', label = 'h = 0.1')
plt.title('Error Size of the Decay Model (Euler Method)')
plt.xlabel('Number of Years Past')
plt.ylabel('Quantity of Error (g)')
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()

plt.figure(figsize = (14, 8))
plt.plot(t_h1_rk4, error25_rk4, '.-', label = 'h = 25')
plt.plot(t_h2_rk4, error20_rk4, '.-', label = 'h = 20')
plt.plot(t_h3_rk4, error10_rk4, '.-', label = 'h = 10')
plt.plot(t_h4_rk4, error1_rk4, '.-', label = 'h = 1')
plt.plot(t_h5_rk4, error01_rk4, '.-', label = 'h = 0.1')
plt.title('Error Size of the Decay Model (RK4 Method)')
plt.xlabel('Number of Years Past')
plt.ylabel('Quantity of Error (g)')
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()