import numpy as np


def dft_loop(f):
    N = len(f)
    out = np.zeros(N)

    for freq in range(0, N):
        re = 0
        im = 0
        for val in range(0, N):
            duration = 1.0
            x = val * duration / N
            phi = 2 * np.pi * freq * x
            re += f[val] * np.cos(phi)
            im -= f[val] * np.sin(phi)
            
        re /= N
        im /= N
        out[freq] = re

    return out
        
# https://jakevdp.github.io/blog/2013/08/28/understanding-the-fft/
def dft_matrix(f):
    x = np.asarray(f, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


def fft(f):
    n = len(f)
    if n == 1:
        return f
    f_even, f_odd = f[0::2], f[1::2]
    y_even, y_odd = fft(f_even), fft(f_odd)
    y = [0] * n
    w = np.exp(2j * np.pi / n)
    half_n = int(n/2)
    for i in range(half_n):
        w_i = w**i
        y[i] = y_even[i] + w_i * y_odd[i]
        y[i + half_n] = y_even[i] - w_i * y_odd[i]
    return y

def ifft(f):
    n = len(f)
    if n == 1:
        return f
    f_even, f_odd = f[0::2], f[1::2]
    y_even, y_odd = ifft(f_even), ifft(f_odd)
    y = [0] * n
    w = np.exp(-2j * np.pi / n)
    half_n = int(n/2)
    for i in range(half_n):
        w_i = w**i
        y[i] = y_even[i] + w_i * y_odd[i]
        y[i + half_n] = y_even[i] - w_i * y_odd[i]
    return [x/n for x in y]

print(fft([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
print(ifft(fft([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])))

def fourier_shift(ft):
    n = len(ft)
    half_n = int(n/2)
    new_dft = np.zeros(n)
    for i in range(0, half_n):
        new_dft[i] = ft[half_n - i]
    for i in range(half_n + 1, n):
        new_dft[i] = ft[n + half_n - i]
    return new_dft