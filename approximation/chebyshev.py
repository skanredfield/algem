import numpy as np


class Chebyshev:

    def __init__(self, func, n) -> None:
        self.func = func
        self.n = n

    def approximate(self, x):
        res = sum([(self._c(j) * self._T(x, j)) for j in range(self.n)])
        return res - 0.5 * self._c(0)

    def _T(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        return 2 * x * self._T(x, n-1) - self._T(x, n-2)
    
    def _c(self, j):
        res = 0
        for k in range(self.n):
            res += self.func(np.cos(np.pi * (k + 0.5) / self.n)) * np.cos(np.pi * j * (k + 0.5) / self.n)
        return res * 2.0 / self.n


angle = np.pi / 4.0
print("Chebyshev original: ", np.sin(angle))

ch = Chebyshev(np.sin, 10)
print("Chebyshev approximation: ", ch.approximate(angle))