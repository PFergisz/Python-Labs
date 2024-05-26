#! /usr/bin/env python3

import random
import matplotlib.pyplot as plt
import math

#zad.1
print("zad.1")

class IFS:
    def __init__(self, transformation, probability=None):
        self.point = (0,0)
        self.transformation = transformation
        self.probability = probability
        self.factors = []
        self.factors.append(self.point)

    def change(self, iterations):
        for i in range(iterations):
            par = random.choices(self.transformation, weights=self.probability, k=1)[0]
            self.point = (par[0]*self.point[0] + par[1]*self.point[1] + par[2], par[3]*self.point[0] + par[4]*self.point[1] + par[5])
            self.factors.append(self.point)

    def draw(self):
        x_axis = [point[0] for point in self.factors]
        y_axis = [point[1] for point in self.factors]
        plt.plot(x_axis, y_axis, ".", markersize=1)
        plt.show()


# test1 = IFS(((0.787879, -0.424242, 1.758647, 0.242424, 0.859848, 1.408065), (-0.121212, 0.257576, -6.721654, 0.151515, 0.05303, 1.377236), (0.181818, -0.136364, 6.086107, 0.090909, 0.181818, 1.568035)), (0.90, 0.05, 0.05))
# test1.change(50000)
# test1.draw()

# test2 = IFS(((0, 0.053, -7.083, -0.429, 0, 5.43), (0.143, 0, -5.619, 0, -0.053, 8.513), (0.143, 0, -5.619, 0, 0.083, 2.057), (0, 0.053, -3.952, 0.429, 0, 5.43), (0.119, 0, -2.555, 0, 0.053, 4.536), (-0.0123806, -0.0649723, -1.226, 0.423819, 0.00189797, 5.235), (0.0852291, 0.0506328, -0.421, 0.420449, 0.0156626, 4.569), (0.104432, 0.00529117, 0.976, 0.0570516, 0.0527352, 8.113), (-0.00814186, -0.0417935, 1.934, 0.423922, 0.00415972, 5.37), (0.093, 0, 0.861, 0, 0.053, 4.536), (0, 0.053, 2.447, -0.429, 0, 5.43), (0.119, 0, 3.363, 0, -0.053, 8.513), (0.119, 0, 3.363, 0, 0.053, 1.487), (0, 0.053, 3.972, 0.429, 0, 4.569), (0.123998, -0.00183957, 6.275, 0.000691208, 0.0629731, 7.716), (0, 0.053, 5.215, 0.167, 0, 6.483), (0.071, 0, 6.279, 0, 0.053, 5.298), (0, -0.053, 6.805, -0.238, 0, 3.714), (-0.121, 0, 5.941, 0, 0.053, 1.487)))
# test2.change(50000)
# test2.draw()

# test3 = IFS(((0.824074, 0.281428, -1.88229, -0.212346, 0.864198, -0.110607), (0.088272, 0.520988, 0.78536, -0.463889, -0.377778, 8.095795)),  (0.8, 0.2))
# test3.change(50000)
# test3.draw()






#zad.2
print("\nzad.2")

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, vector):
        return Vector3D(self.x + vector.x, self.y + vector.y, self.z + vector.z)
    
    __radd__ = __add__

    def __iadd__(self, vector):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z
        return self

    def __sub__(self, vector):
        return Vector3D(self.x - vector.x, self.y - vector.y, self.z - vector.z)
    

    __rsub__ = __sub__

    def __isub__(self, vector):
        self.x -= vector.x
        self.y -= vector.y
        self.z -= vector.z
        return self

    def __mul__(self, a):
        return Vector3D(self.x*a, self.y*a, self.z*a)
    
    __rmul__ = __mul__

    def __imul__(self, a):
        self.x *= a
        self.y *= a
        self.z *= a
        return self       

    def __str__(self):
        return f'x={self.x} y={self.y} z={self.z}'

    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def scal(self, vector):
        return self.x * vector.x + self.y * vector.y + self.z * vector.z 

    def vec(self, vector):
        x = self.y * vector.z - self.z * vector.y
        y = self.z * vector.x - self.x * vector.z
        z = self.x * vector.y - self.y * vector.x
        return Vector3D(x, y, z)
    
    def mix(self, vector1, vector2):
        return vector2.scal(self.vec(vector1))


v1 = Vector3D(1,2,3)
v2 = Vector3D(4,5,6)
v3 = Vector3D(7,9,9)
print(v1+v2)
print(v1)
print(v1.length())
print(v1.scal(v2))
print(v1.vec(v2))
print(v1.mix(v2,v3))


#zad.3
print("\nzad.3")

B = Vector3D(1,2,3)
S = Vector3D(4,5,6)
v = Vector3D(7,9,9)
E = Vector3D(1,1,1)


def induction(B, S):
    if isinstance(B, Vector3D) and isinstance(S, Vector3D):
        return B.scal(S)

def lorentz(q, E, v, B):
    if isinstance(B, Vector3D) and isinstance(v, Vector3D) and isinstance(E, Vector3D):
        return q*(E+v.vec(B))

def force(q, E, v):
    if isinstance(E, Vector3D) and isinstance(v, Vector3D):
        return q*E.scal(v)


print(induction(B,S))
print(lorentz(1,E,v,B))
print(force(1,E,v))