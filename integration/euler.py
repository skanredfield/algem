class Euler:

    def integrate(self, f, x0, y0, xn, dx):
        x = x0
        y = y0
        n = int((xn - x0) / dx)
        xs = [x]
        ys = [y]

        for _ in range(1, n + 1):
            y = y + dx * f(x, y)
            x = x + dx

            xs.append(x)
            ys.append(y)
        
        return xs, ys