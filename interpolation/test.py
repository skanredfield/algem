import matplotlib.pyplot as plt
import numpy as np
from newton import NewtonInterpolator
from lagrange import LagrangeInterpolator


newton = NewtonInterpolator()
lagrange = LagrangeInterpolator()


p1 = (1, 2)
p2 = (2, 3)
p3 = (4, 11)
p4 = (7, 20)
p5 = (15, 22)
points = [p1, p2, p3, p4, p5]

xpoints = np.array([p1[0], p2[0], p3[0], p4[0], p5[0]])
ypoints = np.array([p1[1], p2[1], p3[1], p4[1], p5[1]])

print(plt.style.available)
plt.style.use('seaborn-v0_8')

plt.plot(xpoints, ypoints, 'o')

x = np.linspace(-5, 20, 100)

plt.plot(x, lagrange.interpolate(points, x))

plt.show()