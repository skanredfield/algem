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
p6 = (20, 40)
p7 = (22, 50)
p8 = (30, 51)
p9 = (32, 56)
p10 = (40, 60)
points = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

xpoints = np.array([p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0], p9[0], p10[0]])
ypoints = np.array([p1[1], p2[1], p3[1], p4[1], p5[1], p6[1], p7[1], p8[1], p9[1], p10[1]])

print(plt.style.available)
plt.style.use('seaborn-v0_8')

plt.plot(xpoints, ypoints, 'o')

x = np.linspace(-5, 41, 200)

plt.plot(x, lagrange.interpolate(points, x))

plt.show()