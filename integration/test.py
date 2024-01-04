import numpy as np
import matplotlib.pyplot as plt
from rungekutta import RungeKutta4
from euler import Euler


rk4_integrator = RungeKutta4()
euler_integrator = Euler()

def dydx(x, y):
    return x**2

def y_solved(x):
    # For initial y0 = 1, x0 = 1
    return x**3 / 3.0 + 2 / 3.0

x0 = 1.0
y0 = 1.0
xn = 2.0
dx = 0.1

xs_rk4, ys_rk4 = rk4_integrator.integrate(dydx, x0, y0, xn, dx)
xs_euler, ys_euler = euler_integrator.integrate(dydx, x0, y0, xn, dx)


plt.figure(figsize=(7,5))

analytic_xs = np.linspace(x0, xn, int((xn - x0) / dx))
plt.plot(analytic_xs, y_solved(analytic_xs), 
         label="Analytical solution",color="red", lw=2)

plt.plot(xs_rk4, ys_rk4, label="Numerical solution:\nRunge-Kutta", dashes=(3,2), color="blue",
        lw=3)
plt.plot(xs_euler, ys_euler, label="Numerical solution:\nEuler", dashes=(3,2), color="green",
        lw=3)

plt.legend(loc="best", fontsize=12)
plt.title(r"Solution to ODE: $\quad\frac{dy}{dx}=x^2$")
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.show()
