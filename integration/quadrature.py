import numpy as np


class TrapezoidClosedQuadrature:

    def integrate(self, f, a, b, n):
        """
        Integrates f(x) on a closed interval [a, b] in n steps.
        """
        result = 0
        dx = (b-a) / n
        xi = a
        xf = a + dx
        for _ in range(n):
            result += (0.5 * dx * (f(xi) + f(xf)))
            xi = xf
            xf += dx
        result += dx * f(b)
        return result
    
tcq_integrator = TrapezoidClosedQuadrature()

val = tcq_integrator.integrate(np.sin, 0, np.pi, 100)
print("Sine function from 0 to PI is ", val)
