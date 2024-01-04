import sys
import numpy as np


NTAB = 10
CON = 1.4
CON2 = CON * CON
BIG = sys.float_info.max
SAFE = 2.0


# implementation from the Numerical Recipes book
def derive(f, x, h, err):
    if h == 0.0:
        raise Exception("h must be nonzero")
    
    ans = 0.0
    a = np.empty(shape=(NTAB, NTAB))
    hh = h
    a[0][0] = (f(x+hh) - f(x-hh)) / (2.0 * hh)
    err = BIG
    
    for i in range(1, NTAB):
        hh /= CON
        a[0][i] = (f(x+hh) - f(x-hh)) / (2.0 * hh)
        fac = CON2
        for j in range(1, i+1):
            a[j][i] = (a[j-1][i]*fac - a[j-1][i-1]) / (fac - 1.0)
            fac = CON2 * fac
            errt = max(abs(a[j][i]-a[j-1][i]), abs(a[j][i]-a[j-1][i-1]))
            if errt <= err:
                err = errt
                ans = a[j][i]
        
        if abs(a[i][i]-a[i-1][i-1]) >= (SAFE * err): break
    
    return ans


angle = np.pi / 4.0
print("Original: ", np.sin(angle))
der = derive(np.sin, angle, 0.01, 0.0001)
print("Derivative: ", der)