import itertools, time
import numpy as np  # pip install numpy
from scipy.linalg import expm, norm # pip install scipy

L = 2 * np.identity(6)
for k in range(0,5):
    L[k, k+1] = -1
    L[k+1, k] = -1
L [0,5] = -1
L [5,0] =-1
print("L " , L )
def U (t:int):
    return expm(-1j * L * t )
# print(U(1)) No sé quien eres pero te encontrare y te voy a matar

def getLaplacian(nPoints:int):
    L = 2 * np.identity(nPoints)
    for k in range(0, nPoints-1):
        k
        L[k, k+1] = -1
        L[k+1, k] = -1

    L [0, -1] = -1
    L [-1, 0] =-1
    return L

def getUnitary(tempo, lapacian):
    return expm(-1j * lapacian * tempo )

def basis(n:int, nPoints:int):
    n -=1
    v = list(itertools.repeat(0, nPoints))
    v[n] = 1
    return v


def getProba(initial:int, final:int, tempo: int, L, L_size):
    amp = np.dot(basis(final, L_size), getUnitary(tempo, L))
    amp = np.dot((amp), basis(initial, L_size))
    # print(type(amp))
    prob = norm(amp) **2
    return prob

L = getLaplacian(100)
inicio = time.time()
res = getProba(1, 50, 10, L, 100)
fin = time.time()
print(res)
print("tiempo de ejeccución:  ",  fin-inicio)

# Pequeña modificación, paso como parametro el largo del Laplaciano porque no sé como calcular su tamaño en python gg