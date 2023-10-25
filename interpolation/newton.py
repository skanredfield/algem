from interpolator import Interpolator

class NewtonInterpolator(Interpolator):

    def interpolate(self, points, x):
        num_terms = len(points)
        poly = 0
        for i in range(num_terms):
            term = self._compute_divided_difference(points, i, i)
            for j in range(i):
                term = term * (x - points[j][0])
            poly = poly + term
        return poly

    def _compute_divided_difference(self, points, level, index):
        if level == 0:
            return points[index][1]
        
        left_diff = self._compute_divided_difference(points, level - 1, index)
        right_diff = self._compute_divided_difference(points, level - 1, level - 1)

        return (left_diff - right_diff) / (points[index][0] - points[level - 1][0])
