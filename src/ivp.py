import math
import numpy as np

def assumptions():
    t_initial = 0
    t_final = 100
    N_0 = 1600
    decay_constant = (math.log(2) / 30) * (-1)
    return t_initial, t_final, N_0, decay_constant

def IVP(t:float, N: float) -> float:
    _, _, _, decay_constant = assumptions()
    return decay_constant * N

def exactSolution(t: float) -> float:
    _, _, N_0, decay_constant = assumptions()
    return N_0 * math.exp(decay_constant * t)