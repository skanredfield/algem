from interpolator import Interpolator


class LagrangeInterpolator(Interpolator):

    def interpolate(self, points, x):
        num_terms = len(points)
        it_range = range(num_terms)
        poly = 0
        for i in it_range:
            p = points[i]
            term = p[1]
            for j in it_range:
                if i != j:
                    term = term * (x - points[j][0]) / (p[0] - points[j][0])
            poly = poly + term
        
        return poly
