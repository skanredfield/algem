import numpy as np
import matplotlib.pyplot as plt
from functools import wraps
import time
from fourier import *

# https://stackoverflow.com/questions/15707056/get-time-of-execution-of-a-block-of-code-in-python-2-7
# https://stackoverflow.com/questions/5929107/decorators-with-parameters
def time_usage(label):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            beg_ts = time.time()
            retval = func(*args, **kwargs)
            end_ts = time.time()
            print("(%s) Elapsed time: %f" % (label, (end_ts - beg_ts)))
            return retval
        return wrapper
    return decorator


N = 1024

freq1 = 13                                        # wave frequency
freq2 = 4                                        # wave frequency
amp = 1.0                                       # wave amplitude
duration = 1.0                                  # wave duration

delta_t = duration / N                          # spacing of time values

tvals = np.linspace(0, (N-1) * delta_t, N)      # sampling values
f_t1 = np.cos(2 * np.pi * freq1 * tvals)          # function to transform
f_t2 = np.cos(2 * np.pi * freq2 * tvals)          # function to transform
f_t = f_t1 + f_t2



delta_f = 1 / (N * delta_t)                     # spacing of frequency values
freqvals = np.linspace(0, (N-1) * delta_f, N)   # output frequency values
freqvals -= (N/2) * delta_f                     # shift half to center on 0 and include the negative values
    



fig, ax = plt.subplots(4, 1)

def plot(axis, title, xlabel, ylabel, xs, ys):
    axis.set_title(title)
    axis.set_xlabel(xlabel)
    axis.set_ylabel(ylabel)
    axis.plot(xs, ys, '.')

def plot_time_function():
    plot(ax[0], "f(t)", "Time (seconds)", "Amplitude", tvals, f_t)

@time_usage("DFT")
def plot_dft():
    plot(ax[1], "dft(f)", "Frequency", "Re(dft(f))", freqvals, fourier_shift(dft_matrix(f_t)))

@time_usage("FFT")
def plot_fft():
    plot(ax[2], "fft(f)", "Frequency", "Re(fft(f))", freqvals, fourier_shift(fft(f_t)))

@time_usage("IFFT")
def plot_ifft():
    plot(ax[3], "ifft(f)", "Time (seconds)", "Amplitude", tvals, ifft(fft(f_t)))

plot_time_function()
plot_dft()
plot_fft()
plot_ifft()

fig.tight_layout()
plt.show()