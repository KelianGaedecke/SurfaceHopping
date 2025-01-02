import numpy as np

def PES(A1 = 0.01, A2 = -0.01, B = 0.6, C = 0.001, D = 1, r):
    pes[0,0] = A1 * tanh(B*r)
    pes[0,1] = C * np.exp(-D * r**2)
    pes[1,0] = C * np.exp(-D * r**2)
    pes[1,1] = A2 * tanh(B*r)

    

    