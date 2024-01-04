class RungeKutta4:

    def integrate(self, f, x0, y0, xn, dx):
        x = x0
        y = y0
        n = int((xn - x0) / dx)
        xs = [x]
        ys = [y]

        for _ in range(1, n + 1):
            k1 = dx * f(x, y)
            k2 = dx * f(x + 0.5 * dx, y + 0.5 * k1)
            k3 = dx * f(x + 0.5 * dx, y + 0.5 * k2)
            k4 = dx * f(x + dx, y + k3)

            x = x + dx
            y = y + (k1 / 6.0 + k2 / 3.0 + k3 / 3.0 + k4 / 6.0)
            
            xs.append(x)
            ys.append(y)
        
        return xs, ys
    