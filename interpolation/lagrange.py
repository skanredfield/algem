import matplotlib.pyplot as plt
import numpy as np

def interpolate(points, x):
    num_terms = len(points)
    it_range = range(num_terms)
    #TODO: 1. the special case of the points being in linear dependence should be covered
    #TODO: 2. the case of only two points should be covered
    for i in it_range:
        p = points[i]
        poly = 0
        term = p[1]
        for j in it_range:
            if i != j:
                term = term * (x - points[j][0]) / (p[0] - points[j][0])
        poly = poly + term
    
    return poly

p1 = (1, 2)
p2 = (2, 3)
p3 = (4, 11)
points = [p1, p2, p3]

xpoints = np.array([p1[0], p2[0], p3[0]])
ypoints = np.array([p1[1], p2[1], p3[1]])

print(plt.style.available)
plt.style.use('seaborn-v0_8')

plt.plot(xpoints, ypoints, 'o')

x = np.linspace(-20, 25, 100)
plt.plot(x, interpolate(points, x))

plt.show()